class Category :
    def __init__(self, name, parent=None, no_of_count=0) :
        self.name = name
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

class Movement :
    def __init__(self, from_location, to_location, product, quantity) :
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        print(self.quantity, self.product.name, "is moved from", self.from_location.name, "to", self.to_location.name)

        try :
            if from_location in product.stock_at_locations:
                #for i in product.stock_at_locations:
                if product.stock_at_locations[from_location] >= quantity :
                    update_quantity = self.product.stock_at_locations[from_location] - self.quantity
                    product.stock_at_locations.update({from_location : update_quantity})
            if to_location in product.stock_at_locations:
                #for i in product.stock_at_locations:
                #if product.stock_at_locations[to_location] <= quantity :
                    updated_quantity = self.product.stock_at_locations[to_location] + self.quantity
                    product.stock_at_locations.update({to_location : updated_quantity})
                    """print("Product:", self.product.name, "From_location:", self.from_location.name,
                                    "To_location:",self.to_location.name,update_quantity,updated_quantity)"""
                    print()
            else:
                print("No",self.product.name,"is found at",self.to_location.name)

        except Exception:
            print(self.product.name, "is not available at", self.from_location.name)
            print()

    @staticmethod
    def movements_by_product(product) :
        for m in movement_list:
            if m.product.name == product.name:
                print(f"avalible quantity ,{m.from_location.name,product.stock_at_locations.values(),m.to_location.name}")
                #for i in product.stock_at_locations:
                #print("avalible quantity: {}-{}".format(m.from_location.name,product.stock_at_locations[i]))
                #print("{}-{}".format(m.to_location.name, product.stock_at_locations[i]))
                     #if m.product.name == product.name:

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

led = Product("led", "l1", 20000, electronics, {rajkot : 20, delhi : 3})
choco = Product("5star", "F1", 20, chocolate, {delhi : 87, ahmedabad : 2})
#choco_5star = Product("5star", "F1", 20, chocolate, {delhi : 87, ahmedabad : 2})
car = Product("car", "V1", 200000, vehicle, {mumbai : 90, delhi : 1})
table = Product("table", "T1", 500, furn, {surat : 112, ahmedabad : 5})
apple = Product("apple", "A1", 200, fruit, {ahmedabad : 800, rajkot : 20})

product_list = [led,choco, car, table, apple]

m1 = Movement(rajkot, delhi, led, 54)
m7 = Movement(delhi,ahmedabad,choco,23)
#m2 = Movement(delhi, ahmedabad, choco_5star, 50)
m3 = Movement(mumbai, delhi, car, 35)
m4 = Movement(surat, ahmedabad, table, 25)
m5 = Movement(ahmedabad, rajkot, apple, 230)
m6 = Movement(rajkot, ahmedabad, led, 30)

movement_list = [m1, m3, m4, m5, m6,m7]

for i in product_list:
    Movement.movements_by_product(i)

for product1 in product_list :
    print(product1.name)
    for i in product1.stock_at_locations :
        print("{}-{}".format(i.name, product1.stock_at_locations[i]))
    print("--------------------")

for j in location_list :
    print(j.name)
    for location in product_list :
        if j in location.stock_at_locations :
            print("{}-{}".format(location.name, location.stock_at_locations[j]))
    print()


"""class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()"""