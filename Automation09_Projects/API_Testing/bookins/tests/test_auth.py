from bookins.requests.auth import *


def test_auth():
    response = auth('admin', 'password123')
    print(response.json())

