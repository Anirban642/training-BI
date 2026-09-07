class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []
    def add_to_cart(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("Quantity should be positive")
        found = False
        for product in products:
            if product.id == product_id:
                cart_item = {
                    "product": product,
                    "quantity": quantity
                }
                self.cart.append(cart_item)
                found = True
                break
        if not found:
            raise ValueError("Product not found")

    def remove_from_cart(self, product_id):
        for item in self.cart:
            if item["product"].id == product_id:
                self.cart.remove(item)
                return
        raise ValueError("Product is not in the cart")

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.cart:
            item_total = item["product"].price * item["quantity"]
            subtotal += item_total
        return subtotal

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        if subtotal >= 5000:
            discount = subtotal * 0.25
        elif subtotal >= 2000:
            discount = subtotal * 0.15
        else:
            discount = 0
        return discount

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = (subtotal - discount) * 0.18
        return tax

    def calculate_final_amount(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        final_amount = subtotal - discount + tax
        return final_amount

# Products
products = [
    Product(1, "Laptop", 70000),
    Product(2, "Mouse", 1200),
    Product(3, "Keyboard", 2500)
]

cart = ShoppingCart()

# Use the cart
try:
    cart.add_to_cart(1, 1)
    cart.add_to_cart(2, 2)

    print(f"Subtotal: {cart.calculate_subtotal()}")
    print(f"Discount: {cart.calculate_discount()}")
    print(f"Tax: {cart.calculate_tax()}")
    print(f"Final Amount: {cart.calculate_final_amount()}")

except ValueError as e:
    print(e)