from src.main import assess, summarize


def test_assess_smoke() -> None:
    result = assess("critical outage detected")
    assert result.project
    assert 0.0 <= result.score <= 1.0
    assert result.status in {"critical", "high", "medium", "low"}


def test_summary_smoke() -> None:
    text = summarize("warning latency")
    assert "status=" in text
    assert "score=" in text
