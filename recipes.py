class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self._quantity = float(quantity)
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value: float):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

class Recipe:
    def __init__(self, title: str, ingredients: list = None):
        self.title = title
        if ingredients is not None:
            self.ingredients = ingredients
        else:
            self.ingredients = []
    
    def add_ingredient(self, ingredient: Ingredient):
        for one in self.ingredients:
            if one == ingredient:
                one.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
