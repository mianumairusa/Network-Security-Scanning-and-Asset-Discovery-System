def ai_explain(ports, risk):
    if risk == "HIGH":
        return "Critical services exposed. Immediate mitigation recommended."
    elif risk == "MEDIUM":
        return "Moderate exposure. Review security configurations."
    elif risk == "LOW":
        return "Low risk. Maintain monitoring."
    return "No significant risk detected."
