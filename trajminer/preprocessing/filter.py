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
    n_tids, n_data, n_labels = [], [], []
    has_labels = data.get_labels() is not None

    for i, tid in enumerate(data.get_tids()):
        traj = data.get_trajectory(tid)

        if (min_length is not None and len(traj) < min_length) or \
           (max_length is not None and len(traj) > max_length):
            continue

        n_tids.append(tid)
        n_data.append(traj)

        if has_labels:
            n_labels.append(data.get_label(tid))

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
    labels_to_keep = []

    for label in enumerate(data.get_labels(unique=True)):
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
    pass
