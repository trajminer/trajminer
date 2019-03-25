import numpy as np


def discrete(x, y):
    """Computes the discrete distance between two objects.

    Parameters
    ----------
    x : object
        Any object.
    y : object
        Any object.

    Returns
    -------
    distance : float
        Returns ``0.0`` if ``x == y``, ``1.0`` otherwise.
    """
    return 0.0 if x == y else 1.0


def euclidean(x, y):
    """Computes the euclidean distance between two objects described by an
    array of floats.

    Parameters
    ----------
    x : float or array-like
        A float or an array-like object of floats.
    y : float array-like
        A float or an array-like object of floats.

    Returns
    -------
    distance : float
        The euclidean distance between ``x`` and ``y``.
    """
    return np.sqrt(np.sum(np.square(np.array(x) - np.array(y))))


def haversine(x, y, unit='meters'):
    """Computes the haversine distance between two pairs of latitude and
    longitude.

    Parameters
    ----------
    x : array-like, shape (2)
        An array like ``[lat, lon]``. ``lat`` and ``lon`` must be floats.
    y : array-like, shape (2)
        An array like ``[lat, lon]``. ``lat`` and ``lon`` must be floats.
    unit : str (default='meters')
        The unit to use for measuring the distance. It must be one of
        {'meters', 'km', 'mi'}.

    Returns
    -------
    distance : float
        The haversine distance between ``x`` and ``y`` in the specified unit.
    """
    lon1, lat1, lon2, lat2 = np.radians([x[1], x[0], y[1], y[0]])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371000  # Radius of earth in meters

    if unit == 'km':
        return c * r / 1000
    elif unit == 'mi':
        return c * r / 1609.34

    return c * r
