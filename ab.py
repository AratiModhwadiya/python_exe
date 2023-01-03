while True:
    ec = int(input("enter choice:"))
    if ec==1:
            name = input("Enter your name:-")
            phone = input("Enter your phone:-")
            email = input("Enter your email:-")
            age = input("Enter your age:-")

    if ec==2:
        dict1={
            "name is:": name,
            "phone is:" : phone,
            "email is:" : email,
            "age is:" : age
        }
        for x, y in dict1.items() :
            print(x, y)

    elif ec==3:
        print("Quite")
        break
