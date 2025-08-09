class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.__products = []  # เก็บสินค้าแบบ private list

    def add_product(self, name, quantity):
        new_product = Product(name, quantity)  # สร้างสินค้าใหม่
        self.__products.append(new_product)    # เพิ่มเข้าไปใน list

    def show_products(self):
        for product in self.__products:
            print(f"สินค้า: {product.name}, จำนวน: {product.quantity}")

# --- ตัวอย่างการทดสอบโปรแกรม ---
my_store = Store()
my_store.add_product("Laptop", 15)
my_store.add_product("Mouse", 50)
my_store.show_products()
