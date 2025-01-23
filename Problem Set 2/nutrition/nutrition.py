x = input("Item: ").strip().lower()
d = {
    "apple": "130",
    "banana":"110",
    "avocado": "50",
    "cantaloupe":"50",
    "grapefruit":"60",
    "grapes":"90",
    "honeydew Melon":"50",
    "kiwifruit":"90",
    "lemon":"15",
    "lime":"20",
    "nectarine":"60",
    "orange":"80",
    "pear":"100",
    "peach":"60",
    "pineapple":"50",
    "plums":"70",
    "srawberries":"50",
    "sweet cherries":"100",
    "tangerine":"50",
    "watermelon":"80",
}

if x in d:
    print("Calories:", d[x])
else:
    print("\n")
