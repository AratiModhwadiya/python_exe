"""from module1 import max,min
while True:
    print("1.Add Number")
    print("2.Maximum no")
    print("3.Minimum no")
    print("4.Ascending  order")
    print("5.Descending order")
    print("Close")
    choice = int(input("enter choice"))
    if choice == 2:
        max()
    elif choice == 3:
        min()
        break
    else:
        print("Close")
        break"""

"""def addvalue() :
    for i in range(0, 5) :
        no = int(input('Enter Number-{}: '.format(i + 1)))
        lst.append(no)"""
def max(lst):
    max_no = lst[0]
    for no in range(len(lst)) :
        if lst[no] >= max_no :
            max_no = lst[no]
    #print('Max No. is: {}'.format(max_no))
    return max_no
def min(lst):
    min_no = lst[0]
    for no in range(len(lst)) :
        if lst[no] <= min_no :
            min_no = lst[no]
    return min_no
    #print('Min No. is: {}'.format(min_no))
