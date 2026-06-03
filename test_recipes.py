import pytest
from recipes import Ingredient

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