# adding numbers to an array
# append to insert element at the end of the array
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(4)
print(numbers)

# insert to insert elements in between the array
numbers.insert(2, 3)
print(numbers)


# pop
popped_value = numbers.pop(2)
print(f"Popped value: {popped_value}")
print(f"Numbers: {numbers} ")


#remove
numbers.remove(2)
print(f"Numbers: {numbers} ")
