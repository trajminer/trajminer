from pathlib import Path
from urllib import request
import tarfile
import tempfile

_trajminer_data_dir = None


def set_cache_dir(folder):
    global _trajminer_data_dir
    _trajminer_data_dir = Path(folder)


def get_file_url(folder, file_name):
    return 'https://github.com/trajminer/data/blob/master/' + \
           f'{folder}/{file_name}?raw=true'


def download_file(folder, file_name, cache=True):
    _create_cache_dir(folder)

    file_path = _trajminer_data_dir.joinpath(folder, file_name)
    if not cache or not file_path.is_file():
        request.urlretrieve(get_file_url(folder, file_name), file_path)

    return file_path


def extract_tar(folder, file, cache=True):
    _create_cache_dir(folder)

    extraction_folder = _trajminer_data_dir.joinpath(folder)

    with tarfile.open(file, 'r') as tar_file:
        extracted_file = extraction_folder.joinpath(tar_file.getnames()[0])

        if not cache or not extracted_file.is_file():
            tar_file.extractall(extraction_folder)

    return extracted_file


def _create_cache_dir(folder):
    global _trajminer_data_dir
    if _trajminer_data_dir is None:
        _trajminer_data_dir = Path(_get_temp_dir())

    Path(_trajminer_data_dir, folder).mkdir(parents=True, exist_ok=True)


def _get_temp_dir():
    dirs = Path(tempfile.gettempdir()).glob('trajminer_data_*')

    try:
        return next(dirs)
    except StopIteration:
        return tempfile.mkdtemp(prefix='trajminer_data_')
