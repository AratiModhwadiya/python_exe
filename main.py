class Category:
    def __init__(self,name,parent=None)->None:
        self.name = name
        self.parent = parent
        self.display_name = self.name
        self.set_display_name()
    def display_category(self):
        print(self.display_name)
    def set_display_name(self):
        obj = self
        while(obj.parent!=None):
            self.display_name = f'{obj.parent.name} > {self.display_name}'
            obj = obj.parent

# Parent Categories
vehicle = Category("Vehicle")
electronics = Category("Electronics")

#Level1
car = Category('Car',vehicle)
tv = Category('Television',electronics)

#Level2
petrol = Category('Petrol',car)
sony = Category('Sony',tv)

#Level3
bmw = Category('BMW',petrol)
audi = Category('Audi',petrol)

category_list = [vehicle,electronics,car,tv,petrol,sony,bmw,audi]

for category in category_list:
    category.display_category()