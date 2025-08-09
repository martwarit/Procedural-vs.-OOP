class OnlineShop:
    def __init__(self, name, url):
        self.__name = name
        self.__url = url
        self.__products = []

    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def addingItemsToCart(self, customer, product, quantity):
        customer.add_to_cart(product, quantity)

    def checkOut(self, customer):
        cart = customer.get_cart()
        if not cart:
            print("Cart is empty.")
            return
        
        total_price = 0
        items = []

        for item in cart:
            product = item['product']
            quantity = item['quantity']
            total = product.get_price() * quantity
            total_price += total
            items.append({
                "product_name": product.get_name(),
                "quantity": quantity,
                "unit_price": product.get_price(),
                "total": total
            })

        order_id = "001"
        order_summary = {
            "order_id": order_id,
            "items": items,
            "total_price": total_price
        }

        customer.add_past_order(order_summary)
        customer.clear_cart()
        print(f"Order placed successfully. Order ID: {order_id}")
        return order_summary

    def orderTracking(self, customer, order_id):
        past_orders = customer.get_past_orders()
        for order in past_orders:
            if order["order_id"] == order_id:
                return order
        return "Order not found."


class Product:
    def __init__(self, name, description, price, online_shop):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__online_shop = online_shop
        self.__online_shop.add_product(self)

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_online_shop(self):
        return self.__online_shop


class Customer:
    def __init__(self, name, email, address):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__cart = []
        self.__past_orders = []

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_cart(self):
        return self.__cart

    def get_past_orders(self):
        return self.__past_orders

    def add_to_cart(self, product, quantity):
        self.__cart.append({"product": product, "quantity": quantity})

    def add_past_order(self, order):
        self.__past_orders.append(order)

    def clear_cart(self):
        self.__cart = []

shop = OnlineShop("Gadget World", "www.gadgetworld.com")

product1 = Product("Gaming Mouse", "High precision gaming mouse", 1500.00, shop)
product2 = Product("Mechanical Keyboard", "RGB mechanical keyboard", 2500.00, shop)

customer1 = Customer("สมชาย", "somchai@gmail.com", "123/45 กรุงเทพฯ")

shop.addingItemsToCart(customer1, product1, 2)
shop.addingItemsToCart(customer1, product2, 1)

order = shop.checkOut(customer1)

order_id = order["order_id"]
status = shop.orderTracking(customer1, order_id)
print(status)
