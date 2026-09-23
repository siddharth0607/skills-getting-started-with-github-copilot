import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import app, activities

client = TestClient(app)


def test_unregister_removes_participant_from_activity():
    activity = activities["Chess Club"]
    original = activity["participants"][:]
    test_email = "newstudent@mergington.edu"

    try:
        activity["participants"].append(test_email)

        response = client.delete(
            "/activities/Chess Club/unregister",
            params={"email": test_email},
        )

        assert response.status_code == 200
        assert test_email not in activity["participants"]
        assert response.json()["message"] == f"Unregistered {test_email} from Chess Club"
    finally:
        activity["participants"] = original


def test_unregister_missing_participant_returns_404():
    response = client.delete(
        "/activities/Soccer Team/unregister",
        params={"email": "missing@mergington.edu"},
    )

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
