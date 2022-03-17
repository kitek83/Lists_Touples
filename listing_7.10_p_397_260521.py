def main():
    numbers = [1,2,3,4,5]
    print('Total sum of all indexes in numbers list is', get_total(numbers))

def get_total(values):
    total = 0.0
    for num in values:
        total += num
    return total



main()