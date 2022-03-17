def main():
    name_list = []
    again = 't'
    while again == 't':
        name = input('Enter your name.')
        name_list.append(name)
        again = input('Enter "t", if you want to add another name, otherwise enter another mark.')
    print('You appended the following name:', name_list)
    for name in name_list:
        print(name)

main()