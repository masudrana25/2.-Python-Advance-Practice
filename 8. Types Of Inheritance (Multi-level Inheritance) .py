class A:
  def displayA(self):
    print('i am inside A class')

class B(A):
  def displayB(self):
    print('i am inside B class')

'''
class C(B):
  def displayC(self):
    print('i am inside C class')

object1 = C()
object1.displayA() ; object1.displayB() ; object1.displayC() 
'''

class C(B) :
  def displayC(self):
    super().displayA()
    super().displayB()
    print('i am inside C class')

object2 = C()
object2.displayC()

