class ProductNotFoundError(Exception):
    pass

class InvalidStockError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

class Inventory:
    def __init__(self):
        self.inventory = {
            "laptop": 10,
            "mouse": 50,
            "keyboard": 25
        }

    def add_product(self, product, quantity):
        if quantity < 0:
            raise InvalidStockError("Cannot be -ve")
        self.inventory[product] = quantity
        
    def remove_product(self, product):
        if product not in self.inventory:
            raise ProductNotFoundError("Product not found")
        del self.inventory[product]

    def sell_product(self, product, quantity):
        if product not in self.inventory:
            raise ProductNotFoundError("Product not found")
        if quantity <= 0:
            raise InvalidStockError("Quantity must be +ve")
        if quantity > self.inventory[product]:
            raise InsufficientStockError("Not enough stock")
        self.inventory[product] -= quantity

    def restock_product(self, product, quantity):
        if product not in self.inventory:
            raise ProductNotFoundError("Product not found")
        if quantity <= 0:
            raise InvalidStockError("Quantity should be positive")
        self.inventory[product] += quantity

    def check_stock(self, product):
        if product not in self.inventory:
            raise ProductNotFoundError("Product not found")
        return self.inventory[product]
        
# object
inventory = Inventory()

try:
    inventory.add_product("monitor", 15)
    print("Monitor:", inventory.check_stock("monitor"))
    inventory.sell_product("laptop", 3)
    print("Laptop:", inventory.check_stock("laptop"))
    inventory.restock_product("mouse", 20)
    print("Mouse:", inventory.check_stock("mouse"))
    inventory.remove_product("keyboard")
    print("Final:", inventory.inventory)

except ProductNotFoundError as e:
    print(e)

except InvalidStockError as e:
    print(e)

except InsufficientStockError as e:
    print(e)        