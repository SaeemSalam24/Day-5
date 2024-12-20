# Adding elements
numbers = [10, 20, 30]
numbers.append(40)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

# Removing elements
numbers.remove(20)
print("After remove:", numbers)

popped = numbers.pop()
print("After pop:", numbers)
print("Popped element:", popped)

# Sorting a list
numbers = [5, 3, 8, 1]
numbers.sort()
print("Sorted list:", numbers)

# Reversing a list
numbers.reverse()
print("Reversed list:", numbers)
