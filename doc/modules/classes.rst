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
   similarity.MUITAS

Functions
---------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: function.rst

   similarity.pairwise_similarity


:mod:`trajminer.datasets`: Datasets
================================================

.. automodule:: trajminer.datasets
   :no-members:
   :no-inherited-members:

Functions
---------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: function.rst

   datasets.load_starkey_animals


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

Functions
---------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: function.rst

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

   preprocessing.TrajectorySegmenter

Functions
---------
.. currentmodule:: trajminer

.. autosummary::
   :toctree: generated/
   :template: function.rst

   preprocessing.filter_trajectory_length
   preprocessing.filter_label_size
   preprocessing.filter_duplicate_points
