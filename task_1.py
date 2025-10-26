class Product:
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


    def update_stock(self, quantity):
        if self.stock + quantity < 0:
            print(f"Error! Not enough {self.name} in shop")
        else:
            self.stock += quantity
    
    def __str__(self):
        return f"{self.name} for price {self.price} rub. (in stock: {self.stock})"
    

class Order:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            print("Error! quantity must be greater then 0")
            return
        
        if product.stock < quantity:
            print(f"Error! Not enough {product.name} in stock")
            return
        
        product.update_stock(-quantity)

        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.products.items())
        return total
    
    def __str__(self):
        items = ''.join([f"{prod.name} x {qnty} |" for prod, qnty in self.products.items()])

        return f"Order:\n {items} \n Total sum: {self.calculate_total()} rub."
    

class Store:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
    
    def list_products(self):
        if not self.products:
            print("No items in store")
            return
        for product in self.products:
            print(product)
    
    def create_order(self):
        return Order()
    


store = Store()
p1 = Product("Laptop", 40000, 3)
p2 = Product("Phone", 10000, 10)

store.add_product(p1)
store.add_product(p2)

store.list_products()

order = store.create_order()
order.add_product(p1,3)
order. add_product(p2,1)

print(order)

store.list_products()

order1 = store.create_order()
order1.add_product(p1,1)
print(order1)