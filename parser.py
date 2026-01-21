def parse_answers(data: dict):
    fields = ["age", "smoker", "exercise", "diet"]
    missing_fields = []

    for field in fields:
        if data.get(field) is None:
            missing_fields.append(field)

    confidence = round(1 - (len(missing_fields) / len(fields)), 2)

    return {
        "answers": data,
        "missing_fields": missing_fields,
        "confidence": confidence
    }
