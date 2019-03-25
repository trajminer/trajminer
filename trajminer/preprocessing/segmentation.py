from joblib import Parallel, delayed
from sklearn.utils import gen_even_slices
import numpy as np

from ..trajectory_data import TrajectoryData


class TrajectorySegmenter(object):
    """Trajectory segmenter.

    Parameters
    ----------
    attributes : array-like
        The attributes of a trajectory dataset.
    thresholds : dict (default=None)
        A dictionary with callables for the attributes that will be used in
        the segmentation (e.g. dict['key'] is the callable for attribute
        `key`). A callable takes as input two attribute values and outputs
        `True` if the trajectory should be segmented and `False` otherwise.

        For instance, suppose we have a dataset with a `time` attribute which
        represents the minutes from midnight when a trajectory point was
        recorded. If we'd like to segment trajectories every time there is a
        distance of more than 60 minutes between points, the callable for time
        would be defined as::

            lambda x, y: abs(x - y) > 60

        If ``None``, then trajectories are segmented whenever two attribute
        values are different (this behavior changes according to the `mode`
        parameter).
    mode : str (default='strict')
        A string in {'strict', 'any'}:

            - If 'strict', then trajectories are segmented when thresholds are
              `True` for all attributes.
            - If 'any', then trajectories are segmented when at least one
              threshold is `True` for any attribute.
    n_jobs : int (default=1)
        The number of parallel jobs.
    """

    def __init__(self, attributes, thresholds=None, mode='strict', n_jobs=1):
        self.attributes = attributes
        self.thresholds = thresholds
        self.mode = mode
        self.n_jobs = n_jobs

    def fit_transform(self, X):
        """Fit and segment trajectories.

        Parameters
        ----------
        X : :class:`trajminer.TrajectoryData`
            Input dataset to segment.

        Returns
        -------
        X_out : :class:`trajminer.TrajectoryData`
            Segmented dataset.
        """
        tids = X.get_tids()

        def segment(X, slice):
            def check_segment(p1, p2):
                if not self.thresholds and self.mode == 'any':
                    return not np.array_equal(p1, p2)
                elif not self.thresholds:
                    for i, f in enumerate(p1):
                        if f == p2[i]:
                            return False
                    return True
                else:
                    b = np.array([t(p1, p2)
                                  for attr, t in self.thresholds.items()])
                    return np.any(b) if self.mode == 'any' else np.all(b)

            ret = []

            for t in range(slice.start, slice.end):
                traj = X.get_trajectory(tids[t])
                s = [traj[0]]

                for i in range(1, len(traj)):
                    if check_segment(traj[i - 1], traj[i]):
                        ret.append(s)
                        s = [traj[i]]
                    else:
                        s.append(traj[i])
                ret.append(s)

            return ret

        func = delayed(segment)
        segments = Parallel(n_jobs=self.n_jobs, verbose=0)(
            func(X, s) for s in gen_even_slices(len(X.get_trajectories()),
                                                self.n_jobs))
        labels = X.get_labels()
        new_labels = None

        if labels:
            new_labels = []

            for idx, l in enumerate(labels):
                new_labels.append(np.full(len(segments[idx]), l))

        segments = np.concatenate(segments)
        new_tids = np.r_[1:len(segments) + 1]
        return TrajectoryData(attributes=X.get_attributes(),
                              data=segments,
                              tids=new_tids,
                              labels=new_labels)
