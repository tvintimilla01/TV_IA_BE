from cook_api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are correctly defined
    """
    recipe = Recipe('Pancakes', 'Flour, Water, Salt, Sugar, Butter', 'Mix the ingredients, cook one by one with butter', 5, True)
    assert recipe.name == 'Pancakes'
    assert recipe.ingredients == 'Flour, Water, Salt, Sugar, Butter'
    assert recipe.steps == 'Mix the ingredients, cook one by one with butter'
    assert recipe.rating == 5
    assert recipe.favorite == True