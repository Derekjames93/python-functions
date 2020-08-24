#Write a function that accepts a list of numbers as an argument
use_this = [2,32,534,23,24,345,23]

def smallest(list_of_numbers): 
    smallest_number = []
    for num in list_of_numbers :
        smallest_number.append(num)
    smallest_number.sort()
    # print(smallest_number)
    return smallest_number[0]



print(smallest(use_this))