cookbook = {
	"Sandwich" : {
		"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
		"meal" : "lunch",
		"prep_time" : 10
	},
	"Cake" : {
		"ingredients" : ["floor", "sugar", "egg"],
		"meal" : "dessert",
		"prep_time" : 60
	},
	"Salad" : {
		"ingredients" : ["avocado", "tomatos", "spinach"],
		"meal" : "lunsh",
		"prep_time" : 15
	}
}


def print_resipies():
	print("available recipies are: ", end='')
	for c in cookbook.keys():
		print(c, end=' ')


def print_specific_recipe():
	recipe = input("please enter a recipe name to get its details:\n>>")
	if recipe in cookbook.keys():
		print("Recipe for " + recipe + ":")
		print("Ingredient list: ", end='')
		print((cookbook[str(recipe)])['ingredients'])
		print("to be eaten of " + cookbook[str(recipe)]["meal"])
		print("takes " + str(cookbook[str(recipe)]["prep_time"]) + " minuts of cooking")
	else:
		print("recipe does not exist!")

def delet_recipe():
	recipe = input("enter a recipe that you want to delet\n>>")
	if recipe in cookbook.keys():
		del cookbook[str(recipe)]
	else:
		print("recipe does not exist!")

def Add_recipe():
	name = input("enter name\n")
	cookbook[name] = {}
	print("enter ingrdients")
	ing = 'c'
	cookbook[name]['ingredients'] = []
	ing = input()
	while ing != '':
		cookbook[name]['ingredients'].append(ing)
		ing = input()
	ing = input("entre meal type\n")
	cookbook[name]['meal'] = ing
	ing = input("entre preparation time\n")
	cookbook[name]['prep_time'] = ing



print("Welcome to the Python Cookbook !")
print("List of available option:\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit")
while True:
	print("please select an option")
	option = input(">>")
	if option is "1":
		Add_recipe()
	elif option is "2":
		delet_recipe()
	elif option is "4":
		print(cookbook)
	elif option is "3":
		print_specific_recipe()
	elif option is "5":
		print("Cookbook closed. Goodbye !")
		break
	else:
		print("Sorry, this option does not exist")
		print("List of available option:\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit")