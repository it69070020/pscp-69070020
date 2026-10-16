"""THIS IS WHAT PAD THAI SHOULD TASTE LIKE FUIYOHHHHHH"""
def main():
    """yume kibou wa shoumikigen ga aru no yo"""
    ingredients = {"Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"}
    taste = {"Sweet", "Sour", "Salty"}
    used = set()
    ingredients_used = input()
    while ingredients_used != "Cook":
        used.add(ingredients_used)
        ingredients_used = input()

    food_taste = set()
    actual_taste = input()
    while actual_taste != "End":
        food_taste.add(actual_taste)
        actual_taste = input()
    if not used <= ingredients:
        print("This is not Pad Thai!!!")
    elif used != ingredients:
        print("This is bad!")
    elif food_taste == taste:
        print("Delicious!")
    else:
        print("Not Bad...")
main()
