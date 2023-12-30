class Phone :
  def call (self) :
    print('You can Call')
  def message(self) :
    print('You can Message')
# phn1 = Phone(); phn1.call();phn1.message()

'''
class Samsung :
  def call (self) :
    print('You can Call')
  def message(self) :
    print('You can Message')
  def photo(self) :
    print('You can take Photo')
phn2 = Samsung(); phn2.call();phn2.message();phn2.photo()
'''

class Samsung(Phone) :
  # Phone Class er Methods gula automatically Samsung class er moddhey choley asby.
  def photo(self) :
    print('You can take photos')
phn2 = Samsung(); phn2.call();phn2.message();phn2.photo()

# Phone = Super_Class / Parent_Class / Base class  
# Samsung = Sub_Class / Child_Class / Derived class
print(issubclass(Samsung, Phone)) # Samsung ki Phone er sub class ? check korby
print(issubclass( Phone, Samsung))