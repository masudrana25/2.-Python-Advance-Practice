# "(-)?"
import re

# "(-)?" zero or one sonkhok oi character/"-" ta thaktey parbey
# aikhan a one or zero sonkhok "-" character ta thaktey parbey
# if re.match('ice(-)?cream','ice-cream') :
#   print('Matched') 
# else:
#   print('Not matched')

if re.match('ice(-)?cream','ice--cream') :
  print('Matched') 
else:
  print('Not matched')

