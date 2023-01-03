list1 = []


def number() :
    no = int(input("enter choice:"))
    for nu in range(no) :
        ab = int(input("Enter number:-"))
        list1.append(ab)


def ass() :
    for i in range(len(list1)) :
        for j in range(i + 1, len(list1)) :
            if list1[i] >= list1[j] :
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
        print(list1[i])


def des() :
    print("Dessending order")
    for i in range(len(list1)) :
        for j in range(i + 1, len(list1)) :
            if (list1[i] <= list1[j]) :
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
        print(list1[i])

    for i in range(len(list1)) :
        for j in range(i + 1, len(list1)) :
            if (list1[i] >= list1[j]) :
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
                print(list1[i])


while True :
    print("Add numbers")
    print("2.Asseding order")
    print("3.disending order")
    print("4.quite")
    ec = int(input("Enter choice"))
    if ec == 1 :
        number()
    if ec == 2 :
        ass()
    if ec == 3 :
        des()
    else :
        print("Quite")
