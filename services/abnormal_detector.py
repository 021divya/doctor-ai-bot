normal_ranges = {
    "hemoglobin": (12, 16),
    "cholesterol": (0, 200),
    "wbc": (4000, 11000),
    "platelets": (150000, 450000)
}

def detect_abnormal(parameters):

    abnormal = {}

    for param, value in parameters.items():

        if param not in normal_ranges:
            abnormal[param] = "UNKNOWN"
            continue

        min_val, max_val = normal_ranges[param]

        if value < min_val:
            abnormal[param] = "LOW"

        elif value > max_val:
            abnormal[param] = "HIGH"

        else:
            abnormal[param] = "NORMAL"

    return abnormal