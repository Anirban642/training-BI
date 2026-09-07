class ProductNotFoundError(Exception):
    pass

class InvalidStockError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

def add_product(inventory, product, quantity):
    if quantity < 0:
        raise InvalidStockError("Cannot be negative")
    inventory[product] = quantity

def remove_product(inventory, product):
    if product not in inventory:
        raise ProductNotFoundError("Product not found")
    del inventory[product]

def sell_product(inventory, product, quantity):
    if product not in inventory:
        raise ProductNotFoundError("Product not found")
    if quantity <= 0:
        raise InvalidStockError("Quantity must be positive")
    if quantity > inventory[product]:
        raise InsufficientStockError("Not enough stock")
    inventory[product] -= quantity

def restock_product(inventory, product, quantity):
    if product not in inventory:
        raise ProductNotFoundError("Product not found")
    if quantity <= 0:
        raise InvalidStockError("Quantity should be positive")
    inventory[product] += quantity

def check_stock(inventory, product):
    if product not in inventory:
        raise ProductNotFoundError("Product not found")
    return inventory[product]

inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 25
}

try:
    add_product(inventory, "monitor", 15)
    print("Monitor:", check_stock(inventory, "monitor"))
    sell_product(inventory, "laptop", 3)
    print("Laptop:", check_stock(inventory, "laptop"))
    restock_product(inventory, "mouse", 20)
    print("Mouse:", check_stock(inventory, "mouse"))
    remove_product(inventory, "keyboard")
    print("Final inventory:", inventory)
except ProductNotFoundError as e:
    print(e)
except InvalidStockError as e:
    print(e)
except InsufficientStockError as e:
    print(e)