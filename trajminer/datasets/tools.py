from os import path
from urllib import request
import tarfile
import tempfile


def _get_file_url(folder, file):
    url = 'https://github.com/trajminer/data/blob/master/' + \
          '{}/{}?raw=true'
    return url.format(folder, file)


def _download_file(url, file_path=None):
    file, _ = request.urlretrieve(url, file_path)
    return file


def _extract_tar(file):
    tmp = tempfile.mkdtemp()
    tar_file = tarfile.open(file, 'r')
    tar_file.extractall(tmp)
    extracted = path.join(tmp, tar_file.getnames()[0])
    tar_file.close()
    return extracted
