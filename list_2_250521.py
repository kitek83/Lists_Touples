numbers = [1,22,33,55,44,7]
print(numbers)
numbers[0] = 99
print(numbers)
print('-----------------------')

numbers2 = [0] * 5
index = 0
while index < len(numbers2):
    numbers2[index] = 99
    index += 1
print(numbers2)
print('---------------------------------')