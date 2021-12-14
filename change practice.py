import random

keyword = ['True', 'False', 'None']
def change_keyword(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j] == '='):
                j = j-1
                b = random.choice(keyword)
                a[i][j] = b

c = [[1, 2], [3, '=', 5]]
change_keyword(c)
