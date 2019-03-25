class TrajectoryData(object):
    """Trajectory data wrapper.

    Parameters
    ----------
    attributes : array-like
        The names of attributes/features describing trajectory points in the
        dataset.
    data : array-like, shape: (n_trajectories, n_points, n_features)
        The trajectory data.
    tids : array-like
        The corresponding trajectory IDs of trajectories in ``data``.
    labels : array-like (default=None)
        The corresponding labels of trajectories in ``data``.
    """

    def __init__(self, attributes, data, tids, labels=None):
        import numpy as np
        self.attributes = attributes
        self.tids = tids
        self.labels = labels
        self.data = np.array(data)
        self.stats = None
        self.tidToIdx = dict(zip(tids, np.r_[0:len(tids)]))

        if self.labels:
            self.labelToIdx = {}
            for i, label in enumerate(self.labels):
                if label in self.labelToIdx:
                    self.labelToIdx[label].append(i)
                else:
                    self.labelToIdx[label] = [i]

    def get_attributes(self):
        """Retrieves the attributes in the dataset.

        Returns
        -------
        attributes : array
            An array of length `n_features`.
        """
        return self.attributes

    def get_tids(self):
        """Retrieves the trajectory IDs in the dataset.

        Returns
        -------
        attributes : array
            An array of length `n_trajectories`.
        """
        return self.tids

    def get_labels(self, unique=False):
        """Retrieves the labels of the trajectories in the dataset.

        Parameters
        ----------
        unique : bool (default=False)
            If ``True``, then the set of unique labels is returned. Otherwise,
            an array with the labels of each individual trajectory is returned.

        Returns
        -------
        labels : array
            An array of length `n_trajectories` if `unique=False`, and of
            length `n_labels` otherwise.
        """
        if unique:
            return sorted(list(set(self.labels)))

        return self.labels

    def get_trajectory(self, tid):
        """Retrieves a trajectory from the dataset.

        Parameters
        ----------
        tid : int
            The trajectory ID.

        Returns
        -------
        trajectory : array, shape: (n_points, n_features)
            The corresponding trajectory.
        """
        return self.data[self.tidToIdx[tid]]

    def get_trajectories(self, label=None):
        """Retrieves multiple trajectories from the dataset.

        Parameters
        ----------
        label : int (default=None)
            The label of the trajectories to be retrieved. If ``None``, then
            all trajectories are retrieved.

        Returns
        -------
        trajectories : array
            The trajectories of the given label. If `label=None` or if the
            dataset does not contain labels, then all trajectories are
            returned.
        """
        if not label or not self.labels:
            return self.data

        idxs = self.labelToIdx[label]
        return self.data[idxs]
