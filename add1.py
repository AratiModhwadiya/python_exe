"""sum1 = 0
no = int(input("enter choice of number:"))
for nu in range(no) :
    ab = int(input("Enter number:-"))
    sum1 = sum1+ab
    print(sum1)"""



"""list1=[1,4,2,5,7]
list2=[2,3,7,6,0]
for list1 in range(len(list1),len(list2),1):
    print("list1 is",list1)
    for list2 in range(len(list1),len(list2),2):
        print("list2 is:",list2)"""
list1=[1,2,3,4,5,6]
for even in range(1,len(list1),1):
    if even %2!=0:
      print("even:",even)
list2=[1,2,3,4,5,6,7]
for odd in range(1,len(list2),1):
    if odd %2==0:
        print("odd:",odd)

