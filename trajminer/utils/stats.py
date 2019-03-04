def compute_dataset_stats(data, print_stats=False):
    """Computes statistics for a given dataset.

    Parameters
    ----------
    data : dict
        A dictionary as loaded by a :class:`trajminer.utils.TrajectoryLoader`
    print_stats : bool (default=False)
        If `True`, stats are printed.

    Returns
    -------
    stats : dict
        A dictionary containing the dataset statistics.
    """
    import numpy as np

    traj_lengths = [len(x) for x in data['data']]
    points = np.concatenate(data['data'])
    count_not_none = lambda arr: np.sum([1 if x is not None else 0
                                         for x in arr])
    attr_count = [count_not_none(p) for p in points]

    stats = {
        'attribute': {
            'count': len(data['attributes']),
            'min': np.min(attr_count),
            'avg': np.mean(attr_count),
            'std': np.std(attr_count),
            'max': np.max(attr_count)
        },
        'point': {
            'count': np.sum(traj_lengths)
        },
        'trajectory': {
            'count': len(data['data']),
            'length': {
                'min': np.min(traj_lengths),
                'avg': np.mean(traj_lengths),
                'std': np.std(traj_lengths),
                'max': np.max(traj_lengths)
            }
        }
    }

    if print_stats:
        print('==========================================================')
        print('                           STATS                          ')
        print('==========================================================')
        print('ATTRIBUTE')
        print('  Count:           ', stats['attribute']['count'])
        print('  Min:             ', stats['attribute']['min'])
        print('  Max:             ', stats['attribute']['max'])
        print('  Avg ± Std:        %.4f ± %.4f' % (stats['attribute']['avg'],
              stats['attribute']['std']))

        print('\nPOINT')
        print('  Count:           ', stats['point']['count'])

        print('\nTRAJECTORY')
        print('  Count:           ', stats['trajectory']['count'])
        print('  Min length:      ', stats['trajectory']['length']['min'])
        print('  Max lenght:      ', stats['trajectory']['length']['max'])
        print('  Avg length ± Std: %.4f ± %.4f' %
              (stats['trajectory']['length']['avg'],
               stats['trajectory']['length']['std']))

    if 'labels' in data:
        unique, counts = np.unique(data['labels'], return_counts=True)
        stats['label'] = {
            'count': len(unique),
            'min': np.min(counts),
            'avg': np.mean(counts),
            'std': np.std(counts),
            'max': np.max(counts)
        }

        if print_stats:
            print('\nLABEL')
            print('  Count:           ', stats['label']['count'])
            print('  Min:             ', stats['label']['min'])
            print('  Max:             ', stats['label']['max'])
            print('  Avg ± Std:        %.4f ± %.4f' % (stats['label']['avg'],
                  stats['label']['std']))
            print('==========================================================')
    elif print_stats:
        print('==========================================================')

    return stats
