# ".","^", "$"
import re

 # . er jaigai j kono character thaklei match korbey
# if re.match('colo.r','colour') : 
#   print('Match')

 # .. er jaigai j kono 2ta character thaklei match korbey
# if re.match('colo..r','colobur') : 
#   print('Match')

# if re.match('colo..r','colobaur') : 
#   print('Match')
# else : 
#   print('Not Match')

# "^" = surutey ar chinher porer tuku thakai lagby "." er ager tuku porjonto.
# "$" = er ager letter ta must thakai lagby
# first er "colo" must match korty hby, tarpor j kono 2ta character thakbey, r last a must "r" thakty hby
# if re.match('^colo..r$','colobar') : 
#   print('Match')
# else : 
#   print('Not Match')

# if re.match('^colo..r$','colobah') : 
#   print('Match')
# else : 
#   print('Not Match')

if re.match('^colo..r$','coltbar') : 
  print('Match')
else : 
  print('Not Match')