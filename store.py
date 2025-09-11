class Store:
    """
    Represents a store that manages a list of products.
    Attributes:
        products_list (list): List of Product instances in the store.
    """
    def __init__(self, products_list):
        """
        Initialize the store with a list of products.
        Parameters:
            products_list (list): List of Product instances.
        """
        self.products_list = products_list


    def add_product(self, product):
        """
        Add a product to the store's inventory.
        Parameters:
            product (Product): The product instance to add.
        """
        self.products_list.append(product)


    def remove_product(self, product):
        """
        Remove a product from the store's inventory if it exists.
        Parameters:
            product (Product): The product instance to remove.
        """
        if product in self.products_list:
            self.products_list.remove(product)


    def get_total_quantity(self):
        """
        Calculate the total quantity of all products in the store.
        Returns:
            int: Sum of quantities of all products.
        """
        total_quantity = 0
        for product in self.products_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """
        Get all active products in the store.
        Returns:
            list: List of active Product instances.
        """
        active_products_list = []
        for product in self.products_list:
            if product.is_active():
                active_products_list.append(product)
        return active_products_list


    def order(self, shopping_list):
        """
        Process an order of products and return the total price.
        Parameters:
            shopping_list (list of tuples): Each tuple contains a Product instance and
                                            an integer quantity to buy.
        Returns:
            float: Total price of the ordered products.
        """
        total_price = 0
        for product, quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price
        return total_price
