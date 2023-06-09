num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # variable declaration
string = 'Hello World' # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary
fruit = ('blueberry', 'strawberry', 'banana') # Tuples
print(type(fruit)) # type check
print(pizza_toppings[1]) # list, access value, log statement
pizza_toppings.append('Mushrooms') # list, add value 
print(person['name']) # Dictionary, access value, log statement
person['name'] = 'George' # Dictionary, change value 
person['eye_color'] = 'blue' # Dictionary, change value
print(fruit[2]) # Tuples, access value, log statement

if num1 > 45: # if
    print("It's greater") # log statement
else: # else
    print("It's lower") # log statement

if len(string) < 5: # if
    print("It's a short word!") # log statement
elif len(string) > 15: #if
    print("It's a long word!") # log statement
else: # else
    print("Just right!") # log statement

for x in range(5): # for loop
    print(x) # log statement
for x in range(2,5): #for loop
    print(x) # log statement
for x in range(2,10,3): # for loop
    print(x) #log statement
x = 0 # variable declaration
while(x < 5): # while loop
    print(x) # log statement
    x += 1 # variable declaration

pizza_toppings.pop() # list, access value, delete value
pizza_toppings.pop(1) # list, access value, delete value

print(person) # log statement
person.pop('eye_color') # Dicitionary, access value, delete value
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional, if
        continue # function
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if
        break # function

def print_hello_ten_times(): # function
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # function

def print_hello_x_times(x): # function, argument
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # function, argument

def print_hello_x_or_ten_times(x = 10): # function, argument
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # function
print_hello_x_or_ten_times(4) # function, argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)