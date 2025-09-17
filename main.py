import sys
import products
import store


def main():
    """
    Setup initial stock of inventory for the Best Buy store and start
    the application.

    This section creates Product instances for the store and adds them
    to the store's inventory. Each product has a name, price, and quantity.

    After setting up the inventory, the start() function is called
    to begin the interactive store menu for the user.
    """
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    store_instance = store.Store(product_list)
    start(store_instance)


def start(best_buy):
    """
    This function shows the menu options to the user.
    It prints a list of available actions, guiding the user
    on how to interact with best-buy.

    The function continuously prompts the user until they choose to quit.

    Parameters:
        best_buy (Store): An instance of the Store class representing the inventory.

    Returns:
        None
    """
    while True:
        print(
            "\nStore Menu:\n"
            "1.  List all products in the store\n"
            "2.  Show total amount in store\n"
            "3.  Make an order\n"
            "4.  Quit\n"
        )

        user_action = input("Please select a number of your choice:").strip()
        try:
            user_choice = int(user_action)
            if 1 <= user_choice <= 4:
                if user_choice == 1:
                    all_products = best_buy.get_all_products()
                    print("------")
                    for index, product in enumerate(all_products, start=1):
                        print(f"{index}. ", end="")
                        product.show()
                    print("------")

                elif user_choice == 2:
                    print(f"\nTotal of {best_buy.get_total_quantity()} items in store")

                elif user_choice == 3:
                    products_list = best_buy.get_all_products()
                    take_order(best_buy, products_list)

                elif user_choice == 4:
                    print("Thank you for visiting best buy, See you again. Bye!")
                    sys.exit()
            else:
                print(
                    "Invalid entry! User action should be an integer between 1 and 4."
                )

        except ValueError:
            print("Invalid entry! User_choice should be of type int.")


def take_order(best_buy, products_list):
    """
    Handles the user order process:
    - Shows products with numbering
    - Lets user select product numbers and quantity
    - Checks stock availability and deactivated status
    - Updates quantities immediately
    - Prints running total after each selection
    - Prints final total once at the end before returning to menu
    """
    print("------")
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("------")
    print("When you want to finish order, enter empty text.")

    running_total = 0

    while True:
        user_interaction = input("\nWhich product # do you want?").strip()
        if not user_interaction:
            break

        try:
            user_choice_number = int(user_interaction)
            if 1 <= user_choice_number <= len(products_list):
                product_selected = products_list[user_choice_number - 1]

                if not product_selected.is_active():
                    print("Sorry, this product is deactivated and cannot be purchased.")
                    continue

                units_input = int(input("How many units do you want?").strip())
                if 0 < units_input <= product_selected.get_quantity():
                    # Buy immediately and update product quantity
                    total_price_for_units = product_selected.buy(units_input)
                    running_total += total_price_for_units
                    print(f"Running total: ${running_total:.2f}")
                else:
                    print(
                        "Sorry, not enough stock for this quantity.\n"
                        "Please choose a lower quantity or another product."
                    )
            else:
                print("Invalid product number, try again.")

        except ValueError:
            print("Invalid input, please enter a valid number.")

    print(f"\nOrder completed! Total payment: ${running_total:.2f}")


if __name__ == "__main__":
    main()
