def main():
    numbers = get_numbers()
    print('The list is following', numbers)

def get_numbers():
    val = []
    again = 't'
    while again == 't':
        num = float(input('Enter number:'))
        val.append(num)
        again = input('Press "t" if you want to add next number to the list.')
    return val

main()