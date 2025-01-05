from unittest.mock import Mock, patch
from app.models import Movie

def test_movie_nullable_fields():
    # Test that nullable fields can be None
    movie = Movie(
        title="Test Movie",
        description="Test Description",
        duration=120
    )
    
    assert movie.released_date is None
    assert movie.rating is None

def test_movie_str_representation():
    movie = Movie(
        title="Test Movie",
        description="Test Description",
        duration=120
    )
    
    expected_str = "<Movie Test Movie: description Test Description >"
    assert str(movie) == expected_str
