from product import Product


class Store:
    def __init__(self, name, products=[]) -> None:
        self.name = name
        self.products = products

    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product_by_idx(self, idx):
        self.products.pop(idx)
        return self
    
    def sell_product_by_id(self, product_id):
        if type(product_id) == int:
            product_id = str(product_id)
        for item in self.products:
            if item.id == product_id:
                self.products.remove(item)
        return self
    
    def inflation(self, percent_increase):
        for item in self.products:
            item.price += (item.price * percent_increase)
        return self
    
    def set_clearance(self, category, percent_discount):
        for item in self.products:
            if item.category == category:
                item.price -= (item.price * percent_discount)
        return self



# prod1 = Product('a', 11, 'b')
# prod2 = Product('a', 10, 'b')

# print(prod1.id)
# print(prod2.id)

# radioShed = Store('radioShed')

# radioShed.add_product(prod1).add_product(prod2)
# print(radioShed.products)
# radioShed.sell_product_by_id(2)
# for item in radioShed.products:
#     print(item.price)




