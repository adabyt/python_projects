# Menu with items and their prices
menu = {"popcorn": 5.00, "nachos": 3.50, "sweets": 2.00, "soda": 2.50, "water": 0.00}


def display_menu():
    """
    Display the menu items and their prices in a formatted manner.
    """
    print("-------- MENU --------")
    for item, price in menu.items():
        print(f"{item.title():7}: £{price:.2f}")
    print("----------------------\n")


def take_order():
    """
    Take user orders by repeatedly prompting for menu items.
    Users can enter 'q' to finish ordering.
    Returns:
        list: List of ordered items.
    """
    cart = []
    while True:
        food = input("Select an item (q to quit): ").lower()
        if food == "q":
            break
        elif food in menu:
            cart.append(food)
        else:
            print("Sorry, that item is not on the menu.")
    return cart


def summarize_order(cart):
    """
    Summarize the ordered items, showing counts, subtotal per item,
    and total order cost.

    Args:
        cart (list): List of ordered items.
    """
    print("\n~~~~~ YOUR ORDER ~~~~~")
    total = 0
    item_counts = {}

    # Count quantities of each item and calculate total cost
    for food in cart:
        item_counts[food] = item_counts.get(food, 0) + 1
        total += menu[food]

    # Display each item, quantity, and price subtotal
    for item, count in item_counts.items():
        price = menu[item] * count
        print(f"{item.title():7} x{count} = £{price:.2f}")

    print("----------------------")
    print(f"Order total: £{total:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~")


def main():
    """
    Run the concession stand program by displaying the menu,
    taking orders, and summarizing the final order.
    """
    display_menu()
    cart = take_order()
    summarize_order(cart)


if __name__ == "__main__":
    main()
