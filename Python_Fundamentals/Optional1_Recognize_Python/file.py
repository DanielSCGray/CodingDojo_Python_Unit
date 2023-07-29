#In file.py, identify the code with a comment to correspond with the concept from file.txt
num1 = 42
#num: int
num2 = 2.3
#num: float
boolean = True
#bool
string = 'Hello World'
#str
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#dictionary
fruit = ('blueberry', 'strawberry', 'banana')
#tuple
print(type(fruit))
#log statement will print the type: tupple
print(pizza_toppings[1])
#prints the str at list index 1: 'Sausage'
pizza_toppings.append('Mushrooms')
#'Mushrooms added/pushed to the end of the list
print(person['name'])
#prints the value attached to key 'name' in dictionary 'person'
person['name'] = 'George'
# in dictionary "person", set the value of key 'name' to 'George'
person['eye_color'] = 'blue'
# in dictionary "person", create a new key 'eye_color' and assign value 'blue'
print(fruit[2])
# print the value at idx 2 in the tuple "fruit" : 'banana'
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# num1 = 42 so statement will print "It's lower"
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# var string = 'Hello World' which is length 11. conditional will print 'Just right!'
for x in range(5):
    print(x)
# range will start at 0, stop at 4: prints 0,1,2,3,4
for x in range(2,5):
    print(x)
#range starts at 2, ends 4: 2,3,4
for x in range(2,10,3):
    print(x)
#range starts at 2, ends at 9,  increments +3 : prints 2,5,8
x = 0
while(x < 5):
    print(x)
    x += 1
#prints: 0,1,2,3,4
pizza_toppings.pop()
#removes last value which is the recently-appended value 'Mushrooms'
pizza_toppings.pop(1)
#removes the value at idx : 'Sausage'

print(person)
#prints all the key-value pairings in dictionary 'person'
person.pop('eye_color')
#remove key 'Eye_color' and return its value
print(person)
# prints k-v pairings in 'person' less the one removed in line 63
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#will print 'After 1st if statement' 3 times for values 'Jalepenos' 'cheese' and 'Olives', then will break/terminate
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#defines a function
print_hello_ten_times()
print('break1')
#calls function which then prints 'Hello' 10x
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#defines a function which takes a num parameter and prints 'Hello' num times
print_hello_x_times(4)
#calls func w/param 4 : print Hello  4x
print('break2')
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#defines a function w/num parameter, sets default param to 10
print_hello_x_or_ten_times()
#calls func w/out inputing a new param so function will print 10 (default param) times 
print('break3')
print_hello_x_or_ten_times(4)
#calls function w/param 4 which replaces the default: func prints 4 times


"""
Bonus section
"""

# print(num3)
#NameError: num3 is undefined variable
# num3 = 72
#definition fixes name error, if this were above print statement it would run
# fruit[0] = 'cranberry'
#TypeError: fruit is a tuple which is an immutable data type
# print(person['favorite_team'])
#KeyError: the key being called does not exist in this dict
# print(pizza_toppings[7])
#IndexError: index 7 does not exist in pizza_toppings which is less than 8 values long
#   print(boolean)
#IndentationError: the print statement is not properly indented
# fruit.append('raspberry')
#AttributeError: tuples do not have a built in method append() likely because they are immutable
# fruit.pop(1)
#AttributeError: tuples are  immutable so no pop() method exists for them