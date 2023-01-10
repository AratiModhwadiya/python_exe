class Category :
    def __init__(self, name, parent=None, no_of_count=0) :
        self.name = name
        # self.code=code
        self.parent = parent
        self.products = []
        self.display_name = self.name
        self.set_display_name()
        # self.products = products
        self.no_of_count = 0

    def display_category(self) :
        print(self.display_name)
        print("Name:", self.name)
        print("No_of_count:", self.no_of_count)
        print(self.products)
        print("-----------------------------")

    def set_display_name(self) :
        obj = self
        while (obj.parent != None) :
            self.display_name = f'{obj.parent.name} > {self.display_name}'
            obj = obj.parent


class product(Category) :
    def __init__(self, name, code, price, category) :
        self.name = name
        self.code = code
        self.price = price
        self.category = category
        self.display_name = self.name
        category.no_of_count += 1
        category.products.append(self.name)

    def display_name1(self) :
        print("Name: ", self.name, "code: ", self.code, "price:", self.price, "category: ",
              self.category.name)


# Parent Categories
vehicle = Category("Vehicle")
electronics = Category("Electronics")
furn = Category('Furniture')
fruit = Category('Fruits')
# Level1
car = Category('Car', vehicle)
tv = Category('Television', electronics)
child2 = Category('Table', furn)
child4 = Category("Apple", fruit)
# child5 = Category("Choco", choco)
# Level2
petrol = Category('Petrol', car)
sony = Category('Sony', tv)
c_ofchild2 = Category('Large table', child2)
c_ofchild1 = Category("empire", child4)
# Level3
# bmw = Category('BMW', petrol)
# audi = Category('Audi', petrol)

category_list = [vehicle, electronics, furn, fruit, car, tv, petrol, sony, child2, child4, c_ofchild2, c_ofchild1]
category_list.sort(key=lambda high_low : high_low.display_name)
lst1 = [product("led", "ele", 20000, tv),
        product("oled", "ele", 30000, sony),
        product("qled", "ele", 40000, electronics),
        product("audi", "v", 2000000, car),
        product("swift", "v", 20000, petrol),
        product("bmw", "v", 200000, car),
        product("tv table", "fur", 1000, furn),
        product("computer desk", "fur", 1400, child2),
        product("dining table", "fur", 2000, c_ofchild2),
        product("green apple", "frut", 100, fruit),
        product("empire", "frut", 200, child4),
        product("honeycrisp", "frut", 250, c_ofchild1)]

for category in category_list :
    category.display_category()
