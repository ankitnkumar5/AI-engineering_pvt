#1. Declaring and Accessing List Elements
fruits = ["Apple", "Banana", "Cherry", "Mango"]
print(fruits[0])  
print(fruits[2]) 
print(fruits[-1])
print(len(fruits))


#Modifying, Adding, and Removing Elements
numbers = [10, 20, 30]

# Modify an existing element
numbers[1] = 25
print(numbers)
numbers.append(40)
print(numbers)  
numbers.insert(1, 15)
print(numbers) 
numbers.remove(25) 
last_item = numbers.pop() 
print(numbers) 