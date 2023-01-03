print("Add numbers")
print("2.Asseding order")
print("3.disending order")
print("4.quite")

while True:
    ec=int(input("Enter choice"))
    lst = [1, 2, 3, 4]
    if ec>=1 and ec<=4:

     if ec==lst[0]:
       add1=int(input("Enter 1st number"))
       add2=int(input("Enter 2nd number"))
       sum=add1+add2
       print("Sum is", sum)
     if ec==lst[1]:
        list1 = [21, 45, 32, 89, 0]
        for i in range(0, 5):
            for j in range(i + 1, 5):
                if (list1[i] <= list1[j]):
                    temp = list1[i]
                    list1[i] = list1[j]
                    list1[j] = temp
            print(list1[i])
     if ec==lst[2]:
       m = int(input("enter choice:"))
       list1 = []
       for n in range(m):
           a = int(input("Enter number:-"))
           list1.append(a)
       for i in range(m):
           for j in range(i + 1, m):
               if (list1[i] <= list1[j]):
                   temp = list1[i]
                   list1[i] = list1[j]
                   list1[j] = temp
           print(list1[i])
     elif ec==lst[3]:
        print("Quite")
        break
