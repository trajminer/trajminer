"""Trajectory classifiers. Implementations of traditional classification
algorithms work alongside with a trajectory similarity measure from
:mod:`trajminer.similarity`.
"""
from .knn import KNearestNeighbors
from .movelets import Movelets
from .traclass import TraClass

__all__ = ['KNearestNeighbors',
           'Movelets',
           'TraClass']
