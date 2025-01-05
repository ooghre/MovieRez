from unittest.mock import Mock, patch
from app.models import User

def test_user_nullable_fields():
    # Test that nullable fields can be None
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password="hashedpass123"
    )
    
    assert user.phone_number is None
    assert user.preferences is None

def test_user_str_representation():
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password="hashedpass123"
    )
    
    expected_str = "<User testuser>"
    assert str(user) == expected_str