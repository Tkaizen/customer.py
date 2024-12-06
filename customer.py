class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Shop:
    def __init__(self):
        self.products = [
            Product(1, "T-shirt", 20),
            Product(2, "Jeans", 40),
            Product(3, "Cap", 15),
            Product(4, "Sneakers", 60)
        ]
        self.cart = {}

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products:
            print(f"{product.product_id}. {product}")

    def add_to_cart(self, product_id, quantity):
        # Check if the product exists
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            if product_id in self.cart:
                self.cart[product_id] += quantity
            else:
                self.cart[product_id] = quantity
            print(f"{quantity} {product.name}(s) added to your cart.")
        else:
            print("Product not found.")

    def view_cart(self):
