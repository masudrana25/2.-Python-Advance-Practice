class Shape() :
  def __init__(self,dim1,dim2) :
    self.dim1 = dim1; self.dim2 = dim2
  def area(self):
    print('I am area method in Shape class.')

class Rectangle(Shape) : 
  def area(self):
    area = 0.5 * self.dim1 * self.dim2
    print('Area of Rectangle is = ',area)

class Triangle(Shape) :
  def area(self):
    area = self.dim1 * self.dim2
    print('Area of Triangle is = ',area)

rectangle1 = Rectangle(20,30) ; rectangle1.area()
triangle1 = Triangle(20,30) ; triangle1.area()