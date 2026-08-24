class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def remove_product(self, product_id):
        for product in self.items:

            if product.product_id == product_id:
                self.items.remove(product)
                print("Product removed.")
                return

        print("Product not found.")

    def calculate_total(self):
        return sum(product.price for product in self.items)

    def display_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n--- Shopping Cart ---")

        for product in self.items:
            print(
                f"{product.product_id} | "
                f"{product.name} | "
                f"₹{product.price:.2f}"
            )

        print("---------------------")
        print(f"Total: ₹{self.calculate_total():.2f}")


cart = ShoppingCart()

while True:

    print("\n1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product_id = input("Product ID: ")
        name = input("Product name: ")
        price = float(input("Product price: "))

        product = Product(product_id, name, price)
        cart.add_product(product)

    elif choice == "2":
        cart.display_cart()

    elif choice == "3":
        product_id = input("Enter product ID: ")
        cart.remove_product(product_id)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")