class category :
    def __init__(self, name, code, parent=None, no_of_count=0) :
        self.name = name
        self.code = code
        #self.display_name = display_name
        #self.products = products
        self.parent = parent
        self.no_of_count = no_of_count

    def display(self) :
        print('name: ', self.name)
        print('code:', self.code)
        print('category: ', self.no_of_count)

    def display_name(self,name,display_name,parent) :
        print("Name: ", self.name, "display_name: ", self.display_name, "Parent: ", self.parent)


class product(category) :
    def __init__(self, name, code, price, category) :
        self.name = name
        self.code = code
        self.price = price
        self.category = category
        category.no_of_count += 1

    def display(self) :
        print("Name: ", self.name, "code: ", self.code, "price:", self.price, "category: ", self.category.name)
    def display_name(self,name,display_name,parent=None) :
        print("Name: ", self.name, "display_name: ", self.display_name, "Parent: ", self.parent)
elec = category("electronic", 'ele')
furn = category('furniture', 'fur')
fruit = category('fruits', 'frut')
vehic = category('vehic', 'v')
choco = category('chocolate', 'c')

child1 = category("TV", elec)
child2 = category("table", furn)
child3 = category("apple", fruit)
child4 = category("car", vehic)
child5 = category("jams", choco)

cchild1 = category("tv", child1)
cchild2 = category("Amul", child2)
cchild3 = category("car", child3)

p1 = product("led", "ele", 20000, elec),
p2 = product("oled", "ele", 30000, elec),
p3 = product("qled", "ele", 40000, elec),
p4 = product("audi", "v", 2000000, vehic),
p5 = product("swift", "v", 20000, vehic),
p6 = product("bmw", "v", 200000, vehic),
p7 = product("tv table", "fur", 1000, furn),
p8 = product("computer desk", "fur", 1400, furn),
p9 = product("dining table", "fur", 2000, furn),
p10 = product("green apple", "frut", 100, fruit),
p11 = product("empire", "frut", 200, fruit),
p12 = product("honeycrisp", "frut", 250, fruit),
p13 = product("dark chocolate", "c", 100, choco),
p14 = product("cocoa", "c", 20, choco),
p15 = product("milk chocolate", "c", 120, choco)
"""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"""
lst1 = [elec, furn, fruit, vehic, choco, child1, child2, child3, child4, child5, cchild1, cchild2, cchild3]
lst2 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]
elec.display()
furn.display()
fruit.display()
vehic.display()
choco.display()

for product in lst1 :
    print('Name : {}'.format(product.name))
    print('Code : {}'.format(product.code))
    print('Price : {}'.format(product.price))
    print('Category : {}'.format(product.category.name))
    print("---------------------------")
    print(product.display())
