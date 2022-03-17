def main():
    prod_num = ['v475', 'f987', 'q143', 'r688']
    search = input('Enter number of the product:')
    if search in prod_num:
        print(search,'was found in the list.')
    else:
        print(search,'wasn\'t found in the list.')


main()