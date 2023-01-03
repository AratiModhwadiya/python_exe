"""lst = []
def addvalue():
    for i in range(0,5):
        no = int(input('Enter Number-{}: '.format(i+1)))
        lst.append(no)

def ascending ():
    temp = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] >= lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])

def descending():
    temp = 0
    print("Descending order")
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] <= lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])

def max():
    max_no = lst[0]
    for no in range(len(lst)) :
        if lst[no] >= max_no :
            max_no = lst[no]
    print('Max No. is: {}'.format(max_no))

def min():
    min_no = lst[0]
    for no in range(len(lst)) :
        if lst[no] <= min_no :
            min_no = lst[no]
    print('Min No. is: {}'.format(min_no))

while True:
    print("1.Add numbers")
    print("2.Maximum no")
    print("3.Minimum no")
    print("4.Ascending  order")
    print("5.Descending order")
    print("Close")
    choice = int(input("enter choice"))

    if choice==1:
        addvalue()
        break"""

from minmaxm import min, max
from aedem import ascending, descending
lst = []

for i in range(0, 5):
    no = int(input('Enter No {}: '.format(i + 1)))
    lst.append(no)

while True:
    print("1.Maximum no")
    print("2.Minimum no")
    print("3.Ascending  order")
    print("4.Descending order")
    choice = int(input("enter choice"))

    if choice == 1 :
        m=max(lst)
        print(m)
    elif choice == 2 :
        mi=min(lst)
        print(mi)
    elif choice == 3 :
        asce=ascending(lst)
        print(lst)
    elif choice == 4 :
       des= descending(lst)
       print(lst)
    else :
        print("Close")
        break

