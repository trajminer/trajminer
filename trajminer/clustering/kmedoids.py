import random
import numpy as np

from .base import Clustering
from ..similarity.pairwise import pairwise_similarity


class KMedoids(Clustering):
    """K-Medoids Clustering.

    Parameters
    ----------
    n_clusters : int
        The number of clusters to group trajectories into.
    init : 'park' or array-like (default=None)
        The indices of the trajectories representing the initial cluster
        medoids. If 'park', the medoids will be initialized using the
        approach introduced in [Park et al., 2009] (see references). If
        ``None``, the initial medoids will be chosen randomly.
    seed : int (default=None)
        The random seed to be used for centroid initialization. If ``None``,
        the default seed of NumPy will be used.
    max_iter : int (default=300)
        The maximum number of iterations to run the algorithm, in case it has
        not yet converged.
    measure : SimilarityMeasure object or str (default='precomputed')
        The similarity measure to use for computing similarities (see
        :mod:`trajminer.similarity`) or the string 'precomputed'.
    n_jobs : int (default=1)
        The number of parallel jobs.

    References
    ----------
    `Park, H. S., & Jun, C. H. (2009). A simple and fast algorithm for
    K-medoids clustering. Expert systems with applications, 36(2), 3336-3341.
    <https://www.sciencedirect.com/science/article/pii/S095741740800081X>`__
    """

    def __init__(self, n_clusters, init=None, seed=None, max_iter=300,
                 measure='precomputed', n_jobs=1):
        self.n_clusters = n_clusters
        self.init = init
        self.seed = seed
        self.max_iter = max_iter
        self.measure = measure
        self.n_jobs = n_jobs

    def fit_predict(self, X):
        if self.measure != 'precomputed':
            self.distances = 1 - pairwise_similarity(X=X, measure=self.measure,
                                                     n_jobs=self.n_jobs)
        else:
            self.distances = np.array(X)

        if not self.init:
            if self.seed is not None:
                random.seed(self.seed)

            idxs = np.r_[0:len(self.distances)]
            random.shuffle(idxs)
            self.medoids = idxs[:self.n_clusters]
        elif self.init == 'park':
            scores = np.zeros(len(self.distances))

            for j in range(0, len(self.distances)):
                scores[j] = 0
                for i in range(0, len(self.distances)):
                    scores[j] += self.distances[i][j] / \
                        np.sum(self.distances[i])

            self.medoids = np.argsort(scores)[0:self.n_clusters]
        else:
            self.medoids = self.init

        self.medoids = np.sort(self.medoids).astype(int)
        clusters = {}

        for self.iter in range(1, self.max_iter + 1):
            new_medoids = np.zeros(self.n_clusters)

            d = np.argmin(self.distances[:, self.medoids], axis=1)
            clusters = dict(zip(np.r_[0:self.n_clusters],
                                [np.where(d == k)[0]
                                 for k in range(self.n_clusters)]))

            for k in range(self.n_clusters):
                d = np.mean(self.distances[np.ix_(clusters[k],
                                                  clusters[k])],
                            axis=1)
                j = np.argmin(d)
                new_medoids[k] = clusters[k][j]

            new_medoids = np.sort(new_medoids).astype(int)

            if np.array_equal(self.medoids, new_medoids):
                break

            self.medoids = np.copy(new_medoids)
        else:
            d = np.argmin(self.distances[:, self.medoids], axis=1)
            clusters = dict(zip(np.r_[0:self.n_clusters],
                                [np.where(d == k)[0]
                                 for k in range(self.n_clusters)]))

        self.labels = np.zeros(len(self.distances))

        for key in clusters:
            self.labels[clusters[key]] = key + 1

        self.labels = self.labels.astype(int)
        return self.labels
