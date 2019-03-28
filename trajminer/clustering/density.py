from sklearn.cluster import DBSCAN as skDBSCAN
import numpy as np

from .base import Clustering
from ..similarity.pairwise import pairwise_similarity


class DBSCAN(Clustering):
    """DBSCAN Clustering.

    Parameters
    ----------
    eps : float (default=0.5)
        The maximum distance between two trajectories for them to be
        considered in the same neighborhood.
    min_samples : int (default=5)
        The minimum number of trajectories in a neighborhood for a trajectory
        to be considered as a core point, including the trajectory itself.
    measure : SimilarityMeasure object or str (default='precomputed')
        The similarity measure to use for computing similarities (see
        :mod:`trajminer.similarity`) or the string 'precomputed'.
    n_jobs : int (default=1)
        The number of parallel jobs.

    References
    ----------
    `Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996, August). A density-
    based algorithm for discovering clusters in large spatial databases with
    noise. In Kdd (Vol. 96, No. 34, pp. 226-231).
    <https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf>`__
    """

    def __init__(self, eps=0.5, min_samples=5, measure='precomputed',
                 n_jobs=1):
        self.dbscan = skDBSCAN(eps=eps, min_samples=min_samples,
                               metric='precomputed', n_jobs=n_jobs)
        self.eps = eps
        self.min_samples = min_samples
        self.measure = measure
        self.n_jobs = n_jobs

    def fit_predict(self, X):
        if self.measure != 'precomputed':
            self.distances = 1 - pairwise_similarity(X=X, measure=self.measure,
                                                     n_jobs=self.n_jobs)
        else:
            self.distances = np.array(X)

        self.labels = self.dbscan.fit_predict(self.distances)
        return self.labels
