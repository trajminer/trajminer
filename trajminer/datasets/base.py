from os import path
import tempfile
import zipfile

from ..utils.loader import CSVTrajectoryLoader


def load_starkey_animals(n_jobs=1):
    """Loads the Starkey Project telemetry data.

    =================   ==============
    Classes                          3
    Trajectories                   253
    Features                         6
    =================   ==============

    Parameters
    ----------
    n_jobs : int (default=1)
        The number of parallel jobs.

    Returns
    -------
    data : :class:`trajminer.TrajectoryData`
        The loaded dataset.

    References
    ----------
    `https://www.fs.fed.us/pnw/starkey/mapsdata.shtml
    <https://www.fs.fed.us/pnw/starkey/mapsdata.shtml>`__
    """
    zip_file = path.join(_get_data_dir(), 'starkey_telemetry',
                         'starkey_animals.zip')
    csv_file = _extract_zip(zip_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='tid',
                                 label_col='species', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def _extract_zip(file):
    tmp = tempfile.mkdtemp()
    zip_file = zipfile.ZipFile(file, 'r')
    zip_file.extractall(tmp)
    zip_file.close()
    return path.join(tmp, zip_file.namelist()[0])


def _get_data_dir():
    return path.join(path.dirname(__file__), 'data')
