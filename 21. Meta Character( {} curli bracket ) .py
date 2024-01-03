# "{}"
import re

# "a{1,3}$" minimum 1 bar and maximum 3 bar "a" thaktey parbey
# if re.match("a{1,3}$",'a') :
#   print('Matched') 
# else:
#   print('Not matched')

# if re.match("a{1,3}$",'aaa') :
#   print('Matched') 
# else:
#   print('Not matched')

# if re.match("a{1,3}$",'aaaa') :
#   print('Matched') 
# else:
#   print('Not matched')

# must por por "a" k thaktey hby
if re.match("a{1,3}$",'agahatt') :
  print('Matched') 
else:
  print('Not matched')
