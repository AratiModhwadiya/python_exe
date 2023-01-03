"""print("1.Add Details")
print("2.Print ")
print("3.Quite")
list1 = []
choice = input("enter choice")
for i in range(len(choice)) :
    for no in range(i):
        print("abc")


def add() :
    name = input("enter name:")
    email = input("Enter email:")
    phone = input("enter phone:")
    age = input("enter age:")


def print1() :
    dict1 = {
        "name is:" : name,
        "email is:" : phone,
        "phone is:" : email,
        "age is:" : age
    }
    x = list1.append(dict1)
    print(x)


while True :
    if choice == 1 :
        add()
    elif choice == 2 :
        print1()
    else :
        print("Quite")
        break"""
list1 = []
def add() :

    dict1 = {
        "NAme is:" : name,
        "Email is:" : email
    }
def print1() :
    for i in dict1.items() :
        list1.append(i)
        print(list1)


while True :
    print("Add numbers")
    print("2.Asseding order")
    print("3.disending order")
    print("4.quite")
    ec = int(input("Enter choice"))

    if ec == 1 :
        name = input("enter your name:")
        email = input("enter your email")
        add()
    if ec == 2 :
        print1()
    else :
        print("Quite")
        break