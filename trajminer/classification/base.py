class Classifier(object):
    """Base class for all classifiers."""

    def fit(self, X, y):
        pass

    def predict(self, X):
        """Returns the predictions for the given test data.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data.

        Returns
        -------
        predictions : array-like, shape (n_samples, n_labels)
            Predicted class for each input sample.
        """
        pass

    def score(self, X, y):
        """Returns the accuracy on the given test data and labels.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data.
        y : array-like, shape (n_samples, n_labels)
            Labels of input samples.

        Returns
        -------
        score : float
            Accuracy of self.predict(X) according to y.
        """
        pass
