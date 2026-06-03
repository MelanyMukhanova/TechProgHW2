import pytest
from recipes import Ingredient, Recipe

def test_ingred_correct_init():
    one = Ingredient("Мука", 500, "г")
    assert one.name == "Мука"
    assert one.quantity == 500.0
    assert one.unit == "г"

def test_ingred_str_correct():
    one = Ingredient("Мука", 500, "г")
    assert str(one) == "Мука: 500.0 г"

def test_ingred_eq_same_nu():
    one = Ingredient("Мука", 500, "г")
    other = Ingredient("Мука", 300, "г")
    assert one == other

def test_ingred_different_names():
    one = Ingredient("Мука", 500, "г")
    other = Ingredient("Соль", 500, "г")
    assert one != other

def test_ingred_different_units():
    one = Ingredient("Мука", 500, "г")
    other = Ingredient("Мука", 500, "мг")
    assert one != other

def test_quantity_is_negative():
    one = Ingredient("Мука", 500, "г")
    with pytest.raises(ValueError, match = "Количество должно быть положительным"):
        one.quantity = -500


def test_recipe_correct_init():
    flour = Ingredient("Мука", 500, "г")
    milk = Ingredient("Молоко", 500, "мл")
    recipe = Recipe("Charlotte", [flour, milk])
    assert recipe.title == "Charlotte"
    assert len(recipe.ingredients) == 2

def test_add_ingred_correct():
    recipe = Recipe("Charlotte")
    flour = Ingredient("Мука", 500, "г")
    recipe.add_ingredient(flour)
    assert len(recipe) == 1
    assert recipe.ingredients[0].name == "Мука"

def test_add_dublicate_correct():
    recipe = Recipe("Charlotte")
    flour1 = Ingredient("Мука", 500, "г")
    flour2 = Ingredient("Мука", 300, "г")
    recipe.add_ingredient(flour1)
    recipe.add_ingredient(flour2)
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 800

def test_scale_correct():
    flour = Ingredient("Мука", 500, "г")
    recipe = Recipe("Charlotte", [flour])
    new_one = recipe.scale(2)
    assert recipe.ingredients[0].quantity == 500
    assert new_one.ingredients[0].quantity == 1000
    assert new_one.title == "Charlotte"

def __len__():
    flour = Ingredient("Мука", 500, "г")
    milk = Ingredient("Молоко", 500, "мл")
    recipe = Recipe("Charlotte", [flour, milk])
    assert len(recipe) == 2

def test_scale_invalid_rat():
    flour = Ingredient("Мука", 500, "г")
    recipe = Recipe("Charlotte", [flour])
    with pytest.raises(ValueError, match = "Число должно быть положительным"):
        recipe.scale(-1)
    with pytest.raises(ValueError, match = "Число должно быть положительным"):
        recipe.scale(0)

