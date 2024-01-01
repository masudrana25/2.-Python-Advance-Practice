# starts with "__" and ends with "__" = double underscore
# __lt__ ->  < (less than)
# __le__ ->  <= (less than or equal to)

# __gt__ ->  > (greater than)
# __ge__ ->  >= (greater than or equal to)

# __eq__ ->  == (equal to)
# __ne__ ->  != (not equal to)

class Bike:

  def __init__(self,name,color) :
    self.name = name; self.color = color

  def __str__(self):
    return (f"Name : {self.name}, color : {self.color}")
  
  def __eq__(self, other) :
    return self.name == other.name and self.color == other.color

  def display(self):
    print(f"Name : {self.name}, color : {self.color}")
  
bike1 = Bike('Yemaha', 'Blue')
bike2 = Bike('Honda', 'Red')
# bike1.display()
# print(str(bike1)) ; print(str(bike2))
print(bike1 == bike2) # == ta class ar magic method k call korby. alada korey oi method k call korty hocchy na


