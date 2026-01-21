def calculate_risk(answers: dict):
    score = 0
    factors = []

    if answers.get("smoker") is True:
        score += 30
        factors.append("smoking")

    if answers.get("diet") == "high sugar":
        score += 25
        factors.append("poor diet")

    if answers.get("exercise") in ["rarely", "never"]:
        score += 20
        factors.append("low exercise")

    if score >= 60:
        risk_level = "high"
    elif score >= 30:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "risk_level": risk_level,
        "score": score,
        "factors": factors
    }
