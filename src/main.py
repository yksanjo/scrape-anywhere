from dataclasses import dataclass
from datetime import datetime, timezone

PROJECT = "scrape-anywhere"
DOMAIN = "application"


@dataclass
class Assessment:
    project: str
    domain: str
    score: float
    status: str
    reason: str
    timestamp: str


def assess(signal: str) -> Assessment:
    text = signal.lower()
    weight = 0.1
    if any(k in text for k in ["critical", "breach", "outage", "failure", "incident"]):
        weight += 0.6
    if any(k in text for k in ["warning", "anomaly", "retry", "latency"]):
        weight += 0.2
    score = min(weight, 1.0)
    status = "high" if score >= 0.7 else "medium" if score >= 0.4 else "low"
    reason = "Context-aware baseline model for core runtime signals to support reliable product operations."
    return Assessment(PROJECT, DOMAIN, score, status, reason, datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    result = assess("baseline health check")
    print(f"{result.project}:{result.domain}:{result.status}:{result.score}")
