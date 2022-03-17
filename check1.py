list1 = ['Jarek', 'Wacek', 'Kris']

a = list1[0]
print(a)
b = list1.index('Wacek')
print(b)
print(list1.index('Kris'))
print('-------------------')
item = 'Wacek'
c = list1.index(item)
print(c)
new_name = 'Alex'
print('================')
d = list1[c]
print(d)
f = list1.index('Wacek')
print(f)
print('###################')
list1[c] = 'Felix'
print(list1)