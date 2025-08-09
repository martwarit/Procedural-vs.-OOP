product_list = []

def add_product(product_list):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    product = {
        "name" : name,
        "quantity" : quantity
    }

    product_list.append(product)
    pass

def show_products(product_list):
    print("Product List:")
    for i, product in enumerate(product_list, start=1):
        print(f"{i}. {product['name']}-{product['quantity']}units")

    pass
add_product(product_list)
add_product(product_list)
show_products(product_list)