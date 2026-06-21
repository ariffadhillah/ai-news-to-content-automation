# app/incident_scorer.py

def calculate_score(incident):
    score = 0

    if incident["severity"] == "fatal":
        score += 30

    elif incident["severity"] == "serious":
        score += 20

    elif incident["severity"] == "moderate":
        score += 10

    score += incident["fatalities"] * 20
    score += incident["injuries"] * 5

    if incident["commercial_vehicle"]:
        score += 15

    if incident["child_involved"]:
        score += 15

    if incident["dui_suspected"]:
        score += 15

    return score


def classify_priority(score):
    if score >= 60:
        return "HIGH"

    if score >= 30:
        return "MEDIUM"

    return "LOW"