my_numbers = [1,34,6,32,23,35,23,34]
def is_even(num1):
    # Use an if/else statement that returns a boolean
    if num1 % 2 == 0 :
        return True
    else :
        return False

def is_odd(num1):
    if num1 % 2 != 0 :
        return True
    else :
        return False

#Write a function that accepts list of numbers as an arugment


def odd_list(list_of_numbers):
    new_list = []
    for num in list_of_numbers:
        if is_odd(num):
            new_list.append(num)
    
    return new_list

print(odd_list(my_numbers))