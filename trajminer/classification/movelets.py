import sys
import numpy as np

from .base import Classifier


class Movelets(Classifier):
    """MOVELETS: exploring relevant subtrajectories for robust trajectory
    classification.

    Parameters
    ----------
    dist_functions : array-like, shape (n_features)
        Specifies the distance functions used for each trajectory
        attribute.
    norm_distances : array-like, shape (n_features) (default=[])
        Specifies the maximum values to use for distance normalization. For
        the i-th feature, if norm_distances[i] <= 0, then the distance is not
        normalized.

    References
    ----------
    `Ferrero, C. A., Alvares, L. O., Zalewski, W., & Bogorny, V. (2018,
    April). MOVELETS: exploring relevant subtrajectories for robust trajectory
    classification. In Proceedings of the 33rd Annual ACM Symposium on Applied
    Computing (pp. 849-856). ACM.
    <https://dl.acm.org/citation.cfm?doid=3167132.3167225>`__
    """

    def __init__(self, dist_functions, norm_distances=[]):
        self.distances = dist_functions

        if len(norm_distances) > 0:
            for i in range(0, len(dist_functions)):
                if norm_distances[i] > 0:
                    self.distances[i] = \
                        lambda x, y: self.distances[i] / norm_distances[i]

    def fit(self, X, y):
        for i, traj in enumerate(X):
            break

        pass

    def predict(self, X):
        pass

    def score(self, X, y):
        pass

    def _best_alignment(self, subtraj, traj):
        if len(subtraj) > len(traj):
            return sys.float_info.max

        comp = len(traj) - len(subtraj)
        minDist = sys.float_info.max
        position = -1

        for i in range(0, comp + 1):
            curDist = 0
            for j in range(0, len(subtraj)):
                pointDist = 0

                for dist in self.distances:
                    pointDist += dist(subtraj[j], traj[i + j])
                curDist += pointDist * pointDist

            if curDist < minDist:
                minDist = curDist
                position = i

        minDist = np.sqrt(minDist / len(subtraj))
        position = [position, position + len(subtraj)]
        return minDist, position
