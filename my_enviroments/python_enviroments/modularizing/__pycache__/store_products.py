class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []

    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self

    def sell_product(self, id):
        sold = self.product_list[id]
        self.product_list.remove(self.product_list[id])
        print(f"Item Sold: {sold.name}")
        return self

    def inflation(self, percent_increase):
        self.percent_increase = percent_increase
        for product in self.product_list:
            product.price = product.price + (product.price * percent_increase)
        return self

    def inventory(self):
        inventory = "Iventory: "
        for product in self.product_list:
            inventory += f"{product.name}, "
        print(inventory)

    def set_clearance(self, catgetory, percent_discount):
        self.percent_discount = percent_discount
        self.cagetory = catgetory
        clearance = "Clearance: "
        for product in self.product_list:
            if product.category == "vegetables":
                product.price = product.price - \
                    (product.price / percent_discount)


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        self.percent_change = percent_change
        self.is_increased = is_increased
        if is_increased == True:
            self.price = self.price * self.percent_change
        elif is_increased == False:
            self.price = self.price / self.percent_change

    def print_info(self):
        print(
            f"Product: {self.name}, Price: ${self.price}, Category: {self.category}"
        )


apple = Product("apple", 3, "vegetables")
orange = Product("orange", 2, "vegetables")
starbuck = Product("starbucks", 4, "drinks")
monster = Product("monster", 3, "drink")


# Item Info
walmart = Store("Walmart")


apple.print_info()
orange.print_info()
starbuck.print_info()
monster.print_info()


# Store info
walmart.add_product(apple).add_product(
    orange).add_product(starbuck).add_product(monster)

walmart.inventory()


walmart.inflation(0.3)

walmart.sell_product(0)

walmart.set_clearance("vegetables", 2)

walmart.inventory()


# # Test

# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.products = []

#     def add_product(self, product_name, price, category):
#         self.products.append(Product(product_name, price, category))
#         return self

#     def list_products(self):
#         inventory = "Inventory: "
#         for i in self.products:
#             print(i.item)
#         return i.print_info()

#     def sell_products(self, id):
#         sold = self.products.pop(id)
#         print(f"Product sold: {sold.item}")
#         return self

#     # def inflation(self, percent_increase):
#     # def set_clearance(self, category, percent_discount):


# class Product:
#     def __init__(self, product_name, price, category):
#         self.item = product_name
#         self.price = price
#         self.category = category

#     def update_price(self, percent_change, is_increased):
#         if is_increased == True:
#             self.price = self.price + (self.price * percent_change)
#             return self
#         else:
#             self.price = self.price - (self.price * percent_change)
#             return self

#     def print_info(self):
#         print(
#             f"Product: {self.item} Category: {self.category} Price: {self.price}")
#         return self


# walmart = Store("walmart")

# walmart.add_product("Oreos", 4.99, "Cookies").add_product("Orange", 2.99, "Fruit").add_product(
#     "Bread", 2.49, "Bakery").add_product("Milk", 1.99, "Dairy").list_products()

# walmart.sell_products(1)
# walmart.list_products()
