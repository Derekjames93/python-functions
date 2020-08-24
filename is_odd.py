#Create a function that will use your is_even function to determine if odd

def is_even(num1):
    # Use an if/else statement that returns a boolean
    if num1 % 2 == 0 :
        return True
    else :
        return False

def is_odd(num1):
    if not is_even(num1) :
        return "The number is odd"
    else :
        return "The number is even"
print(is_odd(2))

# def is_odd(num1):
#     if is_even(num1) != True :
#         return "The number is odd


    