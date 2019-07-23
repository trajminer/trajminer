"""This module contains utilities for loading well-known trajectory datasets.
"""
from .base import load_brightkite_checkins
from .base import load_gowalla_checkins
from .base import load_foursquare_checkins
from .base import load_starkey_animals

__all__ = ['load_brightkite_checkins',
           'load_gowalla_checkins',
           'load_foursquare_checkins',
           'load_starkey_animals']
