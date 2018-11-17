def pairwise_similarity(X, Y=None, measure=None, n_jobs=1):
    """Compute the similarity between trajectories in X and Y.

    Parameters
    ----------
    X : array-like, shape: (n_trajectories_X, n_points, n_features)
        Input data.
    Y : array-like, shape: (n_trajectories_Y, n_points, n_features)
        Input data. If ``None``, the output will be the pairwise
        similarities between all samples in ``X``.
    measure : SimilarityMeasure object (default=None)
        The similarity measure to use for computing similarities. See
        :mod:`trajminer.similarity`.
    n_jobs : int (default=1)
        The number of parallel jobs.

    Returns
    -------
    similarities : array
        An array with shape (n_trajectories_X, n_trajectories_Y).
    """
    import numpy as np
    from joblib import Parallel, delayed
    from sklearn.utils import gen_even_slices

    def compute_slice(X, Y, slice, upper=False):
        matrix = np.zeros(shape=(len(X), len(Y)))

        for i in range(slice.start + 1, len(X)):
            for j in range(0, min(len(Y), i - slice.start)):
                matrix[i][j] = measure.similarity(X[i], Y[j])
        return matrix

    upper = Y is not None
    Y = X if not Y else Y
    func = delayed(compute_slice)

    similarity = Parallel(n_jobs=n_jobs, verbose=0)(
        func(X, Y[s], s, upper) for s in gen_even_slices(len(Y), n_jobs))
    similarity = np.hstack(similarity)

    if not upper:
        similarity += np.transpose(similarity) + np.identity(len(X))

    return similarity
