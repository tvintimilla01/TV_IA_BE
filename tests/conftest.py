import pytest
from api.models import Recipe
from api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe('Testing Recipe', 'Testing Ingredients', 'Testing Steps', 1, True)
    db.session.add(recipe)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()