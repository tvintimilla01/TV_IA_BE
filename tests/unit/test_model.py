from api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are correctly defined
    """
    recipe = Recipe('Pancakes', 'Flour, Butter, Eggs, Banana, Salt, Butter', 'Mix everything, cook in a pan one by one with butter', 5, True)
    assert recipe.name == 'Pancakes'
    assert recipe.ingredients == 'Flour, Butter, Eggs, Banana, Salt, Butter'
    assert recipe.steps == 'Mix everything, cook in a pan one by one with butter'
    assert recipe.rating == 5
    assert recipe.favorite == True