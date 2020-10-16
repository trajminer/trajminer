from .tools import download_file
from .tools import extract_tar
from .tools import get_file_url
from ..utils.loader import CSVTrajectoryLoader


def load_brightkite_checkins(n_jobs=1, cache=True, verbose=False):
    """Loads the Brightkite location-based social network data.

    =================   ==============
    Classes                     58,228
    Trajectories                58,228
    Points                   4,491,143
    Features                         4
    =================   ==============

    Parameters
    ----------
    n_jobs : int (default=1)
        The number of parallel jobs.
    cache : bool (default=True)
        If `False`, then always downloads the data. Otherwise, checks if the
        data was previously downloaded.
    verbose : bool (default=False)
        If `True`, then logs the actions for loading the data.

    Returns
    -------
    data : :class:`trajminer.TrajectoryData`
        The loaded dataset.

    References
    ----------
    `https://snap.stanford.edu/data/loc-brightkite.html
    <https://snap.stanford.edu/data/loc-brightkite.html>`__
    """
    log = lambda *x: print(*x) if verbose else True
    csv_file = _get_csv('brightkite', 'checkins.tar.xz', cache, verbose)

    log('Loading dataset from', csv_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='user',
                                 label_col='user', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def load_gowalla_checkins(n_jobs=1, cache=True, verbose=False):
    """Loads the Gowalla location-based social network data.

    =================   ==============
    Classes                    196,591
    Trajectories               196,591
    Points                   6,442,890
    Features                         4
    =================   ==============

    Parameters
    ----------
    n_jobs : int (default=1)
        The number of parallel jobs.
    cache : bool (default=True)
        If `False`, then always downloads the data. Otherwise, checks if the
        data was previously downloaded.
    verbose : bool (default=False)
        If `True`, then logs the actions for loading the data.

    Returns
    -------
    data : :class:`trajminer.TrajectoryData`
        The loaded dataset.

    References
    ----------
    `https://snap.stanford.edu/data/loc-gowalla.html
    <https://snap.stanford.edu/data/loc-gowalla.html>`__
    """
    log = lambda *x: print(*x) if verbose else True
    csv_file = _get_csv('gowalla', 'checkins.tar.xz', cache, verbose)

    log('Loading dataset from', csv_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='user',
                                 label_col='user', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def load_foursquare_checkins(location, n_jobs=1, cache=True, verbose=False):
    """Loads the Foursquare location-based social network data.

    NYC
    =================   ==============
    Classes                      1,083
    Trajectories                 1,083
    Points                     227,428
    Features                         6
    =================   ==============

    TKY
    =================   ==============
    Classes                      2,293
    Trajectories                 2,293
    Points                     573,703
    Features                         6
    =================   ==============

    Parameters
    ----------
    location : 'nyc', or 'tky'
        If `nyc`, then loads New York City's check-ins data. If `tky`, then
        loads Tokyo's.
    n_jobs : int (default=1)
        The number of parallel jobs.
    cache : bool (default=True)
        If `False`, then always downloads the data. Otherwise, checks if the
        data was previously downloaded.
    verbose : bool (default=False)
        If `True`, then logs the actions for loading the data.

    Returns
    -------
    data : :class:`trajminer.TrajectoryData`
        The loaded dataset.

    References
    ----------
    `https://sites.google.com/site/yangdingqi/home/foursquare-dataset
    <https://sites.google.com/site/yangdingqi/home/foursquare-dataset>`__
    """

    if location not in ('nyc', 'tky'):
        raise ValueError("'%s' is not a supported location" % location)

    log = lambda *x: print(*x) if verbose else True

    if location == 'nyc':
        csv_file = _get_csv(
            'foursquare',
            'checkins_nyc.tar.xz',
            cache,
            verbose)
    elif location == 'tky':
        csv_file = _get_csv(
            'foursquare',
            'checkins_tky.tar.xz',
            cache,
            verbose)

    log('Loading dataset from', csv_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='user',
                                 label_col='user', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def load_starkey_animals(n_jobs=1, cache=True, verbose=False):
    """Loads the Starkey Project telemetry data.

    =================   ==============
    Classes                          3
    Trajectories                   253
    Points                     287,136
    Features                         6
    =================   ==============

    Parameters
    ----------
    n_jobs : int (default=1)
        The number of parallel jobs.
    cache : bool (default=True)
        If `False`, then always downloads the data. Otherwise, checks if the
        data was previously downloaded.
    verbose : bool (default=False)
        If `True`, then logs the actions for loading the data.

    Returns
    -------
    data : :class:`trajminer.TrajectoryData`
        The loaded dataset.

    References
    ----------
    `https://www.fs.fed.us/pnw/starkey/mapsdata.shtml
    <https://www.fs.fed.us/pnw/starkey/mapsdata.shtml>`__
    """
    log = lambda *x: print(*x) if verbose else True
    csv_file = _get_csv('starkey', 'starkey.tar.xz', cache, verbose)

    log('Loading dataset from', csv_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='tid',
                                 label_col='species', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def _get_csv(folder, file, cache, verbose=False):
    log = lambda *x: print(*x) if verbose else True

    log('Downloading file', file)
    tar_file = download_file(get_file_url(folder, file), file, cache)
    log('Extracting content of', tar_file)
    return extract_tar(tar_file)
