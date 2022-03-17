#This program save list of the numbers in the file
def main():
    numbers = [1,2,3,4,5,6,7,8]
    file = open('numbers.txt','w')
    for num in numbers:
        file.write(str(num) + '\n')
    file.close()


main()