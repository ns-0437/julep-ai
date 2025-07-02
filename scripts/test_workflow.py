import json
import random
import os

# Load cities
with open("../data/cities.json") as f:
    cities = json.load(f)["cities"]

# Mock functions
def get_weather(city):
    return random.choice(["sunny", "rainy", "cloudy"])

def get_dining_type(weather):
    return "outdoor" if weather == "sunny" else "indoor"

def get_dishes(city):
    dishes = {
        "Paris": ["Croissant", "Coq au Vin", "Ratatouille"],
        "Tokyo": ["Sushi", "Ramen", "Okonomiyaki"],
        "New York": ["Bagel", "Pastrami Sandwich", "Cheesecake"]
    }
    return dishes.get(city, ["Dish1", "Dish2", "Dish3"])

def get_restaurants(city, dish):
    return f"{dish} House in {city}"

def generate_tour(city, weather, dishes, restaurants):
    return f"""
--- {city} Foodie Tour ({weather}) ---

- Breakfast: {dishes[0]} at {restaurants[0]}
- Lunch: {dishes[1]} at {restaurants[1]}
- Dinner: {dishes[2]} at {restaurants[2]}

Recommended for: {'outdoor' if weather == 'sunny' else 'indoor'} dining
"""

# Create outputs directory if not exists
output_dir = "../outputs"
os.makedirs(output_dir, exist_ok=True)

# Process each city
for city in cities:
    weather = get_weather(city)
    dishes = get_dishes(city)
    restaurants = [get_restaurants(city, dish) for dish in dishes]
    tour = generate_tour(city, weather, dishes, restaurants)

    with open(f"{output_dir}/{city.lower().replace(' ', '_')}_tour.txt", "w") as f:
        f.write(tour)
