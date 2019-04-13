from os import path
from urllib import request
import tarfile
import tempfile
import glob

_trajminer_data_dir = None


def get_file_url(folder, file):
    url = 'https://github.com/trajminer/data/blob/master/' + \
          '{}/{}?raw=true'
    return url.format(folder, file)


def download_file(url, file_name, cache=True):
    _create_temp_dir()
    file_path = path.join(_trajminer_data_dir, file_name)

    if not cache or not path.isfile(file_path):
        request.urlretrieve(url, file_path)

    return file_path


def extract_tar(file):
    _create_temp_dir()
    tar_file = tarfile.open(file, 'r')
    tar_file.extractall(_trajminer_data_dir)
    extracted = path.join(_trajminer_data_dir, tar_file.getnames()[0])
    tar_file.close()
    return extracted


def _create_temp_dir():
    global _trajminer_data_dir

    if _trajminer_data_dir is None:
        dirs = glob.glob(path.join(tempfile.gettempdir(), 'trajminer_data_*'))

        if len(dirs) > 0:
            _trajminer_data_dir = dirs[0]
        else:
            _trajminer_data_dir = tempfile.mkdtemp(prefix='trajminer_data_')
