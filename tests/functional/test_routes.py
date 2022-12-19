from api import app
import pytest

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is accessed (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_dummy_wrong_method():
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is accessed (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.post('/')
        assert response.status_code == 400

def test_get_recipes(testing_client):
    response = testing_client.get('/')
    assert response.status_code == 200

def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is posted (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/', json={'name': 'recipe1', 'ingredients': 'ingredient1', 'steps': 'step1', 'rating': 1, 'favorite': False})
    assert response.status_code == 200

def test_create_recipe_invalid_rating(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page has invalid rating
    THEN check the response is valid
    """
    response = testing_client.post('/', json={'name': 'recipe1', 'ingredients': 'ingredient1', 'steps': 'step1', 'rating': 6, 'favorite': False})
    assert response.status_code == 200

def test_get_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<id>' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/1')
    assert response.status_code == 200

def test_update_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<id>' page is posted (PUT)
    THEN check the response is valid
    """
    response = testing_client.put('/1', json={'name': 'recipe1', 'ingredients': 'ingredient1', 'steps': 'step1', 'rating': 1, 'favorite': False})
    assert response.status_code == 200

def test_delete_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<id>' page is posted (DELETE)
    THEN check the response is valid
    """
    response = testing_client.delete('/1')
    assert response.status_code == 200

