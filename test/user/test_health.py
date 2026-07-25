from fastapi.testclient import TestClient

def test_app_starts(client):
    assert client is not None
    
def test_root(client: TestClient ):
    
    response = client.get("/api/v1/bms")
    
    assert response.status_code == 200