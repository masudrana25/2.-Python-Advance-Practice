# constructor = a types of method = aita declared korer somoi e input parameter deya jai . extra declared korer por abar "set_value" korey parameter gula input deya lagy na.  
# class er vitorey method er poribortey constructor use kora jai. 
class Student :
  def __init__(self,roll,gpa) :
    self.roll = roll; self.gpa = gpa
  
  def display(self): # methods or function in class
    print(f"Roll : {self.roll}, GPA : {self.gpa}")

rahim = Student(101,3.45)
rahim.display()

karim = Student(102,4.55)
karim.display()
