import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import app, activities

client = TestClient(app)


def test_unregister_removes_participant_from_activity():
    # Arrange
    activity = activities["Chess Club"]
    original = activity["participants"][:]
    test_email = "newstudent@mergington.edu"

    try:
        activity["participants"].append(test_email)

        # Act
        response = client.delete(
            "/activities/Chess Club/unregister",
            params={"email": test_email},
        )

        # Assert
        assert response.status_code == 200
        assert test_email not in activity["participants"]
        assert response.json()["message"] == f"Unregistered {test_email} from Chess Club"
    finally:
        activity["participants"] = original


def test_unregister_missing_participant_returns_404():
    # Arrange
    activity_name = "Soccer Team"
    email = "missing@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
