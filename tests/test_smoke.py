from src.main import assess


def test_assess_smoke() -> None:
    result = assess("critical outage detected")
    assert result.project
    assert 0.0 <= result.score <= 1.0
