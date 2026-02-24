from src.scoring import classify_score, compute_score


def test_compute_score_keywords() -> None:
    score, reasons = compute_score("critical breach")
    assert score > 0.5
    assert any(r.startswith("keyword:") for r in reasons)


def test_classification() -> None:
    assert classify_score(0.85) == "critical"
    assert classify_score(0.65) == "high"
    assert classify_score(0.40) == "medium"
    assert classify_score(0.10) == "low"
