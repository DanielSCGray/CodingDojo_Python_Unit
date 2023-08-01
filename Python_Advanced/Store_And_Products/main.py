from product import Product
from store import Store


prod1 = Product('a', 11, 'b')
prod2 = Product('a', 10, '?')

print(prod1.id)
print(prod2.id)

radioShed = Store('radioShed')

radioShed.add_product(prod1).add_product(prod2)
print(radioShed.products)

# radioShed.inflation(.1)
radioShed.set_clearance('?', .25)

#print the info for both prods
for item in radioShed.products:
    item.print_info()
#sell prod2 by id 
radioShed.sell_product_by_id(2)
#test should print info for only prod1
for item in radioShed.products:
    item.print_info()