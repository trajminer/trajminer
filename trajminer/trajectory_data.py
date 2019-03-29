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
        self.tids = tids
        self.labels = labels
        self.data = np.array(data)
        self._stats = None
        self.tidToIdx = dict(zip(tids, np.r_[0:len(tids)]))

        if self.labels is not None:
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

        if self.labels:
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

        if self.labels:
            print('\nLABEL')
            print('  Count:           ', self._stats['label']['count'])
            print('  Min:             ', self._stats['label']['min'])
            print('  Max:             ', self._stats['label']['max'])
            print('  Avg ± Std:        %.4f ± %.4f' % (
                self._stats['label']['avg'], self._stats['label']['std']))
            print('==========================================================')
        else:
            print('==========================================================')
