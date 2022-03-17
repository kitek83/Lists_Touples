def main():
    file = open('numbers.txt','r')
    numbers = file.readlines()
    file.close()

    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1
    print(numbers)
