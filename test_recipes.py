from recipes import Ingredient

def ingred_correct_init():
    one = Ingredient("Мука", 500, "Г")
    assert one.name == "Мука"
    assert one.quantity == 500.0
    assert one.unit == "Г"