class Rectangle :

    def __init__(self) :
        self.length =(int(input("Enter length:")))
        self.width = (int(input("Enter width:")))

    def perimeter(self) :
        return 2 * (self.length + self.width)

    def area(self) :
        return self.length * self.width

    def display(self) :
        print("Length is:", self.length)
        print("width is:", self.width)
        print("Perimiter is:", self.perimeter())
        print("Area is:", self.area())

obj = Rectangle()
obj.display()
