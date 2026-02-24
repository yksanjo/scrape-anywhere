def classify_score(score: float) -> str:
    if score >= 0.8:
        return "critical"
    if score >= 0.6:
        return "high"
    if score >= 0.35:
        return "medium"
    return "low"


def compute_score(text: str) -> tuple[float, list[str]]:
    signal = text.lower()
    weights = {
        "critical": 0.35,
        "breach": 0.35,
        "outage": 0.30,
        "failure": 0.25,
        "incident": 0.25,
        "warning": 0.15,
        "anomaly": 0.20,
        "latency": 0.12,
        "timeout": 0.15,
        "retry": 0.08,
    }
    base = 0.05
    reasons: list[str] = []
    for key, weight in weights.items():
        if key in signal:
            base += weight
            reasons.append(f"keyword:{key}")
    if not reasons:
        reasons.append("keyword:none")
    return min(base, 1.0), reasons
