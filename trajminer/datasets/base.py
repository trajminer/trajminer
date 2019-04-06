from .tools import _download_file
from .tools import _extract_tar
from .tools import _get_file_url
from ..utils.loader import CSVTrajectoryLoader


def load_brightkite_checkins(n_jobs=1, verbose=False):
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
    verbose : bool (default=False)
        If `True`, logs the actions for loading the data.

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
    csv_file = _get_csv('gowalla', 'checkins.tar.xz', verbose)

    log('Loading dataset from', csv_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='user',
                                 label_col='user', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def load_gowalla_checkins(n_jobs=1, verbose=False):
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
    verbose : bool (default=False)
        If `True`, logs the actions for loading the data.

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
    csv_file = _get_csv('gowalla', 'checkins.tar.xz', verbose)

    log('Loading dataset from', csv_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='user',
                                 label_col='user', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def load_starkey_animals(n_jobs=1, verbose=False):
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
    verbose : bool (default=False)
        If `True`, logs the actions for loading the data.

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
    csv_file = _get_csv('starkey', 'starkey.tar.xz', verbose)

    log('Loading dataset from', csv_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='tid',
                                 label_col='species', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def _get_csv(folder, file, verbose=False):
    log = lambda *x: print(*x) if verbose else True

    log('Downloading file', file)
    tar_file = _download_file(_get_file_url(folder, file))
    log('Extracting content of', tar_file)
    return _extract_tar(tar_file)
