"""Pad Thai"""
def main():
    """Check Pad Thai ingredients and taste"""
    ingredients = {
        "Pad Thai Sauce",
        "Tofu",
        "Pickle Turnip",
        "Shrimp",
        "Bean Sprouts",
        "Noodle",
        "Chives",
        "Lime",
        "Egg",
        "Oil",
        "Peanuts"
    }
    tastes_required = {"Sweet", "Sour", "Salty"}
    used = set()
    bad_ingredient = False
    while True:
        food = input()

        if food == "Cook":
            break
        used.add(food)

        if food not in ingredients:
            bad_ingredient = True
    tastes = set()
    while True:
        taste = input()

        if taste == "End":
            break
        tastes.add(taste)
    if bad_ingredient:
        print("This is not Pad Thai!!!")
    elif len(used) < len(ingredients):
        print("This is bad!")
    elif tastes == tastes_required:
        print("Delicious!")
    else:
        print("Not Bad...")
main()
