from joblib import Parallel, delayed
from sklearn.utils import gen_even_slices
import pandas as pd
import numpy as np

from ..trajectory_data import TrajectoryData


class TrajectoryLoader(object):
    """Base class for trajectory loaders.
    """

    def load(self):
        """Loads trajectories according to the specific approach.

        Returns
        -------
        data : :class:`trajminer.TrajectoryData`
            A :class:`trajminer.TrajectoryData` containing the loaded dataset.
        """
        pass


class CSVTrajectoryLoader(TrajectoryLoader):
    """A trajectory data loader from a CSV file.

    Parameters
    ----------
    file : str
        The CSV file from which to read the data.
    sep : str (default=',')
        The CSV separator.
    tid_col : str (default='tid')
        The column in the CSV file corresponding to the trajectory IDs.
    label_col : str (default='label')
        The column in the CSV file corresponding to the trajectory labels. If
        `None`, labels are not loaded.
    lat : str (default='lat')
        The column in the CSV file corresponding to the latitude of the
        trajectory points. If both the `lat` and `lon` columns are present in
        the file, they are included as a single new attribute in the loaded
        dataset.
    lon : str (default='lon')
        The column in the CSV file corresponding to the longitude of the
        trajectory points. If both the `lat` and `lon` columns are present in
        the file, they are included as a single new attribute in the loaded
        dataset.
    drop_col : array-like (default=[])
        List of columns to drop when reading the data from the file.
    n_jobs : int (default=1)
        The number of parallel jobs.

    Examples
    --------
    >>> from trajminer.utils import CSVTrajectoryLoader
    >>> loader = CSVTrajectoryLoader('my_data.csv')
    >>> dataset = loader.load()
    >>> dataset.get_attributes()
    ['poi', 'day', 'time']
    """

    def __init__(self, file, sep=',', tid_col='tid', label_col='label',
                 lat='lat', lon='lon', drop_col=[], n_jobs=1):
        self.file = file
        self.sep = sep
        self.tid_col = tid_col
        self.label_col = label_col
        self.lat = lat
        self.lon = lon
        self.drop_col = drop_col
        self.n_jobs = n_jobs

    def load(self):
        df = pd.read_csv(self.file, sep=self.sep)
        attributes = list(df.keys())
        attributes.remove(self.tid_col)

        if self.label_col:
            attributes.remove(self.label_col)

        lat_lon = self.lat in attributes and self.lon in attributes

        if lat_lon:
            attributes.remove(self.lat)
            attributes.remove(self.lon)

        for col in self.drop_col:
            if col in attributes:
                attributes.remove(col)

        tids = sorted(df[self.tid_col].unique())

        def load_tids(slice):
            ret = []

            for idx in range(slice.start, slice.stop):
                tid = tids[idx]
                traj = df.loc[df['tid'] == tid, attributes].values

                if lat_lon:
                    loc = df.loc[df['tid'] == tid, [self.lat, self.lon]].values
                    new_traj = [np.append(traj[i], loc[i])
                                for i in range(0, len(loc))]
                    traj = new_traj
                ret.append(traj)
            return ret

        labels = None
        func = delayed(load_tids)

        data = Parallel(n_jobs=self.n_jobs, verbose=0)(
            func(s) for s in gen_even_slices(len(tids), self.n_jobs))

        data = np.concatenate(data)

        if self.label_col:
            labels = df \
                .drop_duplicates(subset=[self.tid_col, self.label_col],
                                 inplace=False) \
                .sort_values(self.tid_col,
                             ascending=True,
                             inplace=False)[self.label_col].values

        if lat_lon:
            attributes.append('lat_lon')

        return TrajectoryData(attributes=attributes,
                              data=data,
                              tids=tids,
                              labels=labels)
