class Inventory:
    """Manage product stock and inventory value."""
    def __init__(self):
        self.products = {}
        
    def add_product(self, sku, quantity, price):
        if not sku:
            raise ValueError("SKU cannot be empty")
        if quantity < 0:
            raise ValueError("Quantity cannot b e negative")
        if price < 0:
            raise ValueError("Price Cannot be negative")
        
        if sku in self.products:
            self.products[sku]["quantity"] += quantity
            self.products[sku]["price"] = price
            
        else:
            self.products[sku] = {
                "quantity": quantity,
                "price" : price
            }
    def remove_product(self, sku, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if sku not in self.products:
            raise KeyError("Product not found")
        if quantity > self.products[sku]["quantity"]:
            raise ValueError("Insufficient stock")
        
        self.products[sku]["quantity"] -= quantity
        
    def get_stock(self, sku):
        if sku not in self.products:
            raise KeyError("Product not found")
        return self.products[sku]["quantity"]
    
    def total_value(self):
        return sum(
            item["quantity"] * item["price"]
            for item in self.products.values()
        )