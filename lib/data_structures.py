spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

spicy_names = []
def get_names(spicy_foods):
    for food in spicy_foods:
        spicy_names.append(food["name"])
    return spicy_names

spiciest_list = []
def get_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_list.append(food)
    return spiciest_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: " + "🌶"*food["heat_level"])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: " + "🌶"*food["heat_level"])

def get_average_heat_level(spicy_foods):
    food_heat_list=[]
    for food in spicy_foods:
        food_heat_list.append(food["heat_level"])
    heat_list_total = sum(food_heat_list)
    return heat_list_total/len(food_heat_list)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods