from .base import SimilarityMeasure


class EDR(SimilarityMeasure):
    """Edit Distance on Real sequence.

    Parameters
    ----------
    dist_functions : array-like, shape (n_features)
        Specifies the distance functions used for each trajectory
        attribute.
    thresholds : array-like, shape (n_features)
        Specifies the thresholds used for each trajectory attribute.

    References
    ----------
    `Chen, L., Özsu, M. T., & Oria, V. (2005, June). Robust and fast
    similarity search for moving object trajectories. In Proceedings
    of the 2005 ACM SIGMOD international conference on Management of
    data (pp. 491-502). ACM. <https://dl.acm.org/citation.cfm?id=1066213>`__
    """

    def __init__(self, dist_functions, thresholds):
        self.dist_functions = dist_functions
        self.thresholds = thresholds

    def similarity(self, t1, t2):
        import numpy as np
        matrix = np.zeros(shape=(len(t1) + 1, len(t2) + 1))
        matrix[:, 0] = np.r_[0:len(t1)+1]
        matrix[0] = np.r_[0:len(t2)+1]

        for i, p1 in enumerate(t1):
            for j, p2 in enumerate(t2):
                cost = self._match_cost(p1, p2)
                matrix[i+1][j+1] = min(matrix[i][j] + cost,
                                       min(matrix[i+1][j] + 1,
                                           matrix[i][j+1] + 1))

        return 1 - matrix[len(t1)][len(t2)] / max(len(t1), len(t2))

    def _match_cost(self, p1, p2):
        for i, _ in enumerate(p1):
            d = self.dist_functions[i](p1[i], p2[i])
            if d > self.thresholds[i]:
                break
        else:
            return 0
        return 1


class LCSS(SimilarityMeasure):
    """Longest Common SubSequence.

    Parameters
    ----------
    dist_functions : array-like, shape (n_features)
        Specifies the distance functions used for each trajectory
        attribute.
    thresholds : array-like, shape (n_features)
        Specifies the thresholds used for each trajectory attribute.

    References
    ----------
    `Vlachos, M., Kollios, G., & Gunopulos, D. (2002). Discovering similar
    multidimensional trajectories. In Data Engineering, 2002. Proceedings.
    18th International Conference on (pp. 673-684). IEEE.
    <https://ieeexplore.ieee.org/abstract/document/994784/>`__
    """

    def __init__(self, dist_functions, thresholds):
        self.dist_functions = dist_functions
        self.thresholds = thresholds

    def similarity(self, t1, t2):
        import numpy as np
        matrix = np.zeros(shape=(len(t1) + 1, len(t2) + 1))

        for i, p1 in enumerate(t1):
            for j, p2 in enumerate(t2):
                if self._match(p1, p2):
                    matrix[i+1][j+1] = matrix[i][j] + 1
                else:
                    matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])

        return matrix[len(t1)][len(t2)] / min(len(t1), len(t2))

    def _match(self, p1, p2):
        for i, _ in enumerate(p1):
            d = self.dist_functions[i](p1[i], p2[i])
            if d > self.thresholds[i]:
                break
        else:
            return True
        return False


class MSM(SimilarityMeasure):
    """Multidimensional Similarity Measure.

    Parameters
    ----------
    dist_functions : array-like, shape (n_features)
        Specifies the distance functions used for each trajectory
        attribute.
    thresholds : array-like, shape (n_features)
        Specifies the thresholds used for each trajectory attribute.
    weights : array-like, shape (n_features)
        Specifies the weight (importance) of each trajectory attribute.

    References
    ----------
    `Furtado, A. S., Kopanaki, D., Alvares, L. O., & Bogorny, V. (2016).
    Multidimensional similarity measuring for semantic trajectories.
    Transactions in GIS, 20(2), 280-298.
    <https://onlinelibrary.wiley.com/doi/abs/10.1111/tgis.12156>`__
    """

    def __init__(self, dist_functions, thresholds, weights):
        self.dist_functions = dist_functions
        self.thresholds = thresholds
        self.weights = weights

    def similarity(self, t1, t2):
        import numpy as np
        matrix = np.zeros(shape=(len(t1), len(t2)))

        for i, p1 in enumerate(t1):
            for j, p2 in enumerate(t2):
                matrix[i][j] = self._score(p1, p2)

        parity1 = np.sum(np.amax(matrix, axis=1))
        parity2 = np.sum(np.amax(np.transpose(matrix), axis=1))
        return (parity1 + parity2) / (len(t1) + len(t2))

    def _score(self, p1, p2):
        import numpy as np
        matches = np.zeros(len(p1))
        for i, _ in enumerate(p1):
            matches[i] = self.dist_functions[i](p1[i], p2[i]) <= \
                self.thresholds[i]
        return np.sum(matches * self.weights)
