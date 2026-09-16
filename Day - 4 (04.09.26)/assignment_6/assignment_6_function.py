def add_to_cart(cart, products, product_id, quantity):
    if quantity <= 0:
        raise ValueError("Quantity should be positive")
    found = False
    for product in products:
        if product["id"] == product_id:
            cart_item = {
                "product": product,
                "quantity": quantity
            }
            cart.append(cart_item)
            found = True
            break
    if not found:
        raise ValueError("Product not found")

def remove_from_cart(cart, product_id):
    for item in cart:
        if item["product"]["id"] == product_id:
            cart.remove(item)
            return
    raise ValueError("Product is not in the cart")

def calculate_subtotal(cart):
    subtotal = 0
    for item in cart:
        item_total = item["product"]["price"] * item["quantity"]
        subtotal += item_total
    return subtotal

def calculate_discount(cart):
    subtotal = calculate_subtotal(cart)
    if subtotal >= 5000:
        discount = subtotal * 0.25
    elif subtotal >= 2000:
        discount = subtotal * 0.15
    else:
        discount = 0
    return discount

def calculate_tax(cart):
    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(cart)
    tax = (subtotal - discount) * 0.18
    return tax

def calculate_final_amount(cart):
    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(cart)
    tax = calculate_tax(cart)
    final_amount = subtotal - discount + tax
    return final_amount

products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 1200},
    {"id": 3, "name": "Keyboard", "price": 2500}
]

cart = []

try:
    add_to_cart(cart, products, 1, 1)
    add_to_cart(cart, products, 2, 2)
    print(f"Subtotal: {calculate_subtotal(cart)}")
    print(f"Discount: {calculate_discount(cart)}")
    print(f"Tax: {calculate_tax(cart)}")
    print(f"Final Amount: {calculate_final_amount(cart)}")
except ValueError as e:
    print(e)