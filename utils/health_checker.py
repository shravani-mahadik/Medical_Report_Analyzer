from utils.constants import NORMAL_RANGES


def check_health(parameters):
    """
    Compare extracted medical parameters with normal ranges.
    Returns a dictionary containing value and status.
    """

    results = {}

    for parameter, value in parameters.items():

        # Skip if parameter is not available
        if value == "Not Found":
            results[parameter] = {
                "Value": value,
                "Status": "Not Available"
            }
            continue

        # Skip if no normal range exists
        if parameter not in NORMAL_RANGES:
            results[parameter] = {
                "Value": value,
                "Status": "No Reference"
            }
            continue

        try:
            numeric_value = float(value)

            low, high = NORMAL_RANGES[parameter]

            if numeric_value < low:
                status = "🔶 Low"

            elif numeric_value > high:
                status = "🔴 High"

            else:
                status = "🟢 Normal"

        except:
            status = "Unknown"

        results[parameter] = {
            "Value": value,
            "Status": status
        }

    return results