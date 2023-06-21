from book import Book
from recipe import Recipe

cookbook = Book("bookyy")

rc1 = Recipe("wasfa", 3, 3, "ha slccd ", "starter")
print(rc1)
rc2 = Recipe("wasfa1", 3, 3, "ha slccd ", "starter")
print(rc2)
rc3 = Recipe("wasfa2", 3, 3, "ha slccd ", "starter")
print(rc3)
rc4 = Recipe("wasfa3", 3, 3, "ha slccd ", "starter")
print(rc4)
rc5 = Recipe("wasfa4", 3, 3, "ha slccd ", "starter")
print(rc5)
rc6 = Recipe("wasfa5", 3, 3, "ha slccd ", "starter")
print(rc6)

cookbook.add_recipe(rc1)
cookbook.add_recipe(rc2)
cookbook.add_recipe(rc3)
cookbook.add_recipe(rc4)
cookbook.add_recipe(rc5)
cookbook.add_recipe(rc6)


print(cookbook.get_recipes_by_types("starter"))# for x in range(len(cookbook.get_recipes_by_types("starter"))))
