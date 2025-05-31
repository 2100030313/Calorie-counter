# A simple dict for demo; you can expand this or link to an AI model
food_calories = {
    'apple': 95,
    'banana': 105,
    'orange': 62,
    'rice': 206,
    'bread': 79,
    'egg': 78
}

def estimate_calories(food):
    food = food.lower().strip()
    return food_calories.get(food, "Unknown")