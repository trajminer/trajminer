from os import path
import tempfile
import tarfile

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
    tar_file = path.join(_get_data_dir(), 'starkey_telemetry',
                         'starkey_animals.tar.xz')
    csv_file = _extract_tar(tar_file)
    loader = CSVTrajectoryLoader(file=csv_file, sep=',', tid_col='tid',
                                 label_col='species', lat='lat', lon='lon',
                                 n_jobs=n_jobs)
    return loader.load()


def _extract_tar(file):
    tmp = tempfile.mkdtemp()
    tar_file = tarfile.open(file, 'r')
    tar_file.extractall(tmp)
    extracted = path.join(tmp, tar_file.getnames()[0])
    tar_file.close()
    return extracted


def _get_data_dir():
    return path.join(path.dirname(__file__), 'data')
