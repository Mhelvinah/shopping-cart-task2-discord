# Item details with color
items = {
    "Shoes": {"size": 38, "color": "Brown", "price": 5000},
    "Headphones": {"color": "Silver", "brand": "JBL", "price": 10000},
    "Laptop": {"color": "Black", "brand": "Samsung", "price": 30000},
    "Bag": {"color": "Blue", "brand": "Gucci", "price": 1000},
    "mobile phone": {"color": "rainbow", "brand":"Itel", "price": 15000}
}

# Discount rate
discount_rate = 0.20

# Initializing variables
total_price = 0

def add_to_cart(item_name, quantity, *args, **kwargs):
    """Add the selected item to the cart with discount applied."""
    if item_name in items:
        price = items[item_name]["price"]
        item_total = price * quantity
        discounted_price = item_total * (1 - discount_rate)
        return discounted_price
    else:
        return 0

# Welcome message
print("\nWelcome to our shopping cart! 🛒")

# Loop for item selection
while True:
    item_name = input("\nEnter item name (or 'done' to finish): ").strip()

    if item_name.lower() == 'done':
        break

    # Normalize input to lowercase for matching
    normalized_item_name = None
    for item in items:
        if item_name.lower() == item.lower():  # Compare lowercased versions
            normalized_item_name = item  # Store the correctly capitalized name
            break

    if normalized_item_name:
        # Display item size and color
        size = items[normalized_item_name].get("size", "Size not available")
        color = items[normalized_item_name].get("color", "Color not available")
        print(f"\nSize: {size}, Color: {color}")
        quantity = int(input(f"\nEnter quantity for {normalized_item_name}: "))
        discounted_price = add_to_cart(normalized_item_name, quantity)
        if discounted_price > 0:
            total_price += discounted_price
            print(f"Added {normalized_item_name} (x{quantity}) to cart. Total after discount: ${discounted_price:.2f}")
    else:
        print("\nInvalid item. Please try again.")

# Final total
print(f"\nTotal price for all items: ${total_price:.2f}")

# Thanks message
print("\nThank you for shopping with us! Have a wonderful day!")
