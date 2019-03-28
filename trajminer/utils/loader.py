import pandas as pd

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
    drop_col : array-like (default=[])
        List of columns to drop when reading the data from the file.

    Examples
    --------
    >>> from trajminer.utils import CSVTrajectoryLoader
    >>> loader = CSVTrajectoryLoader('my_data.csv')
    >>> dataset = loader.load()
    >>> dataset.get_attributes()
    ['poi', 'day', 'time']
    """

    def __init__(self, file, sep=',', tid_col='tid', label_col='label',
                 drop_col=[]):
        self.file = file
        self.sep = sep
        self.tid_col = tid_col
        self.label_col = label_col
        self.drop_col = drop_col

    def load(self):
        df = pd.read_csv(self.file, sep=self.sep)
        attributes = list(df.keys())

        attributes.remove(self.tid_col)

        if self.label_col:
            attributes.remove(self.label_col)

        for col in self.drop_col:
            if col in attributes:
                attributes.remove(col)

        tids = df[self.tid_col].unique()
        data = []
        labels = None

        if self.label_col:
            labels = []
            for tid in tids:
                data.append(df.loc[df['tid'] == tid, attributes].values)
                labels.append(df.loc[df['tid'] == tid, ['label']].values[0][0])
        else:
            for tid in tids:
                data.append(df.loc[df['tid'] == tid, attributes].values)

        return TrajectoryData(attributes=attributes,
                              data=data,
                              tids=tids,
                              labels=labels)
