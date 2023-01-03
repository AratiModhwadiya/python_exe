"""class category :
    def __init__(self, name, code, no_of_count=0) :
        self.name = name
        self.code = code
        self.no_of_count = no_of_count

    def display(self) :
        print('name: ', self.name)
        print('code:', self.code)
        print('category: ', self.no_of_count)


class product(category) :
    def __init__(self, name, code, price, category) :
        self.name = name
        self.code = code
        self.price = price
        self.category = category
        category.no_of_count += 1

    def display(self) :
        print("Name: ", self.name, "code: ", self.code, "price:", self.price, "category: ", self.category.name)


elec = category("electronic", 'ele')
furn = category('furniture', 'fur')
fruit = category('fruits', 'frut')

lst1 = [
    {"name" : "phone", "code" : 1, "category" : "electronics", "price" : 100},
    {"name" : "tv", "code" : 2, "category" : "electronics", "price" : 4000},
    {"name" : "charger", "code" : 3, "category" : "electronics", "price" : 10},
    {"name" : "drees", "code" : 4, "category" : "clothes", "price" : 1000},
    {"name" : "tshirt", "code" : 5, "category" : "clothes", "price" : 400},
    {"name" : "apple", "code" : 6, "category" : "fruit", "price" : 120},
    {"name" : "laptop", "code" : 7, "category" : "electronics", "price" : 25000},
    {"name" : "mango", "code" : 8, "category" : "fruit", "price" : 400},
    {"name" : "chair", "code" : 9, "category" : "furniture", "price" : 500},
    {"name" : "table", "code" : 10, "category" : "furniture", "price" : 900}, ]

elec.display()
furn.display()
fruit.display()
for k in lst1 :
    print('Name : {}'.format(k['name']))
    print('Code : {}'.format(k['code']))
    print('Price : {}'.format(k['price']))
    print('Category : {}'.format(k['category']))
    print("---------------------------")


def asort(item) :
    return item["price"]
lst1.sort(key=asort)
for k in lst1 :
    print("name is: {}".format(k['name']))
    print("code is: {}".format(k['code']))
    print("category is: {}".format(k['category']))
    print("price is: {}".format(k['price']))
    print("-------------------")


def dsort(item) :
    return item["price"]
lst1.sort(key=dsort, reverse=True)
for k in lst1 :
    print("name is: {}".format(k['name']))
    print("code is: {}".format(k['code']))
    print("category is: {}".format(k['category']))
    print("price is: {}".format(k['price']))
    print("-------------------")


    email1 = input("enter email you want to search:")
    for k in lst1 :
        if email1 in k.values() :
            print("email exists")
            print("name is: {}".format(k['name']))
            print("phone is: {}".format(k['code']))
            print("email is: {}".format(k['price']))
            print("age is: {}".format(k['category']))
        else :
            print("email is not exist")
            break"""

class category :
    def __init__(self, name, code, no_of_count=0) :
        self.name = name
        self.code = code
        self.no_of_count = no_of_count

    def display(self) :
        print('name: ', self.name)
        print('code:', self.code)
        print('category: ', self.no_of_count)


class product(category) :
    def __init__(self, name, code, price, category) :
        self.name = name
        self.code = code
        self.price = price
        self.category = category
        category.no_of_count += 1

    def display(self) :
        print("Name: ", self.name, "code: ", self.code, "price:", self.price, "category: ", self.category.name)


elec = category("electronic", 'ele')
furn = category('furniture', 'fur')
fruit = category('fruits', 'frut')
p1 = product("phone", "ele", 20000, elec),
p2 = product("charger", "ele", 200, elec),
p3 = product("tv", "ele", 70000, elec),
p4 = product("laptop", "ele", 60000, elec),
p5 = product("chair", "fur", 1000, furn),
p6 = product("table", "fur", 2000, furn),
p7 = product("window", "fur", 1500, furn),
p8 = product("apple", "frut", 100, fruit),
p9 = product("mango", "frut", 300, fruit),
p10 = product("kiwi", "frut", 250, fruit)

lst1=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
lst1.append(p1)
elec.display()
furn.display()
fruit.display()

for i in range(len(lst1)) :
    for j in range(i + 1, len(lst1)) :
        if lst1[i].price <= lst1[j].price :
            temp = lst1[i].price
            lst1[i].price = lst1[j].price
            lst1[j].price = temp
    #print(lst1[i].price)
    print(lst1[i].name, lst1[i].code, lst1[i].price, lst1[i].category.name)


