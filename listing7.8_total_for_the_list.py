def main():
    list = [14,55,66,77,14,45]
    total = 0.0
    count =0
    for x in list:
        total += x
        print('Total sum until index:',count,'is:', total)
        count += 1
    print('Total sum for all indexes from the list is',total)
    print('Number of elements if list is:',len(list))
    average = total / len(list)
    print('Average value of list is:', format(average,'.2f'))


main()