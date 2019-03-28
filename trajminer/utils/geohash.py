import numpy as np
import geohash2 as gh


class Geohash(object):
    """Utility for encoding latitute and longitude coordinates using Geohash.

    References
    ----------
    `Niemeyer, G. (2008). Geohash. <https://en.wikipedia.org/wiki/Geohash>`__

    Examples
    --------
    >>> from trajminer.utils import Geohash
    >>> g = Geohash()
    >>> g.encode(lat=-27.601759, lon=-48.520894)
    '6gj6zzk0j5'
    >>> g.encode(lat=-27.601759, lon=-48.520894, binary=True)
    array([0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
           1, 0, 0, 1, 0, 1])
    >>> g.encode(lat=-27.601759, lon=-48.520894, precision=15)
    '6gj6zzk0j5pnhu8'
    """

    def __init__(self):
        self.base32 = ['0', '1', '2', '3', '4', '5', '6', '7',
                       '8', '9', 'b', 'c', 'd', 'e', 'f', 'g',
                       'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r',
                       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.binary = [np.asarray(list('{0:05b}'.format(x, 'b')), dtype=int)
                       for x in range(0, len(self.base32))]
        self.base32toBin = dict(zip(self.base32, self.binary))

    def encode(self, lat, lon, precision=10, binary=False):
        """Encodes a lat/lon pair with Geohash.

        Parameters
        ----------
        lat : float
            The latitude.
        long : float
            The longitude.
        precision : int (default=10)
            The length of the encoded location in Base32.
        binary : bool (default=False)
            If `True`, computes the binary codification of the Base32 geohash.

        Returns
        -------
        geohash : str or array-like
            The Base32 geohash or a binary array-like representation if
            `binary=True`.
        """
        hashed = gh.encode(lat, lon, precision)

        if binary:
            return np.concatenate([self.base32toBin[x] for x in hashed])

        return hashed
