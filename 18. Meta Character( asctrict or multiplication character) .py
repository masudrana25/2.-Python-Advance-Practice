# "*"
import re

# "*" zero or j kono sonkhok oi character ta thaktey parbey
# aikhan a zero or j kono sonkhok "a" character ta thaktey parbey
# if re.match('a*','color') :
#   print('Matched') 
# else:
#   print('Not matched')

# if re.match('a*','aacolor') :
#   print('Matched') 
# else:
#   print('Not matched')

# "ab" zero or j kono sonkhok bar thaktey parbey
if re.match('(ab)*','aacolor') :
  print('Matched') 
else:
  print('Not matched')

