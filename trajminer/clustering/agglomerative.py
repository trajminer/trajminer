from .base import Clustering


class AgglomerativeClustering(Clustering):
    """Hierarchical Agglomerative Clustering.

    Parameters
    ----------
    n_clusters : int
        The number of clusters to group trajectories into.
    linkage : str (default='ward')
        The linkage method to use. Must be one of {'ward', complete',
        'average'}.
    measure : SimilarityMeasure object or str (default='precomputed')
        The similarity measure to use for computing similarities (see
        :mod:`trajminer.similarity`) or the string 'precomputed'.
    n_jobs : int (default=1)
        The number of parallel jobs.
    """

    def __init__(self, n_clusters, linkage='ward', measure='precomputed',
                 n_jobs=1):
        from sklearn.cluster import AgglomerativeClustering
        self.agglomerative = AgglomerativeClustering(n_clusters=n_clusters,
                                                     affinity='precomputed')
        self.n_clusters = n_clusters
        self.measure = measure
        self.n_jobs = n_jobs

    def fit_predict(self, X):
        import numpy as np

        if self.measure != 'precomputed':
            from ..similarity.pairwise import pairwise_similarity

            self.distances = 1 - pairwise_similarity(X=X, measure=self.measure,
                                                     n_jobs=self.n_jobs)
        else:
            self.distances = np.array(X)

        self.labels = self.agglomerative.fit_predict(self.distances)
        return self.labels
