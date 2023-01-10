"""create one class named "category" with members "name", "code", "no_of_products"
create one class named "product" with members "name", "code", "category", "Price"
Create three objects of category.
Create 10 different products. Code must be unique."""

"""class category :
    no_of_products=0
    def __init__(self, name, code, no_of_products) :
        self.name = name
        self.code = code
        category.no_of_products += 1

    def displayCount(self) :
        print("Total category %d" % category.no_of_products)

obj1 = category()
obj2 = category()
obj3 = category()
obj1.displayCount()
obj2.displayCount()
obj3.displayCount()


def display(self) :
    print("name is:", self.name)
    print("code is:", self.code)
    print("products is:", self.no_of_products)


class products(category) :
    def __init__(self, name, code, category, price) :
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def displayCount(self) :
        print("Total Employee %d" % category.no_of_products)
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
    print("-------------------")"""

"""p1 = product("phone", "ele", 20000, elec),
p2 = product("charger", "ele", 200, elec),
p3 = product("tv", "ele", 70000, elec),
p4 = product("laptop", "ele", 60000, elec),
p5 = product("chair", "fur", 1000, furn),
p6 = product("table", "fur", 2000, furn),
p7 = product("window", "fur", 1500, furn),
p8 = product("apple", "frut", 100, fruit),
p9 = product("mango", "frut", 300, fruit),
p10 = product("kiwi", "frut", 250, fruit)"""


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

lst1 = [product("phone", "ele", 20000, elec),
        product("charger", "ele", 200, elec),
        product("tv", "ele", 70000, elec),
        product("laptop", "ele", 60000, elec),
        product("chair", "fur", 1000, furn),
        product("table", "fur", 2000, furn),
        product("window", "fur", 1500, furn),
        product("apple", "frut", 100, fruit),
        product("mango", "frut", 300, fruit),
        product("cherry", "frut", 250, fruit)]

# lst1=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
elec.display()
furn.display()
fruit.display()
for product in lst1 :
    print('Name : {}'.format(product.name))
    print('Code : {}'.format(product.code))
    print('Price : {}'.format(product.price))
    print('Category : {}'.format(product.category.name))
    print("---------------------------")
    print(product.display())
"""print("SORTING LOW TO HIGH")
lst1.sort(key=lambda low_high : low_high.price)
for product in lst1 :
    print('Name : {}'.format(product.name))
    print('Code : {}'.format(product.code))
    print('Price : {}'.format(product.price))
    print('Category : {}'.format(product.category.name))
    print("---------------------------")"""

print("SORTING HIGH TO LOW")
# lst1.sort(key=lambda high_low : high_low.price, reverse=True)
for i in range(len(lst1)) :
    for j in range(i + 1, len(lst1)) :
        if lst1[i].price <= lst1[j].price :
            temp = lst1[i]
            lst1[i] = lst1[j]
            lst1[j] = temp
    # print(lst1[i].price)
    # print(lst1[i].name, lst1[i].code, lst1[i].price, lst1[i].category.name)
    print('Name : {}'.format(lst1[i].name))
    print('Code : {}'.format(lst1[i].code))
    print('Price : {}'.format(lst1[i].price))
    print('Category : {}'.format(lst1[i].category.name))
    print("----------------------")
print("SORTING LOW TO HIGH")
# lst1.sort(key=lambda high_low : high_low.price, reverse=True)
for i in range(len(lst1)) :
    for j in range(i + 1, len(lst1)) :
        if lst1[i].price >= lst1[j].price :
            temp = lst1[i]
            lst1[i] = lst1[j]
            lst1[j] = temp
    # print(lst1[i].price)
    print('Name : {}'.format(lst1[i].name))
    print('Code : {}'.format(lst1[i].code))
    print('Price : {}'.format(lst1[i].price))
    print('Category : {}'.format(lst1[i].category.name))
    print("----------------------")
    # print(lst1[i].name, lst1[i].code, lst1[i].price, lst1[i].category.name)

code1 = input("enter code you want to search:")
for i in range(len(lst1)) :
    for j in range(1) :
        if code1 in lst1[i].code :
            print('Name : {}'.format(lst1[i].name))
            print('Code : {}'.format(lst1[i].code))
            print('Price : {}'.format(lst1[i].price))
            print('Category : {}'.format(lst1[i].category.name))
        else :
            break

"""new_name = input("Please enter a category name:\n")
new_code = input("Please enter a category name:\n")
new_price = input("Please enter a category name:\n")
new_category = input("Please enter a category name:\n")
lst1.append(new_name)
lst1.append(new_code)
lst1.append(new_price)
lst1.append(new_category)
print(lst1)
for i in range(len(lst1)) :
    for j in range(1) :
        if code1 in lst1[i].code :
            print('Name : {}'.format(lst1[i].new_name))
            print('Code : {}'.format(lst1[i].new_code))
            print('Price : {}'.format(lst1[i].price))
            print('Category : {}'.format(lst1[i].category.name))

for i in lst1 :
        print('Name : {}'.format(lst1[i].name))
        print('Code : {}'.format(lst1[i].code))
        print('Price : {}'.format(lst1[i].price))
        print('Category : {}'.format(lst1[i].category.name))"""
