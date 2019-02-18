from .base import Clustering


class DBSCAN(Clustering):
    """DBSCAN Clustering.

    Parameters
    ----------
    eps : float (default=0.5)
        The maximum distance between two trajectories for them to be
        considered in the same neighborhood.
    min_samples : int (default=5)
        The minibum number of trajectories in a neighborhood for a trajectory
        to be considered as a core point, including the trajectory itself.
    measure : SimilarityMeasure object (default=None)
        The similarity measure to use for computing similarities. See
        :mod:`trajminer.similarity`.
    n_jobs : int (default=1)
        The number of parallel jobs.

    References
    ----------
    `Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996, August). A density-
     based algorithm for discovering clusters in large spatial databases with
     noise. In Kdd (Vol. 96, No. 34, pp. 226-231).
     <https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf>`
    """

    def __init__(self, eps=0.5, min_samples=5, measure=None, n_jobs=1):
        from sklearn.cluster import DBSCAN

        self.dbscan = DBSCAN(eps=eps, min_samples=min_samples,
                             metric='precomputed', n_jobs=n_jobs)
        self.eps = eps
        self.min_samples = min_samples
        self.measure = measure
        self.n_jobs = n_jobs

    def fit_predict(self, X):
        from ..similarity.pairwise import pairwise_similarity

        self.distances = 1 - pairwise_similarity(X=X, measure=self.measure,
                                                 n_jobs=self.n_jobs)
        self.labels = self.dbscan.fit_predict(self.distances)
        return self.labels
