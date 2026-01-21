from fastapi import FastAPI
from backend.schemas import HealthInput
from backend.parser import parse_answers
from backend.risk_engine import calculate_risk

app = FastAPI(title="AI Health Risk Profiler")

@app.get("/")
def home():
    return {"message": "Health Risk Profiler API is running"}

@app.post("/analyze")
def analyze_health(data: HealthInput):
    parsed = parse_answers(data.dict())

    # Guardrail: incomplete profile
    if len(parsed["missing_fields"]) > 2:
        return {
            "status": "incomplete_profile",
            "reason": ">50% fields missing",
            "missing_fields": parsed["missing_fields"]
        }

    risk = calculate_risk(parsed["answers"])

    recommendations = []

    if "smoking" in risk["factors"]:
        recommendations.append("Quit smoking")
    if "poor diet" in risk["factors"]:
        recommendations.append("Reduce sugar intake")
    if "low exercise" in risk["factors"]:
        recommendations.append("Walk 30 minutes daily")

    return {
        "risk_level": risk["risk_level"],
        "score": risk["score"],
        "factors": risk["factors"],
        "recommendations": recommendations,
        "status": "ok"
    }
