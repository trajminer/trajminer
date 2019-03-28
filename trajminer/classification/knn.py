from sklearn.neighbors import KNeighborsClassifier
import numpy as np

from .base import Classifier
from ..similarity.pairwise import pairwise_similarity


class KNearestNeighbors(Classifier):
    """K-Nearest Neighbors Classifier.

    Parameters
    ----------
    n_neighbors : int (default=1)
        Number of neighbors to use for queries.
    weights : str or callable (default='uniform')
        Weight function used in prediction. See the scikit-learn API fo
        details.
    measure : SimilarityMeasure object or str (default='precomputed')
        The similarity measure to use for computing similarities (see
        :mod:`trajminer.similarity`) or the string 'precomputed'.
    n_jobs : int (default=1)
        The number of parallel jobs.
    """

    def __init__(self, n_neighbors=1, weights='uniform',
                 measure='precomputed', n_jobs=1):
        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors,
                                        weights=weights,
                                        metric='precomputed', n_jobs=n_jobs)
        self.n_neighbors = n_neighbors
        self.weights = weights
        self.measure = measure
        self.n_jobs = n_jobs

    def fit(self, X, y):
        if self.measure != 'precomputed':
            self.distances = 1 - pairwise_similarity(X=X, measure=self.measure,
                                                     n_jobs=self.n_jobs)
        else:
            self.distances = np.array(X)

        self.knn.fit(self.distances, y)

    def predict(self, X):
        return self.knn.predict(X)

    def score(self, X, y):
        return self.knn.score(X, y)
