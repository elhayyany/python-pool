from recipe import Recipe
import  datetime
class Book:
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now().strftime("%D-%H:%M:%S")
        self.last_update = self.creation_date
        self.recipe_list = {}
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for key in self.recipe_list.keys() :
            for recipe in self.recipe_list[key] :
                if name is recipe.name :
                    return recipe
        raise ValueError(f"no recipe with {name} name")
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("unkown recipe type")
        return self.recipe_list[recipe_type]
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise ValueError("ash awaa hadaaa")
        if recipe.recipe_type in self.recipe_list:
            self.recipe_list[recipe.recipe_type].append(recipe)
        else:
            self.recipe_list[recipe.recipe_type] = [recipe]
            