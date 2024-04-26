from fastapi.testclient import TestClient
from random import randrange
import pytest
from fastapi import status
from dotenv import load_dotenv
import os 
from app.main import app

load_dotenv()

ENDPOINT = "http://localhost:8000"

client = TestClient(app)

@pytest.mark.parametrize(
    "path,method",
    [
        (f"{ENDPOINT}/users", "POST"),
        (f"{ENDPOINT}/profile", "GET"),
        (f"{ENDPOINT}/login", "POST"),
        (f"{ENDPOINT}/users", "GET"),
        (f"{ENDPOINT}/users/1", "POST"),
        (f"{ENDPOINT}/cars/all", "GET"),
        (f"{ENDPOINT}/cars", "POST"),
        (f"{ENDPOINT}/cars/1", "GET"),
        (f"{ENDPOINT}/cars/mycars", "GET"),
        (f"{ENDPOINT}/users", "POST"),
        (f"{ENDPOINT}/cars/buyer/offer", "POST"),
        (f"{ENDPOINT}/cars/buyer/offer", "GET"),
        (f"{ENDPOINT}/cars/offer/1", "POST"),
        (f"{ENDPOINT}/cars/offer/1", "PUT"),
        (f"{ENDPOINT}/cars/offer/1/buyer", "POST"),
        
        
        
        
        
    ],
)
def test_route_exists(path: str, method: str) -> None:
    """
    Test if the specified route exists and is reachable.
    """
    response = client.request(method, path)
    assert response.status_code not in (
        status.HTTP_404_NOT_FOUND,
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )

def generate_user() :
    random_number = randrange(1, 100000)
    return {
        "name": "Fahim Shakil",
        "email": f"user{random_number}@example.com",
        "password": "1234",
        "phone" : "1234567890"
}


def test_create_user():
    user_data = generate_user()
    response = client.post(ENDPOINT + "/users", json = user_data)
    assert response.status_code == 201
    user = response.json()
    assert user["access_token"] != None

def test_get_user_profile():
    user_data = generate_user()
    response = client.post(ENDPOINT + "/users", json = user_data)
    token = response.json()["access_token"]
    profile = client.get(ENDPOINT + "/profile", headers={"Authorization": f"Bearer {token}"})
    assert profile.status_code == 200
    




    

    
    


    

