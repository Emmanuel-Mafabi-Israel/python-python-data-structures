# GLORY BE TO GOD,
# RUNNING PYTHON CODE, 
# CREATING A PYTHON APPLICATION - PYTHON DATA STRUCTURES,
# BY ISRAEL MAFABI EMMANUEL

chilly:str = "🌶"

spicy_food:dict = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

spicy_foods:list = [
    {
        "name"      : "Green Curry",
        "cuisine"   : "Thai",
        "heat_level": 9,
    },
    {
        "name"      : "Buffalo Wings",
        "cuisine"   : "American",
        "heat_level": 3,
    },
    {
        "name"      : "Mapo Tofu",
        "cuisine"   : "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods:list)->list:
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods:list)->list:
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods:list):
    for food in spicy_foods:
        print(f"{food["name"]} ({food["cuisine"]}) | Heat Level: {chilly * food["heat_level"]}")

def get_spicy_food_by_cuisine(spicy_foods:list, cuisine:str)->dict:
    result:dict = {}
    for food in spicy_foods:
        if food["cuisine"].upper() == cuisine.upper():
            result = food

    return result


def print_spiciest_foods(spicy_foods:list):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food["name"]} ({food["cuisine"]}) | Heat Level: {chilly * food["heat_level"]}")

def get_average_heat_level(spicy_foods:list)->float:
    totals:int = 0
    for food in spicy_foods:
        totals += food["heat_level"]

    average:float = totals / len(spicy_foods)
    return round(average)


def create_spicy_food(spicy_foods:list, spicy_food:dict)->list:
    spicy_foods.append(spicy_food)
    return spicy_foods

print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
print_spiciest_foods(spicy_foods)
print(get_average_heat_level(spicy_foods))
print(create_spicy_food(spicy_foods, spicy_food))