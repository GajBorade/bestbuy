import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


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
                    products = best_buy.get_all_products()
                    print("------")
                    for index, product in enumerate(products, start=1):
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
                    exit()
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
    - Checks stock availability
    - Prints running total after each selection
    """
    print("------")
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        user_interaction = input("\nWhich product # do you want?").strip()
        if not user_interaction:
            break

        try:
            user_choice_number = int(user_interaction)
            if 1 <= user_choice_number <= len(products_list):
                product_selected = products_list[user_choice_number - 1]

                units_input = int(input("How many units do you want?").strip())
                if 0 < units_input <= product_selected.get_quantity():
                    shopping_list.append((product_selected, units_input))
                    total_price = best_buy.order(shopping_list)
                    print(f"\nRunning total: ${total_price}")
                else:
                    print(
                        "Sorry, out of stock, try again in the next days."
                        "\nMeanwhile check out the other available products"
                    )
            else:
                print("Invalid product number, try again.")

        except ValueError:
            print("Invalid input, please enter a valid number.")

    if shopping_list:
        final_total = best_buy.order(shopping_list)
        print(f"\nOrder completed! Total payment: ${final_total}")
    else:
        print("No products were selected.")


if __name__ == "__main__":
    start(best_buy)
