# Create a list
new_numbers = [2,6,89,2,4,6]
#Create a function that accepts list of numbers as an argument

def even_only(number_list):
    even_list = []
    print (number_list)
    for num in number_list :
        if num % 2 == 0:
            even_list.append(num) 
    return even_list
            

         
print(even_only(new_numbers))
