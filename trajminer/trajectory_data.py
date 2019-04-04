import numpy as np


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
        self.attributes = attributes
        self.tids = np.array(tids)
        self.labels = np.array(labels) if labels is not None else None
        self.data = np.array(data)
        self._stats = None
        self.tidToIdx = dict(zip(tids, np.r_[0:len(tids)]))
        self.labelToIdx = self._get_label_to_idx(labels)

    def get_attributes(self):
        """Retrieves the attributes in the dataset.

        Returns
        -------
        attributes : array
            An array of length `n_features`.
        """
        return self.attributes

    def get_tids(self, label=None):
        """Retrieves the trajectory IDs in the dataset.

        Parameters
        ----------
        label : int (default=None)
            If `None`, then retrieves all trajectory IDs. Otherwise, returns
            the IDs corresponding to the given label.

        Returns
        -------
        attributes : array
            An array of length `n_trajectories`.
        """
        if not label or self.labels is None:
            return self.tids

        idxs = self.labelToIdx[label]
        return self.tids[idxs]

    def get_label(self, tid):
        """Retrieves the label for the corresponding tid.

        Parameters
        ----------
        tid : int
            The trajectory ID.

        Returns
        -------
        label : int or str
            The corresponding label.
        """
        return self.labels[self.tidToIdx[tid]]

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
        if unique and self.labels is not None:
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
        if not label or self.labels is None:
            return self.data

        idxs = self.labelToIdx[label]
        return self.data[idxs]

    def length(self):
        """Returns the number of trajectories in the dataset.

        Returns
        -------
        length : int
            Number of trajectories in the dataset.
        """
        return len(self.tids)

    def merge(self, other, ignore_duplicates=True, inplace=True):
        """Merges this trajectory data with another one. Notice that this
        method only works if the datasets have the same set of attributes.

        Parameters
        ----------
        other : :class:`trajminer.TrajectoryData`
            The dataset to be merged with.
        ignore_duplicates : bool (default=True)
            If `True`, then trajectory IDs in `other` that already exist in
            `self` are ignored. Otherwise, raises an exception when a duplicate
            is found.
        inplace : bool (default=True)
            If `True` modifies the current object, otherwise returns a new
            object.

        Returns
        -------
        dataset : :class:`trajminer.TrajectoryData`
            The merged dataset. If `inplace=True`, then returns the modified
            current object.
        """
        if set(self.attributes) != set(other.attributes):
            raise Exception("Cannot merge datasets with different sets of " +
                            "attributes!")

        n_attributes = self.attributes
        n_tids = self.tids.tolist()
        n_labels = self.labels.tolist()
        n_data = self.data.tolist()

        for tid in other.tids:
            if tid in n_tids:
                if ignore_duplicates:
                    continue
                raise Exception("tid", tid, "already exists in 'self'!")
            n_tids.append(tid)
            n_data.append(other.get_trajectory(tid))

            if n_labels is not None:
                n_labels.append(other.get_label(tid))

        if inplace:
            self._update(n_attributes, n_data, n_tids, n_labels)
            return self

        return TrajectoryData(n_attributes, n_data, n_tids, n_labels)

    def stats(self, print_stats=False):
        """Computes statistics for the dataset.

        Parameters
        ----------
        print_stats : bool (default=False)
            If `True`, stats are printed.

        Returns
        -------
        stats : dict
            A dictionary containing the dataset statistics.
        """
        if self._stats:
            if print_stats:
                self._print_stats()
            return self._stats

        traj_lengths = [len(x) for x in self.data]
        points = np.concatenate(self.data)

        def count_not_none(arr):
            return np.sum([1 if x is not None else 0 for x in arr])

        attr_count = [count_not_none(p) for p in points]

        self._stats = {
            'attribute': {
                'count': len(self.attributes),
                'min': np.min(attr_count),
                'avg': np.mean(attr_count),
                'std': np.std(attr_count),
                'max': np.max(attr_count)
            },
            'point': {
                'count': np.sum(traj_lengths)
            },
            'trajectory': {
                'count': len(self.data),
                'length': {
                    'min': np.min(traj_lengths),
                    'avg': np.mean(traj_lengths),
                    'std': np.std(traj_lengths),
                    'max': np.max(traj_lengths)
                }
            }
        }

        if self.labels is not None:
            unique, counts = np.unique(self.labels, return_counts=True)
            self._stats['label'] = {
                'count': len(unique),
                'min': np.min(counts),
                'avg': np.mean(counts),
                'std': np.std(counts),
                'max': np.max(counts)
            }

        if print_stats:
            self._print_stats()
        return self._stats

    def _update(self, attributes, data, tids, labels):
        self.tids = np.array(tids)
        self.labels = np.array(labels)
        self.data = np.array(data)
        self.tidToIdx = dict(zip(tids, np.r_[0:len(tids)]))
        self.labelToIdx = self._get_label_to_idx(labels)
        self._stats = None

    def _get_label_to_idx(self, labels):
        labelToIdx = None
        if labels is not None:
            labelToIdx = {}
            for i, label in enumerate(labels):
                if label in labelToIdx:
                    labelToIdx[label].append(i)
                else:
                    labelToIdx[label] = [i]

        return labelToIdx

    def _print_stats(self):
        print('==========================================================')
        print('                           STATS                          ')
        print('==========================================================')
        print('ATTRIBUTE')
        print('  Count:           ', self._stats['attribute']['count'])
        print('  Min:             ', self._stats['attribute']['min'])
        print('  Max:             ', self._stats['attribute']['max'])
        print('  Avg ± Std:        %.4f ± %.4f' % (
            self._stats['attribute']['avg'], self._stats['attribute']['std']))

        print('\nPOINT')
        print('  Count:           ', self._stats['point']['count'])

        print('\nTRAJECTORY')
        print('  Count:           ', self._stats['trajectory']['count'])
        print('  Min length:      ',
              self._stats['trajectory']['length']['min'])
        print('  Max lenght:      ',
              self._stats['trajectory']['length']['max'])
        print('  Avg length ± Std: %.4f ± %.4f' %
              (self._stats['trajectory']['length']['avg'],
               self._stats['trajectory']['length']['std']))

        if self.labels is not None:
            print('\nLABEL')
            print('  Count:           ', self._stats['label']['count'])
            print('  Min:             ', self._stats['label']['min'])
            print('  Max:             ', self._stats['label']['max'])
            print('  Avg ± Std:        %.4f ± %.4f' % (
                self._stats['label']['avg'], self._stats['label']['std']))
            print('==========================================================')
        else:
            print('==========================================================')
