# For each of the following code snippets, first predict the output (what you will see printed to the terminal). 
# Once you've made a prediction, run the code snippet to see if you are correct!

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#5

#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#NameError

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#5 (function ends at return statement, won't do anything written after)

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#5 will print from the function call
#None from print(x) since no return value

#6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
#3 from function call 1
#5 from function call 2
#None from printing function calls without return values
#^That was wrong!
#it actually causes a type error because the print statement applies the + operator to two 'None's and None Type doesn't support +

#7
def concatenate(b,c):
    return str(b)+str(c)
    print(concatenate(2,5))
#Nothing will print, the print call was mistakenly placed w/in the function's code block

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#100 (from function call)
#10 from return in the else block since b( aka 100) is not < 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#7
#14
#21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#500 (ln 90)
#500 (line 94)
#300 (function call)
#500 (line 96)

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#500 
#500 
#300 
#500 
#same logic as above : the return statement only matters if the function call itself is printed (or saved to a variable and then that is printed)

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#500 
#500 
#300 
#300 (the value of b was re-assigned to the function call's return value on ln 126)

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#a name error? because function foo calls an undefined function bar
#Wrong! order of definitions appears not to matter so 
# 1 from print
# 3 from bar() which calls print(3), and 
# 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#1 from print(1)
#3 fromt bar() on 147
#5 prints x value which is the return value of bar()
#10 from print(y) which is a variable set to foo's return value (10)







