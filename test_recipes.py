import pytest
from recipes import Ingredient, Recipe, ShoppingList

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

def test_len_correct():
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

def test_shop_correct_add():
    flour = Ingredient("Мука", 500, "г")
    milk = Ingredient("Молоко", 500, "мл")
    recipe = Recipe("Charlotte", [flour, milk])
    res = ShoppingList()
    res.add_recipe(recipe, 2)
    assert len(res._items) == 2
    assert res._items[0][1] == "Charlotte"
    assert res._items[1][1] == "Charlotte"

def test_invalid_portions():
    flour = Ingredient("Мука", 500, "г")
    recipe = Recipe("Charlotte", [flour])
    res = ShoppingList()
    with pytest.raises(ValueError, match = "Количество порций должно быть положительным"):
        res.add_recipe(recipe, -2)
    with pytest.raises(ValueError, match = "Количество порций должно быть положительным"):
        res.add_recipe(recipe, 0)

def test_correct_remove():
    flour = Ingredient("Мука", 500, "г")
    milk = Ingredient("Молоко", 500, "мл")
    recipe_charl = Recipe("Charlotte", [flour, milk])
    recipe_pie = Recipe("Pie", [flour])
    res = ShoppingList()
    res.add_recipe(recipe_charl, 1)
    res.add_recipe(recipe_pie, 1)
    assert len(res._items) == 3
    res.remove_recipe("Charlotte")
    assert len(res._items) == 1
    assert res._items[0][1] == "Pie"

def test_remove_nonexisting():
    res = ShoppingList()
    res.remove_recipe("Абракадабра")
    assert len(res._items) == 0

def test_correct_sum_of_ingred():
    flour = Ingredient("Мука", 500, "г")
    recipe_charl = Recipe("Charlotte", [flour])
    recipe_pie = Recipe("Pie", [flour])
    res = ShoppingList()
    res.add_recipe(recipe_charl, 1)
    res.add_recipe(recipe_pie, 1)
    itog = res.get_list()
    assert len(itog) == 1
    assert itog[0].name == "Мука"
    assert itog[0].quantity == 1000

def test_sorted_correctly():
    flour = Ingredient("Мука", 500, "г")
    milk = Ingredient("Молоко", 500, "мл")
    salt = Ingredient("Соль", 5, "г")
    recipe = Recipe("Charlotte", [flour, milk, salt])
    res = ShoppingList()
    res.add_recipe(recipe, 1)
    itog = res.get_list()
    assert itog[0].name == "Молоко"
    assert itog[1].name == "Мука"
    assert itog[2].name == "Соль"

def test_merging_correctly():
    flour = Ingredient("Мука", 500, "г")
    milk = Ingredient("Молоко", 500, "мл")
    recipe_charl = Recipe("Charlotte", [flour])
    recipe_pie = Recipe("Pie", [milk])
    res1 = ShoppingList()
    res1.add_recipe(recipe_charl, 1)
    res2 = ShoppingList()
    res2.add_recipe(recipe_pie, 1)
    merged = res1 + res2
    assert len(merged._items) == 2
    assert len(res1._items) == 1
    assert len(res2._items) == 1
