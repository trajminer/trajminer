from joblib import Parallel, delayed
from sklearn.utils import gen_even_slices
import numpy as np

from ..trajectory_data import TrajectoryData


def filter_trajectory_length(data, min_length, max_length, inplace=True,
                             n_jobs=1):
    """Removes trajectories by length criteria.

    Parameters
    ----------
    data : :class:`trajminer.TrajectoryData`
        The dataset to be filtered.
    min_length : int
        The minimum length required (inclusive) to keep trajectories in the
        dataset. If `None`, then no minimum length is enforced.
    max_length : int
        The maximum length required (inclusive) to keep trajectories in the
        dataset. If `None`, then no maximum length is enforced.
    inplace : bool (default=True)
        If `True` modifies the current object, otherwise returns a new
        object.
    n_jobs : int (default=1)
        The number of parallel jobs.

    Returns
    -------
    dataset : :class:`trajminer.TrajectoryData`
        The filtered dataset. If `inplace=True`, then returns the modified
        current object.
    """
    has_labels = data.get_labels() is not None
    tids = data.get_tids()

    def filter(slice):
        n_tids, n_data, n_labels = [], [], []

        for i in range(slice.start, slice.stop):
            tid = tids[i]
            traj = data.get_trajectory(tid)

            if (min_length is not None and len(traj) < min_length) or \
               (max_length is not None and len(traj) > max_length):
                continue

            n_tids.append(tid)
            n_data.append(traj)

            if has_labels:
                n_labels.append(data.get_label(tid))

        return n_tids, n_data, n_labels

    func = delayed(filter)
    ret = Parallel(n_jobs=n_jobs, verbose=0)(
        func(s) for s in gen_even_slices(len(tids), n_jobs))

    n_tids, n_data, n_labels = [], [], []

    for job in ret:
        n_tids.extend(job[0])
        n_data.extend(job[1])
        n_labels.extend(job[2])

    if inplace:
        data._update(data.get_attributes(), n_data, n_tids, n_labels)
        return data

    return TrajectoryData(data.get_attributes(), n_data, n_tids, n_labels)


def filter_label_size(data, min_size, max_size, inplace=True, n_jobs=1):
    """Removes trajectories corresponding to sets of labels that do not meet
    size criteria.

    Parameters
    ----------
    data : :class:`trajminer.TrajectoryData`
        The dataset to be filtered.
    min_size : int
        The minimum number of trajectories (inclusive) required of a certain
        label to keep it in the dataset. If `None`, then no minimum size is
        enforced.
    max_size : int
        The maximum number of trajectories (inclusive) required of a certain
        label to keep it in the dataset. If `None`, then no maximum size is
        enforced.
    inplace : bool (default=True)
        If `True` modifies the current object, otherwise returns a new
        object.
    n_jobs : int (default=1)
        The number of parallel jobs.

    Returns
    -------
    dataset : :class:`trajminer.TrajectoryData`
        The filtered dataset. If `inplace=True`, then returns the modified
        current object.
    """
    labels = data.get_labels(unique=True)

    def filter(slice):
        labels_to_keep = []

        for i in range(slice.start, slice.stop):
            label = labels[i]
            size = len(data.get_trajectories(label))

            if (min_size is not None and size < min_size) or \
               (max_size is not None and size > max_size):
                continue
            labels_to_keep.append(label)

        n_tids, n_data, n_labels = [], [], []

        for i, tid in enumerate(data.get_tids()):
            traj = data.get_trajectory(tid)
            label = data.get_label(tid)

            if label not in labels_to_keep:
                continue

            n_tids.append(tid)
            n_data.append(traj)
            n_labels.append(label)

        return n_tids, n_data, n_labels

    func = delayed(filter)
    ret = Parallel(n_jobs=n_jobs, verbose=0)(
        func(s) for s in gen_even_slices(len(labels), n_jobs))

    n_tids, n_data, n_labels = [], [], []

    for job in ret:
        n_tids.extend(job[0])
        n_data.extend(job[1])
        n_labels.extend(job[2])

    if inplace:
        data._update(data.get_attributes(), n_data, n_tids, n_labels)
        return data

    return TrajectoryData(data.get_attributes(), n_data, n_tids, n_labels)


def filter_duplicate_points(data, criterium, remove_first=True, inplace=True,
                            n_jobs=1):
    """Removes duplicates of trajectory points according to the given criteria.

    Parameters
    ----------
    data : :class:`trajminer.TrajectoryData`
        The dataset to be filtered.
    criterium : callable
        A callable that takes two trajectory points and decides wheter or not
        they are duplicates. If `True`, then one of the points is removed from
        the dataset (the first or the last point, depending on the
        `remove_first` parameter).
    remove_first : bool (default=True)
        If `True`, then whenever duplicates are found, the first point is
        removed. Otherwise, the last one is removed from the dataset.
    inplace : bool (default=True)
        If `True` modifies the current object, otherwise returns a new
        object.
    n_jobs : int (default=1)
        The number of parallel jobs.

    Returns
    -------
    dataset : :class:`trajminer.TrajectoryData`
        The filtered dataset. If `inplace=True`, then returns the modified
        current object.
    """
    tids = data.get_tids()

    def filter(slice):
        n_data = []

        for t in range(slice.start, slice.stop):
            traj = np.copy(data.get_trajectory(tids[t]))
            i = 1

            while i < len(traj):
                if not criterium(traj[i-1], traj[i]):
                    i += 1
                elif remove_first:
                    traj = np.delete(traj, i-1, axis=0)
                else:
                    traj = np.delete(traj, i, axis=0)
            n_data.append(traj)

        return n_data

    func = delayed(filter)
    ret = Parallel(n_jobs=n_jobs, verbose=0)(
        func(s) for s in gen_even_slices(len(tids), n_jobs))

    n_data = np.concatenate(ret)

    if inplace:
        data._update(data.get_attributes(), n_data, data.get_tids(),
                     data.get_labels())
        return data

    return TrajectoryData(data.get_attributes(), n_data, data.get_tids(),
                          data.get_labels())
