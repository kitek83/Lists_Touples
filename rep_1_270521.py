def main():
    numbers = [1,2,3,4,5]
    print('Sum of the numbers contained in the list is:', get_numbers(numbers))
def get_numbers(vals):
    total = 0
    for num in vals:
        total += num
    return total

main()