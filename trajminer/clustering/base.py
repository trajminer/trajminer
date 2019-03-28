class Clustering(object):
    """Base class for all clustering algorithms."""

    def fit_predict(self, X):
        """Fits and returns the predictions for the given test data.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data. If measure == 'precomputed', then X is a distance
            matrix with shape (n_samples, n_samples).

        Returns
        -------
        predictions : array-like, shape (n_samples)
            Assigned cluster for each input sample.
        """
        pass
