class Clustering(object):
    """Base class for all clustering algorithms."""

    def fit_predict(self, X):
        """Fits and returns the predictions for the given test data.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data.

        Returns
        -------
        predictions : array-like, shape (n_samples, 1)
            Assigned cluster for each input sample.
        """
        pass
