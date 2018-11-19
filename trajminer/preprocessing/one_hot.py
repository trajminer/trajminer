class OneHotEncoder(object):
    """Encode trajectory features as the concatenation of the one-hot numeric
    array for each feature.
    """

    def __init__(self):
        pass

    def fit(self, X):
        """Fit OneHotEncoder to X.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data for setting up the encoder.
        """
        pass

    def fit_transform(self, X):
        """Fit OneHotEncoder to X, then transform X.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data to encode.

        Returns
        -------
        X_out : array-like
            Transformed input.
        """
        pass

    def transform(self, X):
        """Transform X.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data to encode.

        Returns
        -------
        X_out : array-like
            Transformed input.
        """
        pass

    def inverse_transform(self, X):
        """Convert X back to its original representation.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, ?)
            Input data to decode.

        Returns
        -------
        X_out : array-like, shape (n_samples, max_length, n_features)
            Original data.
        """
        pass
