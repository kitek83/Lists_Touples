NUM_DAYS = 5
def main():
    sales = [0] * NUM_DAYS
    index = 0
    while index < len(sales):
        print('The value of sales for Day nr', index + 1, ' is:',sep='', end='')
        sales[index] = float(input())
        index += 1
    print('The values of sales for', NUM_DAYS,'days are:',sales)
    print('Here are the outputs:')
    for val in sales:
        print(val)
main()