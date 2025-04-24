fruits = ["apple", "banana", "cherry", "melone", "peach", "pineapple"]


# print(fruits.remove("apple"))
# print(fruits)

# print(fruits.pop(0))
# print(fruits.pop())
# print(fruits)

# del fruits[0]
# print(fruits)

# # del fruits
# print(fruits.clear())
# print(fruits)

# for fruit in fruits:
#   print(fruit)

# for index in range(len(fruits)):
#   print(index)


# i = 0
# while i < len(fruits):
#   print(fruits[i])
#   i = i + 1
 
# even_numbers = [2,4,6,8,10,12,14,16,64]

# [print (x) for x in even_numbers]
# i = len(even_numbers)
# print(i)

# while i >= 0:
#   print(i)
#   print(even_numbers[i])
#   i = i - 1


# counter_number = 9

# while counter_number >= 0 :
#   print(counter_number)
#   counter_number = counter_number - 1


# index = len(even_numbers)

# while index > 0:
#   index = index - 1
#   print(even_numbers[index])

# i = len(fruits)

# while i > 0:
#   i = i - 1
#   print(fruits[i])


even_numbers = [2,4,6,8,10,12,14,16,64]
# greater_than_ten_numbers = []


# for number in even_numbers:
#   if number > 10 :
#    greater_than_ten_numbers.append(number)
#    print(greater_than_ten_numbers)


greater_than_ten_numbers = [ x for x in even_numbers if x > 10]
print(greater_than_ten_numbers)