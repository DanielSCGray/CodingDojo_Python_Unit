class Product:

    unique_id = 1

    def __init__(self, name, price, category) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.id = str(Product.unique_id)
        Product.unique_id +=1

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self
    
    def print_info(self):
        print(self.name)
        print(f"${self.price}")
        print(self.category)
        print('Id: ' + self.id)





# test = Product('a', 10, '?')

# test.print_info()
# test.update_price(.1, True)
# test.print_info()

# test2 = Product('b', 15, '!')
# print(test.id)
# print(test2.id)
# print(test.id)
