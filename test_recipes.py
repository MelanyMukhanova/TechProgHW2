from recipes import Ingredient

def ingred_correct_init():
    one = Ingredient("Мука", 500, "Г")
    assert one.name == "Мука"
    assert one.quantity == 500.0
    assert one.unit == "Г"

def ingred_str_correct():
    one = Ingredient("Мука", 500, "Г")
    assert str(one) == "Мука: 500.0 г"

def ingred_eq_same_nu():
    one = Ingredient("Мука", 500, "Г")
    other = Ingredient("Мука", 300, "Г")
    assert one == other
