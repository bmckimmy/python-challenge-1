# Menu dictionary
menu = {
    "Fruits": {
        "Apple": 1.00,
        "Banana": 0.50,
        "Orange": 1.00,
        "Pear": 1.25,
        "Kiwi": 1.50,
        "Pineapple": 1.75,
        "Grapefruit": 1.00
    },
    "Drinks": {
        "Juice": {
            "Small": 0.99,
            "Medium": 1.99,
            "Large": 2.99
        }
    },
    "Dessert": {
        "Pie": {
            "Apple": 1.99,
            "Banana Cream": 2.99,
        },
        "Ice Cream": {
            "Vanilla": 1.99,
            "Chocolate": 2.99,
        },
    }
}

# Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Hello! Welcome to Fruit Paradise!")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("What would you like to order ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_selection = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():
            # Save the menu category name to a variable
            menu_selection_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            print(f"You selected {menu_selection_name}")

            # Print out the menu options from the menu_selection_name
            print(f"What {menu_selection_name} item would you like to order?")
            i = 1
            menu_items_dict = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_selection_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items_dict[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items_dict[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # Ask customer to input menu item number
            menu_item = input("What item number do you want? ")

            # Check if the customer typed a number
            if menu_item.isdigit():
                # Convert the menu selection to an integer
                menu_item = int(menu_item)
              
                # Check if the menu selection is in the menu items
                if menu_item in menu_items_dict.keys():

                    # Store the item name and price as variables
                    food_item = menu_items_dict[menu_item]['Item name']
                    item_price = menu_items_dict[menu_item]['Price']               
                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {food_item}s do you want? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else: 
                        print("Invalid input for quantity. Defaulting to 1.")
                        quantity = 1
                    # Add the item name, price, and quantity to the order list
                    order_list.append({'Item name': food_item, 'Price': item_price, 'Quantity': quantity})
                else:
                    print("Your input is invalid. Please enter a valid item number.")
            else:
                # Tell the customer they didn't select a number
                print("You didn't select a valid item number.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        keep_ordering = keep_ordering.lower()
        # Check the customer's input
        match keep_ordering:
            case 'y':
                place_order = True
                break
            case 'n':
                place_order = False
                print("\nThank you very much for visiting the veriety food truck!")
                break          
            # Tell the customer to try again
            case _: 
                print("\nPlease Try again")

# Print out the customer's order
print("This is what we are preparing for you.\n")

print("Item Name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the items in the customer's order and print them
for order_item in order_list:
    # Store the dictionary items as variables
    item_name, price, quantity = order_item['Item name'], order_item['Price'], order_item['Quantity']

    # Calculate the number of spaces for formatted printing
    item_space_str_len = 30 - len(item_name)
    price_space_str_len = 10 - len(str(price))
    # Create space strings
    item_spaces = " " * item_space_str_len
    price_spaces = " " * price_space_str_len
    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| {price:.2f}{price_spaces}| {quantity}")

# Calculate the total cost of the order using list comprehension
total_cost = sum([item['Price'] * item['Quantity'] for item in order_list])
# Print the total cost of the order
print(f"Total cost of the order: ${total_cost:.2f}")