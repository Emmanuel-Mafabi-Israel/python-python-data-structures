# CREATING A PYTHON APPLICATION - PYTHON DATA STRUCTURES
# BY ISRAEL MAFABI EMMANUEL

Welcome to this demonstration of Python data structures! In this example, we will explore various data structures in Python by creating a program that works with a list of spicy foods.

## Spicy Foods Example

This Python application includes functions to handle and process data related to spicy foods. We will use a list of dictionaries to store information about different spicy foods and perform operations on this data.

### Data Structures

Below are the Python variables and functions for this application:

```python
chilly: str = "🌶"

spicy_food: dict = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

spicy_foods: list = [
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

def get_names(spicy_foods: list) -> list:
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods: list) -> list:
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods: list):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {chilly * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods: list, cuisine: str) -> dict:
    result: dict = {}
    for food in spicy_foods:
        if food["cuisine"].upper() == cuisine.upper():
            result = food
    return result

def print_spiciest_foods(spicy_foods: list):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {chilly * food["heat_level"]}')

def get_average_heat_level(spicy_foods: list) -> float:
    totals: int = 0
    for food in spicy_foods:
        totals += food["heat_level"]
    average: float = totals / len(spicy_foods)
    return round(average)

def create_spicy_food(spicy_foods: list, spicy_food: dict) -> list:
    spicy_foods.append(spicy_food)
    return spicy_foods
```

### Explanation

- `get_names(spicy_foods: list) -> list`:
  - Returns a list of the names of the spicy foods.
- `get_spiciest_foods(spicy_foods: list) -> list`:
  - Returns a list of spicy foods with a heat level greater than 5.
- `print_spicy_foods(spicy_foods: list)`:
  - Prints each spicy food's name, cuisine, and heat level using the chili pepper emoji.
- `get_spicy_food_by_cuisine(spicy_foods: list, cuisine: str) -> dict`:
  - Returns a single spicy food dictionary that matches the specified cuisine.
- `print_spiciest_foods(spicy_foods: list)`:
  - Prints only the spiciest foods (heat level greater than 5).
- `get_average_heat_level(spicy_foods: list) -> float`:
  - Returns the average heat level of the spicy foods rounded to the nearest whole number.
- `create_spicy_food(spicy_foods: list, spicy_food: dict) -> list`:
  - Adds a new spicy food to the list and returns the updated list.

### Usage

To use these functions, simply call them with the appropriate arguments as shown in the code. For example, to print all the spicy foods:

```python
print_spicy_foods(spicy_foods)
```

Or to get the average heat level of the spicy foods:

```python
print(get_average_heat_level(spicy_foods))
```

### Example Output

Here's an example of what you might see when running the functions:

```python
print(get_names(spicy_foods))
# Output: ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

print(get_spiciest_foods(spicy_foods))
# Output: [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]

print_spicy_foods(spicy_foods)
# Output:
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
```

## Conclusion

This test demonstrates the use of Python Data Structures to manage and process data about spicy foods. 

~ Glory be to God!!!

Happy coding! 😍😉🤭