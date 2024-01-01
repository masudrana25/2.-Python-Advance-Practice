# abstract method = j method er body nai = j method faka 
# abstract class = j class a abstract method achy
#### abstract class k inherit korley or onno kono class a use korley, sei abstract class ar abstract method k obossoi use korty hby or newly defined korty hby . noiley error asby.
#### abstract class k kokono call kora jai na. Inherit hisebey use kora hoi sudu

from abc import ABC, abstractmethod

class Shape(ABC) :
  def __init__(self,dim1,dim2):
    self.dim1 = dim1; self.dim2 = dim2
  
  @abstractmethod
  def area(self) :
    pass

# object1 = Shape(10,20) 
# abstract class k kokono call kora jai na. Inherit hisebey use kora hoi sudu
  

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