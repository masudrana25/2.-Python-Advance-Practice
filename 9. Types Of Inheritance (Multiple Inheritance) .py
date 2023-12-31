class A:
  def display(self):
    print('i am inside A class')

class B():
  def display(self):
    print('i am inside B class')

# class C(A,B) : # A er method k call korby
#   pass

# class C(B,A) : # B er method k call korbey
#   pass

# class C(A,B) :
#   def display(self):
#     print('i am inside C class')

object2 = C()
object2.display()

