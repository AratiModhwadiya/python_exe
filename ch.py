"""print("Add numbers")
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
        break"""
#Parent Object

plastic = Category("plastic")
chocolate = Category("chocolate")
vehicle = Category("vehicle")
electric = Category("electric")
chemical = Category("chemical")

#Child Object

c1 = Category("Tupperwere", plastic)
c2 = Category("Dark Chocolate", chocolate)
c3 = Category("Four Wheelers", vehicle)
c4 = Category("DC", electric)
c5 = Category("Paint", chemical)

#Child of Child Object

childofc1 = Category("Water container", c1)
childofc2 = Category("Amul", c2)
childofc3 = Category("Audi", c3)

#Name of All Products

pro1 = Product("Water bottle", c1, 225)
pro2 = Product("Lily’s Dark", c2, 100)
pro3 = Product("Audi Q3", c3, 1200000)
pro4 = Product("Lindt Dark", c2, 400)
pro5 = Product("Wet food storage", c1, 300)
pro6 = Product("Audi A8", c3, 2500000)
pro7 = Product("Hu Simple Dark", c2, 500)
pro8 = Product("Audi Q8", c3, 3500000)
pro9 = Product("Kitchen helper", c1, 3000)
pro10 = Product("Audi A6", c3, 4500000)
pro11 = Product("Chocolove Dark", c2, 600)
pro12 = Product("Freezer Storage", c1, 450)
pro13 = Product("Fan", c4, 4500)
pro14 = Product("i20", vehicle, 340000)
pro15 = Product("Fruit & Nuts", chocolate, 340)
pro16 = Product("Light & series", electric, 940)
pro17 = Product("Tubelight", electric, 125)
pro18 = Product("Asian Paint", chemical, 3000)
pro19 = Product("Dulux Paint", chemical, 2500)
pro20 = Product("Super Paint", chemical, 1000)

#List of category

category_list = [plastic, chocolate, vehicle, c1, c2, c3, c4, c5, childofc1, childofc2, childofc3, electric, chemical]

#List of product

product_list = [pro1, pro2, pro3, pro4, pro5, pro6, pro7, pro8, pro9, pro10, pro11, pro12, pro13, pro14, pro15,
                pro16, pro17, pro18, pro19, pro20]

"""lst1 = [product("led", "ele", 20000, elec,"TV","electronic"),
        product("oled", "ele", 30000, elec,"TV","electronic"),
        product("qled", "ele", 40000, elec,"TV","electronic"),
        product("audi", "v", 2000000, vehic,"car","vehicle"),
        product("swift", "v", 20000, vehic,"car","vehicle"),
        product("bmw", "v", 200000, vehic,"car","vehicle"),
        product("tv table", "fur", 1000,furn,"table","furniture"),
        product("computer desk", "fur", 1400,furn,"table","furniture"),
        product("dining table", "fur", 2000,furn,"table","furniture"),
        product("green apple", "frut", 100,fruit,"apple","fruit"),
        product("empire", "frut", 200,fruit,"apple","fruit"),
        product("honeycrisp", "frut", 250,fruit,"apple","fruit"),
        product("dark chocolate", "c", 100,choco,"amul","chocolate"),
        product("cocoa", "c", 20,choco,"amul","chocolate"),
        product("milk chocolate", "c", 120,choco,"amul","chocolate")]"""

"""lst1 = [elec, furn, fruit, vehic, choco, child1, child2, child3, child4, child5, cchild1, cchild2, cchild3]
lst2 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]"""