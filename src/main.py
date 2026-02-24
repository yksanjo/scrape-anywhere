from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from src.scoring import classify_score, compute_score

PROJECT = "scrape-anywhere"
DOMAIN = "application"
GOAL = "core runtime signals to support reliable product operations"


@dataclass
class Assessment:
    project: str
    domain: str
    goal: str
    score: float
    status: str
    reasons: list[str]
    recommendations: list[str]
    timestamp: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "project": self.project,
            "domain": self.domain,
            "goal": self.goal,
            "score": self.score,
            "status": self.status,
            "reasons": self.reasons,
            "recommendations": self.recommendations,
            "timestamp": self.timestamp,
        }


def recommendations_for(status: str) -> list[str]:
    if status == "critical":
        return ["page-oncall", "open-incident", "contain-impact"]
    if status == "high":
        return ["create-ticket", "assign-owner", "increase-observability"]
    if status == "medium":
        return ["queue-review", "collect-context"]
    return ["record-signal"]


def assess(signal: str) -> Assessment:
    score, reasons = compute_score(signal)
    status = classify_score(score)
    return Assessment(
        project=PROJECT,
        domain=DOMAIN,
        goal=GOAL,
        score=score,
        status=status,
        reasons=reasons,
        recommendations=recommendations_for(status),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


def summarize(signal: str) -> str:
    result = assess(signal)
    return (
        f"{result.project} [{result.domain}] "
        f"status={result.status} score={result.score:.2f} "
        f"reasons={','.join(result.reasons)}"
    )


if __name__ == "__main__":
    print(summarize("baseline health check with warning latency"))
