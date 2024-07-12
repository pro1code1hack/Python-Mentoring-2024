from statistics import mean, median, multimode, StatisticsError


# Task 5: Advanced Statistics Calculator
def calculate_statistics(*data: int, **options: bool) -> str | dict[str, int | str]:
    if not data:
        return "Dataset is empty"

    statistics = {}

    # If options are provided, calculate based on options
    if options:
        if options.get("mean", False):
            statistics["mean"] = mean(data)
        if options.get("median", False):
            statistics["median"] = median(data)
        if options.get("mode", False):
            try:
                mode_values = multimode(data)
                if len(mode_values) == 1:  # Only one mode
                    statistics["mode"] = mode_values[0]
                else:
                    statistics["mode"] = mode_values  # Multiple modes
            except StatisticsError:
                statistics["mode"] = "No mode found"  # No mode in the data
        if options.get("range", False):
            statistics["range"] = max(data) - min(data)

    # If no options are provided, calculate all statistics
    else:
        statistics["mean"] = mean(data)
        statistics["median"] = median(data)
        try:
            mode_values = multimode(data)
            if len(mode_values) == 1:  # Only one mode
                statistics["mode"] = mode_values[0]
            else:
                statistics["mode"] = mode_values  # Multiple modes
        except StatisticsError:
            statistics["mode"] = "No mode found"  # No mode in the data
        statistics["range"] = max(data) - min(data)

    return statistics


# Example usage of the function
data_points = [4, 1, 2, 2, 3, 5]
# Specified options
stats_with_options = calculate_statistics(*data_points, mean=True, range=True)
# All statistics
stats_all = calculate_statistics(*data_points)

print(stats_with_options)
print(stats_all)
