from statistics import mean, median, multimode, StatisticsError
from typing import List, Union, Dict, Any


def calculate_mean(data: List[int]) -> float:
    """Calculate the mean of the data."""
    return mean(data)


def calculate_median(data: List[int]) -> float:
    """Calculate the median of the data."""
    return median(data)


def calculate_mode(data: List[int]) -> Union[int, List[int], str]:
    """Calculate the mode of the data."""
    try:
        mode_values = multimode(data)
        if len(mode_values) == 1:
            return mode_values[0]
        return mode_values
    except StatisticsError:
        return "No mode found"


def calculate_range(data: List[int]) -> int:
    """Calculate the range of the data."""
    return max(data) - min(data)


def calculate_statistics(*data: int, **options: bool) -> Union[str, Dict[str, Any]]:
    """
    Calculate statistics for the given data.

    Args:
    data (int): The data points.
    options (bool): Optional arguments to specify which statistics to calculate.

    Returns:
    Union[str, Dict[str, Any]]: A dictionary of calculated statistics or a message if the dataset is empty.
    """
    if not data:
        return "Dataset is empty"

    statistics = {}
    data_list = list(data)

    if options:
        if options.get("mean", False):
            statistics["mean"] = calculate_mean(data_list)
        if options.get("median", False):
            statistics["median"] = calculate_median(data_list)
        if options.get("mode", False):
            statistics["mode"] = calculate_mode(data_list)
        if options.get("range", False):
            statistics["range"] = calculate_range(data_list)
    else:
        statistics["mean"] = calculate_mean(data_list)
        statistics["median"] = calculate_median(data_list)
        statistics["mode"] = calculate_mode(data_list)
        statistics["range"] = calculate_range(data_list)

    return statistics


# Example usage of the function
data_points = [4, 1, 2, 2, 3, 5]
# Specified options
stats_with_options = calculate_statistics(*data_points, mean=True, range=True)
# All statistics
stats_all = calculate_statistics(*data_points)

print(stats_with_options)
print(stats_all)
