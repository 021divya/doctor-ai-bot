def generate_summary(parameters, abnormal):

    summary = []

    for param, status in abnormal.items():

        if status == "LOW":
            summary.append(f"{param} is below normal range")

        elif status == "HIGH":
            summary.append(f"{param} is above normal range")

    if not summary:
        return "All parameters are within normal range"

    return ". ".join(summary)