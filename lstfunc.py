list2 = []

def add() :
    name = input("enter name:")
    phone = input("Enter phone:")
    email = input("enter email:")
    age = input("enter age:")
    dict1 = {
        "Name" : name,
        "Phone" : phone,
        "Email" : email,
        "Age" : age
    }
    list2.append(dict1)
    return dict1

def print1() :
    for i in list2 :
        print("name is: {}".format(i['Name']))
        print("phone is: {}".format(i['Phone']))
        print("email is: {}".format(i['Email']))
        print("age is: {}".format(i['Age']))

def search() :
    email1 = input("enter email you want to search:")
    for k in list2 :
        if email1 in k.values() :
            print("email exists")
            print("name is: {}".format(k['Name']))
            print("phone is: {}".format(k['Phone']))
            print("email is: {}".format(k['Email']))
            print("age is: {}".format(k['Age']))
        else :
            print("email is not exist")

def delete() :
    email1 = input("enter email you want to delete record:")
    for i in range(len(list2)) :
        if list2[i]['Email'] == email1 :
            del list2[i]
            print("deleted")
            break

    else :
        print("record not found")

def update() :
    email1 = input("enter email you want to search:")
    for k in list2 :
        if email1 in k.values() :
            print("email exists")
            print("name is: {}".format(k['Name']))
            print("phone is: {}".format(k['Phone']))
            print("email is: {}".format(k['Email']))
            print("age is: {}".format(k['Age']))

            new_name=input("Enter new name")
            new_phone=input("Enter new phone")
            new_age=input("Enter new age")

            k.update({"Name":new_name})
            k.update({"Phone" : new_phone})
            k.update({"Age" : new_age})
            print(k)

while True :
    print("1.Add Details")
    print("2.Print ")
    print("3.Search")
    print("4.Delete")
    print("5.Update")
    print("5.Quite")
    ec = int(input("Enter choice"))

    if ec == 1 :
        add()
    elif ec == 2 :
        print1()
    elif ec == 3 :
        search()
    elif ec == 4 :
        delete()
    elif ec == 5 :
        update()
    else :
        print("Quite")
        break

        """git status"""