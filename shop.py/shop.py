#Colors
GREEN = "\033[92m"
RESET = "\033[0m"
CYAN ='\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[34m'

# Define shops with their items
shops = {
    "Kwa Jay shop": {
        "Unga": 130,
        "mchele": 100,
        "maharagwe": 70,
        "mkate": 60,
        "mayai": 15,
        "doughnuts": 10
    },
    "Aboo wholesale": {
        "unga": 130,
        "mchele": 100,
        "maharagwe": 70,
        "mkate": 60,
        "perememde":10,
        "doughnuts": 10
    }
}

# Ask user for items they want to buy
user_input = input("Enter the items you want to buy (comma separated): ").lower()

# Convert input into a list and strip spaces
items_to_buy = [item.strip() for item in user_input.split(",")]

# Loop through each shop and check availability
for shop_name, shop_items in shops.items():
    available_items = {}
    unavailable_items = []

    for item in items_to_buy:
        if item in shop_items:
            available_items[item] = shop_items[item]
        else:
            unavailable_items.append(item)

    # Show results per shop
    print(f"\n--- {CYAN}{shop_name} Shopping Summary --- {RESET}")
    print(f"{BLUE}Available items:{RESET}")
    if available_items:
        for item, price in available_items.items():
            print(f"- {YELLOW}{item.capitalize()} {RESET}: {CYAN}{price}{RESET}")
    else:
        print("None")

    print(f"\n{BLUE}Unavailable items:{RESET}")
    if unavailable_items:
        for item in unavailable_items:
            print(f"-{RED} {item.capitalize()}{RESET}")
    else:
        print("None")

    # Calculate total price
    total_price = sum(available_items.values())
    print(f"{BLUE}\nTotal Price of Available Items in {shop_name}:{RESET} {GREEN}{total_price}{RESET}")
    print("----------------------------------------------------------")
