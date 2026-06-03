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

    def remove_recipe(self, title: str):
        self._items = [one for one in self._items if one[1] != title]
    
    def get_list(self):
        res = {}
        for one, title in self._items:
            key = (one.name, one.unit)
            if key in res:
                res[key] += one.quantity
            else:
                res[key] = one.quantity

        itog = []
        for (name, unit), quantity in res.items():
            itog.append(Ingredient(name, quantity, unit))

        itog.sort(key = lambda x: x.name)
        return itog
    
    def __add__(self, other: ShoppingList):
        new_l = ShoppingList()
        new_l._items = self._items + other._items
        return new_l

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Ratio должно быть положительным")
        new_sum_ingred = []
        for one in self.ingredients:
            new_one = Ingredient(one.name, one.quantity * ratio, one.unit)
            new_sum_ingred.append(new_one)
        return DietaryRecipe(self.title, self.diet_type, new_sum_ingred)