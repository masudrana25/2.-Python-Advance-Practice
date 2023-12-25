class Student :
  roll = ''
  gpa = ''

rahim = Student() # rahim = object & Student = class
# Student class er vitorey "rahim" namer object create hoyechey kina check korbey
#print(isinstance(rahim, Student)) 

rahim.roll = 101; rahim.gpa = 3.45
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

karim = Student()
karim.roll = 102; karim.gpa = 4.45
print(f"Roll : {karim.roll}, GPA : {karim.gpa}")
