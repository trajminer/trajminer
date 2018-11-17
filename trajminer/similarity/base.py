class SimilarityMeasure(object):
    """Base class for all trajectory similarity measures.
    """

    def similarity(self, t1, t2):
        """Computes the similarity score of the given trajectories.

        Parameters
        ----------
        t1 : array-like, shape (n_points, n_features)
            Input trajectory.
        t2 : array-like, shape (n_points, n_features)
            Input trajectory.

        Returns
        -------
        score : float
            Similarity score (between 0 and 1).
        """
        pass
