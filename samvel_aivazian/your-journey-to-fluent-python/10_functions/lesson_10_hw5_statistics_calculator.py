import logging
import statistics

logging.basicConfig(level=logging.INFO, format='%(message)s')


def calculate_statistics(*data, **options):
    stats = {}
    if not data:
        return stats

    if options.get('mean', True):
        stats['mean'] = statistics.mean(data)
    if options.get('median', True):
        stats['median'] = statistics.median(data)
    if options.get('mode', True):
        try:
            stats['mode'] = statistics.mode(data)
        except statistics.StatisticsError:
            stats['mode'] = None
    if options.get('range', True):
        stats['range'] = max(data) - min(data)

    return stats


if __name__ == "__main__":
    data_points = [4, 1, 2, 2, 3, 5]
    logging.info(calculate_statistics(*data_points, mean=True, range=True))
    logging.info(calculate_statistics(*data_points))
