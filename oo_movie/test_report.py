from oo_carla_report import Movie
import pytest

def test_class_exist():
    assert Movie

def test_movie_properties_or_construction():
    result = Movie('lamaland', ['lama'], 2025, "nobody", 10)
    assert result.title == 'lamaland'
    assert result.actors == ['lama']
    assert result.year == 2025
    assert result.genre == 'nobody'
    assert result.rating == 10

def test_str_method():
    result = Movie('lamaland', ['lama'], 2025, "nobody", 10).__str__()
    assert result == 'lamaland, 10'

def test_str_method_second():
    movie = Movie('lamaland', ['lama'], 2025, "nobody", 10)
    result = movie.__str__()
    assert result == 'lamaland, 10'

def test_str_method_third():
    movie = Movie('lamaland', ['lama'], 2025, "nobody", 10)
    result = str(movie)
    assert result == 'lamaland, 10'

def test_lt_method():# less-than operator
    movie = Movie('lamaland', ['lama'], 2025, "nobody", 9)
    movie1 = Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 10)
    assert movie < movie1

def test_lt_method_other_way_around():
    movie = Movie('lamaland', ['lama'], 2025, "nobody", 9)
    movie1 = Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 10)
    assert not movie1 < movie

def test_lt_method_again():
    movie = Movie('lamaland', ['lama'], 2025, "nobody", 9)
    movie1 = Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 10)
    with pytest.raises(TypeError):
        assert movie < 19

