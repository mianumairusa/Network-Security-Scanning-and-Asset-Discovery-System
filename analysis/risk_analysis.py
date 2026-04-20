def analyze_risk(ports):
    if any(p in ports for p in [21,23]):
        return "HIGH"
    elif any(p in ports for p in [22,80,443]):
        return "MEDIUM"
    elif ports:
        return "LOW"
    return "SECURE"
