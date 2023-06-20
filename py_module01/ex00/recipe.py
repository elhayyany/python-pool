class   Recipe:
    def __init__(self, name, cooking_lvl, cooling_time, ingredients, recipe_type, description = ""):
        if not name or not cooking_lvl or not cooling_time or not ingredients or not recipe_type:
            raise ValueError("all Recipe atriputs MUST be filled except for description")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("unkown recipe type")
        if cooking_lvl < 0 or cooking_lvl > 5:
            raise ValueError("cooking lvl is between 5 and 0!")
        self.name = name
        self.cooling_lvl = cooking_lvl
        self.cooling_time = cooling_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description
    def __str__(self):
        return f"the name of this recipe is {self.name} and it's cooking levle is {self.cooling_lvl} ..."

