import pytest

@pytest.fixture
def launch():
    print("launch Browser")

@pytest.mark.sanity
def test_login(self):
        print("Login Successful")

def test_cart(self):
        print("Added to cart")
@pytest.mark.sanity
def test_logout(self):
        print("Logged out")

def test_cal(self):
        assert 2 + 2 == 4





