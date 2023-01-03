"""from module1 import ascending,descending
from minmaxm import min,max
while True:
    print("Add Number")
    print("2.Maximum no")
    print("3.Minimum no")
    print("4.Ascending  order")
    print("5.Descending order")
    print("Close")
    choice = int(input("enter choice"))
    if choice == 4:
        ascending ()
    elif choice == 5:
        descending()
    else:
        print("Close")
        break"""

def ascending (lst):
    temp = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] >= lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        #print(lst[i])
        #return lst[i]

def descending(lst):
    temp = 0
    print("Descending order")
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] <= lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        #print(lst[i])
        #return lst

