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

    @staticmethod
    def is_valid_ratio(ratio: float):
        return isinstance(ratio, (int,float)) and ratio > 0
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Число должно быть положительным")
        new_list = []
        for one in self.ingredients:
            new_quan = one.quantity * ratio
            new_one = Ingredient(one.name, new_quan, one.unit)
            new_list.append(new_one)
        return Recipe(self.title, new_list)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        res = f"Рецепт: {self.title}\nИнгредиенты:\n"
        for one in self.ingredients:
            res += f" -> {one}\n"
        return res
    
class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_rec = recipe.scale(portions)
        for one in scaled_rec.ingredients:
            self._items.append((one, recipe.title))

        