import re

def extract_parameters(text):

    parameters = {}

    hemoglobin = re.search(r'Hemoglobin\s*[:\-]?\s*(\d+\.?\d*)', text)
    cholesterol = re.search(r'Cholesterol\s*[:\-]?\s*(\d+\.?\d*)', text)
    wbc = re.search(r'WBC\s*[:\-]?\s*(\d+\.?\d*)', text)
    platelets = re.search(r'Platelets\s*[:\-]?\s*(\d+)', text)

    if hemoglobin:
        parameters["hemoglobin"] = float(hemoglobin.group(1))

    if cholesterol:
        parameters["cholesterol"] = float(cholesterol.group(1))

    if wbc:
        parameters["wbc"] = float(wbc.group(1))

    if platelets:
        parameters["platelets"] = float(platelets.group(1))

    return parameters