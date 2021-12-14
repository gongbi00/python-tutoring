import random

def change_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j] == '['):
                j=j+1
                b = int(a[i][j]) + 1
                a[i][j] = str(b)


a = [['[', '4', ']']]
change_list(a)
