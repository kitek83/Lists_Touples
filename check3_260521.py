list1 = [1,2,3,4,5]
list2 = []
for item in list1:
    list2.append(item)
    print('-----------')
    print('list2:',list2)

print(list2)
print('------------------')
list3 = [] + list1
print('list3:', list3)
print('####################')
m = min(list1)
print(m)

