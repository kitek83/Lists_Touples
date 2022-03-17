import random
def main():
    ROWS = 3
    COL = 4
    val = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    for r in range(ROWS):
        for c in range(COL):
            val[r][c] = random.randint(1,100)
    print(val)
    print('-----------------------------')
    names = ('Hannaw','Waclaw', 'Janek')
    for i in range(len(names)):
        print(names[i])
    print('#################')
    vals = [2,4,6,8,10]
    print(vals[1:3])
    nums = [1,2,3,4,5,6,7,8]
    print(nums[-4:])
    print(nums[4:])
    print('~~~~~~~~~~~~~~~~~~')
    vals = [2] * 5
    print(vals
          )


main()