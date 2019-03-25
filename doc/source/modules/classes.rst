.. _api_ref:

=============
API Reference
=============

This is the main reference for classes and functions present in **trajminer**.

:mod:`trajminer`: Base
================================================

.. automodule:: trajminer
   :no-members:
   :no-inherited-members:

Classes
-------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: class.rst

   trajminer.TrajectoryData


:mod:`trajminer.classification`: Classification
================================================

.. automodule:: trajminer.classification
   :no-members:
   :no-inherited-members:

Classes
-------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: class.rst

   classification.KNearestNeighbors
   classification.RNNClassifier
   classification.TraClass


:mod:`trajminer.clustering`: Clustering
================================================

.. automodule:: trajminer.clustering
   :no-members:
   :no-inherited-members:

Classes
-------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: class.rst

   clustering.AgglomerativeClustering
   clustering.DBSCAN
   clustering.KMedoids


:mod:`trajminer.similarity`: Similarity
================================================

.. automodule:: trajminer.similarity
   :no-members:
   :no-inherited-members:

Classes
-------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: class.rst

   similarity.EDR
   similarity.LCSS
   similarity.MSM

Functions
---------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: function.rst

   similarity.pairwise_similarity


:mod:`trajminer.utils`: Utils
================================================

.. automodule:: trajminer.utils
   :no-members:
   :no-inherited-members:

Classes
-------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: class.rst

   utils.CSVTrajectoryLoader

   utils.distance.discrete
   utils.distance.euclidean
   utils.distance.haversine


:mod:`trajminer.preprocessing`: Preprocessing
================================================

.. automodule:: trajminer.preprocessing
   :no-members:
   :no-inherited-members:

Classes
-------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: class.rst

   preprocessing.OneHotEncoder
   preprocessing.TrajectorySegmenter
