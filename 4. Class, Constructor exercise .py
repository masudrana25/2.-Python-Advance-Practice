class Triangle () :
  def __init__(self,base, height) :
    self.base = base ; self.height = height 

  def calculate_area(self) :
    area = 0.5 * self.height * self.base
    print('Area of Triangle : ',area)

t1 = Triangle(10,20); t1.calculate_area()
t2 = Triangle(20,30); t2.calculate_area()