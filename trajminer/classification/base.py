class Classifier(object):
    """Base class for all classifiers."""

    def fit(self, X, y):
        pass

    def predict(self, X):
        pass

    def score(self, X, y):
        """Returns the accuracy on the given test data and labels.

        Parameters
        ----------
        TO-DO

        Returns
        -------
        score : float
            Accuracy of self.predict(X) according to y.
        """
        pass
