print("Add numbers")
print("2.Asseding order")
print("3.disending order")
print("4.quite")

while True:
    ec=int(input("Enter choice"))
    lst = [1, 2, 3, 4]
    if ec>=1 and ec<=4:

     if ec==lst[0]:
         no = int(input("enter choice:"))
         list1 = []
         for nu in range(no):
             ab = int(input("Enter number:-"))
             list1.append(ab)
     lst = []
     for i in range(0, 5) :
         no = int(input("enter No {}".format(i + 1)))
         lst.append(no)

     max_no = lst[0]
     for no in range(len(lst)) :
         if lst[no] >= max_no :
             lst[no] = max_no
             lst.append((lst[no]))
     print("max no is:{} ".format(lst[no]))
     if ec==lst[1]:
       # list1 = [21, 45, 32, 89, 0]
        for i in range(no):
            for j in range(i + 1, no):
                if (list1[i] <= list1[j]):
                    temp = list1[i]
                    list1[i] = list1[j]
                    list1[j] = temp
            print(list1[i])
     if ec==lst[2]:
       for i in range(no):
           for j in range(i + 1, no):
               if (list1[i] >= list1[j]):
                   temp = list1[i]
                   list1[i] = list1[j]
                   list1[j] = temp
           print(list1[i])
     elif ec==lst[3]:
        print("Quite")
        break
