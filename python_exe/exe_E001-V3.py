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

p1 = Product("led", "l1", 20000, electronics, {rajkot : 20, delhi : 3})#15-8
p2 = Product("5star", "F1", 20, chocolate, {delhi : 87, ahmedabad : 2})#37-52
p3 = Product("car", "V1", 200000, vehicle, {mumbai : 90, delhi : 1})#55-36
p4 = Product("table", "T1", 500, furn, {surat : 112, ahmedabad : 5})#87-30
p5 = Product("apple", "A1", 200, fruit, {ahmedabad : 800, rajkot : 20})#570-250

product_list = [p1, p2, p3, p4, p5]

for product in product_list :
    print(product.name)
    for i in product.stock_at_locations :
        print("{}-{}".format(i.name, product.stock_at_locations[i]))
    print("--------------------")

for j in location_list :
    print(j.name)
    for location in product_list :
        if j in location.stock_at_locations :
            print("{}-{}".format(location.name, location.stock_at_locations[j]))
    print()
class Movement :
    def __init__(self, from_location, to_location, product, quantity) :
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        print("Product:", self.product.name, "From_location:", self.from_location.name, "To_location:",
              self.to_location.name, "Quantity:", self.quantity)
        try :
            if from_location in product.stock_at_locations:
                for i in product.stock_at_locations :
                    if product.stock_at_locations[i] >= quantity :
                        update_quantity = self.product.stock_at_locations[i] - self.quantity
                        product.stock_at_locations.update({from_location : update_quantity})

            if to_location in product.stock_at_locations :
                for j in product.stock_at_locations :
                    if product.stock_at_locations[j] <= quantity :
                        updated_quantity = self.product.stock_at_locations[j] + self.quantity
                        product.stock_at_locations.update({to_location:updated_quantity})
                        print("Product_name:{} From_location-{} To_location-{} Updated_quantity-{} --{}".format(self.product.name,
                                self.from_location.name,self.to_location.name,update_quantity,updated_quantity))
        except Exception:
            print("Stock is not available")

    @staticmethod
    def movements_by_product(product) :
        for i in movement_list :
            if i.product.name == product.name :
                print()

m1 = Movement(rajkot, delhi, p1, 55)
m2 = Movement(delhi, ahmedabad, p2, 50)
m3 = Movement(mumbai, delhi, p3, 35)
m4 = Movement(surat, ahmedabad, p4, 25)
m5 = Movement(ahmedabad, rajkot, p5, 230)

movement_list = [m1, m2, m3, m4, m5]
