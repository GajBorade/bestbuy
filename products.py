class Product:
    """Represents a product available in the store."""

    def __init__(self, name, price, quantity, active=True):
        """Initialize product with name, price, quantity, and active status."""
        if not isinstance(name, str):
            raise TypeError("Name should be of type string")
        elif not name.strip():
            raise ValueError("Name can not be empty, enter a name of the product")
        self.name = name.strip()


        if not isinstance(price, (float, int)):
            raise TypeError("Price should be of type float or int.")
        elif price < 0:
            raise ValueError(
                "Price can not be less than zero. Enter valid price e.g., 1450 or 1399.99"
            )
        self.price = float(price)


        if not isinstance(quantity, int):
            raise TypeError("Quantity should be of type int.")
        elif quantity < 0:
            raise ValueError(
                "Quantity can not be less than zero. Enter valid quantity e.g., positive integers"
            )
        self.quantity = quantity

        self.active = active


    def get_quantity(self):
        """Return the current stock quantity."""
        return self.quantity


    def set_quantity(self, quantity):
        """Update quantity; deactivate if zero; raise if negative."""
        if quantity < 0:
            raise ValueError(
                "Quantity can not be less than zero. Enter valid quantity e.g., positive integers"
            )
        if quantity == 0:
            print("The product is deactivated!")
            self.active = False
        self.quantity = quantity


    def is_active(self):
        """Return True if product is active, otherwise False."""
        return self.active


    def activate(self):
        """Set the product as active."""
        self.active = True


    def deactivate(self):
        """Set the product as inactive."""
        self.active = False


    def show(self):
        """Print product details."""
        print(f"{self.name}, Price:{self.price}, Quantity:{self.quantity}")


    def buy(self, quantity):
        """Purchase given quantity; return total price; raise if insufficient stock."""
        if quantity > self.quantity:
            raise ValueError(
                f"This quantity can not be delivered. Best buy has only {self.quantity}"
            )
        total_price = self.price * quantity
        self.quantity = self.quantity - quantity
        return total_price
