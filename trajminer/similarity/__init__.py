"""Trajectory similarity measures.
"""
from .classes import EDR, LCSS, MSM
from .pairwise import pairwise_similarity

__all__ = ['EDR',
           'LCSS',
           'MSM',
           'pairwise_similarity']
