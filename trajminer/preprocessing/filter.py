def filter_trajectory_length(data, min_length, max_length, inplace=True,
                             n_jobs=1):
    """Removes trajectories by length criteria.

    Parameters
    ----------
    data : :class:`trajminer.TrajectoryData`
        The dataset to be filtered.
    min_length : int
        The minimum length required to keep trajectories in the dataset. If
        `None`, then no minimum length is enforced.
    max_length : int
        The maximum length required to keep trajectories in the dataset. If
        `None`, then no maximum length is enforced.
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


def filter_label_size(data, min_size, max_size, inplace=True, n_jobs=1):
    """Removes trajectories corresponding to sets of labels that do not meet
    size criteria.

    Parameters
    ----------
    data : :class:`trajminer.TrajectoryData`
        The dataset to be filtered.
    min_size : int
        The minimum number of trajectories required of a certain label to keep
        it in the dataset. If `None`, then no minimum size is enforced.
    max_size : int
        The maximum number of trajectories required of a certain label to keep
        it in the dataset. If `None`, then no maximum size is enforced.
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
