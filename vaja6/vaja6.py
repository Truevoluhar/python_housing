class Drinks:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def get_name(self):
        return self.name

    def get_ingredients(self):
        return self.ingredients

    def _get_warning_message(self):
        return "Alcohol is bad for you"

    def get_type(self):
        return "Drink"


class AlcoholicDrink(Drinks):
    def __init__(self, name, ingredients, alcohol_percentage):
        super().__init__(name, ingredients)
        self.alcohol_percentage = alcohol_percentage

    def get_alcohol_percentage(self):
        self._get_warning_message()
        return self.alcohol_percentage

    def get_type(self):
        return "Alcoholic"


class NonAlcoholicDrink(Drinks):
    def __init__(self, name, ingredients, sugar_spoons):
        super().__init__(name, ingredients)
        self.sugar_spoons = sugar_spoons

    def get_sugar_spoons(self):
        return self.sugar_spoons

    def get_type(self):
        return "Non alcoholic"


drink_kind = input("Is the drink alcoholic or non alcoholic? (a/n): ").strip().lower()
drink_name = input("Enter the name of the drink: ").strip()

num_ingredients = int(input("How many ingredients would you like to add? ").strip())
ingredients = []
for _ in range(num_ingredients):
    ingredients.append(input("Enter ingredient: ").strip())

drink = None

if drink_kind == "a":
    alcohol_percentage = int(input("Enter the percentage of alcohol (1-100): ").strip())
    while alcohol_percentage < 1 or alcohol_percentage > 100:
        alcohol_percentage = int(input("Enter the percentage of alcohol (1-100): ").strip())
    drink = AlcoholicDrink(drink_name, ingredients, alcohol_percentage)
else:
    sugar_spoons = int(input("Enter the number of spoons of sugar: ").strip())
    drink = NonAlcoholicDrink(drink_name, ingredients, sugar_spoons)

print("The drink has been created.")
print("Name: " + drink.get_name())
print("Type: " + drink.get_type())
print("Ingredients:")
for ing in drink.get_ingredients():
    print(ing)

if isinstance(drink, AlcoholicDrink):
    print("Alcohol Percentage: " + str(drink.get_alcohol_percentage()) + "%")
else:
    print("Sugar Spoons: " + str(drink.get_sugar_spoons()))
