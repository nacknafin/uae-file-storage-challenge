import os
import tempfile
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_file_upload():
    with tempfile.NamedTemporaryFile(delete=False) as file:
        file.write(b"Test file contents")
        file_path = file.name

    with open(file_path, "rb") as f:
        response = client.post("/files", files={"files": f})

    assert response.status_code == 200
    assert response.json()["message"].startswith("Successfully uploaded")

    message = response.json()["message"]
    start_idx = message.find("(")
    end_idx = message.find(")")
    file_id = message[start_idx+1:end_idx]

    assert os.path.isfile(f"app/files/{file.name}") == True

    os.remove(file_path)
