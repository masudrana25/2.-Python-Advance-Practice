class Phone :
  def __init__(self):
    print('I am in Phone class')

'''
class Samsung(Phone) :
  pass # Samsung a Phone method er constructor ta choley asby
s = Samsung()
'''

'''
class Samsung(Phone) : # Samsung class a Phone method er constructor ta choley asby
  def __init__(self): 
      # ager phone class thekey asa "__init__" constructor ta ai new constructor ta dara replace/ overwrite hoye jaby.
    print('I am in Samsung class')
s = Samsung()
'''

class Samsung(Phone) : # Samsung class a Phone method er constructor ta choley asby
  def __init__(self): 
    super().__init__() # super/parent class er constructor k call korbey.
    print('I am in Samsung class')
s = Samsung()