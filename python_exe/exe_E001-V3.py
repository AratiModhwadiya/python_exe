class Category :
    def __init__(self, name, parent=None, no_of_count=0) :
        self.name = name
        # self.code=code
        self.parent = parent
        self.products = []
        self.display_name = self.name
        self.no_of_count = 0

    def display_category(self) :
        print("Name:", self.name)
        print(self.products)
        print("-----------------------------")

class Product(Category) :
    def __init__(self, name, code, price, category, stock_at_locations={}) :
        self.stock_at_locations = stock_at_locations
        self.name = name
        self.code = code
        self.price = price
        self.category = category
        self.display_name = self.name

    def display_name1(self) :
        print("Name:", self.name, "code:", self.code, "price:", self.price)
        # print(self.stock_at_locations)

class Location :
    def __init__(self, name, code) :
        self.name = name
        self.code = code

class Movement:
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    @staticmethod
    def movements_by_product(product):
        return product


vehicle = Category("Vehicle")
electronics = Category("Electronics")
furn = Category('Furniture')
fruit = Category('Fruits')
chocolate = Category('Chocolate')

rajkot = Location('Rajkot', electronics)
surat = Location('Surat', chocolate)
delhi = Location('Delhi', vehicle)
mumbai = Location('Mumbai', furn)
ahmedabad = Location('Ahmedabad', rajkot)

location_list = [rajkot, surat, delhi, mumbai, ahmedabad]

p1 = Product("led", "l1", 20000, rajkot ,{rajkot : 20, ahmedabad : 3})
p2 = Product("5star", "F1", 20, rajkot, {delhi : 87})
p3 = Product("car", "V1", 200000, delhi, {mumbai : 90})
p4 = Product("table", "T1", 500, mumbai, {surat : 11, rajkot : 24})
p5 = Product("apple", "A1", 200, surat, {ahmedabad : 800})
p6 = Product("greenapple", "G1", 300, ahmedabad, {surat : 90})

product_list = [p1, p2, p3, p4, p5, p6]

for product in product_list :
    print(product.name)
    for i in product.stock_at_locations :
        print("{}-{}".format(i.name, product.stock_at_locations[i]))
    print("--------------------")

for j in location_list:
    print(j.name)
    for location in product_list:
        if j in location.stock_at_locations:
            print("{}-{}".format(location.name,location.stock_at_locations[j]))
    print()

