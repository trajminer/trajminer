from trajminer import TrajectoryData
from trajminer.preprocessing import TrajectorySegmenter


data = TrajectoryData(attributes=['poi', 'hour', 'rating'],
                      data=[[['Bakery', 8, 8.6], ['Work', 9, 8.9],
                             ['Restaurant', 12, 7.7], ['Bank', 12, 5.6],
                             ['Work', 13, 8.9], ['Home', 19, 0]],
                            [['Home', 8, 0], ['Mall', 10, 9.3],
                             ['Home', 19, 0], ['Pub', 21, 9.5]]],
                      tids=[20, 24],
                      labels=[1, 2])


class TestTrajectorySegmenter(object):

    def test_one(self):
        segmenter = TrajectorySegmenter(attributes=data.get_attributes(),
                                        thresholds=None, mode='strict',
                                        n_jobs=1)
        print(segmenter.fit_transform(data))
        assert True  # TO-DO

    def test_two(self):
        assert True  # TO-DO
