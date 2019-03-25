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
        pass

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
        pass
