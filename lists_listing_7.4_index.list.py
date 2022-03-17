def main():
    food = ['hamburger', 'pizza', 'sausage']
    item = input('Enter food item to be changed:')
    try:
        item_index = food.index(item)
        print(item_index)
        new_item = input('Enter new food element:')
        food[item_index] = new_item
        print('Modified food list is the following:',food)
        
    except ValueError:
        print('Entered element wasn \'t found in the list.')

main()