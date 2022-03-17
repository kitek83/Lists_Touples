list = [['Marek, Kasia'], ['Sylwia', 'Janek'], ['Max', 'Mateusz'],['Jacek', 'David']]
print(list)
print(list[0])
print(list[1])
print()
print('----------------------')
for list1 in list:
    print(list1)
print('---------------------')
for x in list:
    for y in x:
        print(y)