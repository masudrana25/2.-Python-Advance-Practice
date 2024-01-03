import re

#### first letter a "aeiou" er moddhy j kono akta thaklei match korbey 

# if re.match('[aeiou]','usud'):
#   print('Match')
# else :
#   print('No match')

# if re.match('[aeiou]','isud'):
#   print('Match')
# else :
#   print('No match')

## not match
# if re.match('[aeiou]','hsud'):
#   print('Match')
# else :
#   print('No match')

#### small "a" theky small "z" porjonto j kono character thaklei match korbey

# if re.match('[a-z]','hsud'):
#   print('Match')
# else :
#   print('No match')

# if re.match('[A-Z]','hsud'):
#   print('Match')
# else :
#   print('No match')

# if re.match('[A-Z]','Hsfdfhgd'):
#   print('Match')
# else :
#   print('No match')

#### [0-9] er moddhy j kono number start a thakley match korby

# if re.match('[0-9]','0sfdfhgd'):
#   print('Match')
# else :
#   print('No match')

# if re.match('[0-9]','7sfdfhgd'):
#   print('Match')
# else :
#   print('No match')

###### [A-Z][a-z][0-9] = serially 3 ta sorto match korlei kabol match korby

# if re.match('[A-Z][a-z][0-9]','Ab9fgdhhgh'):
#   print('Match')
# else :
#   print('No match')

# if re.match('[A-Z][a-z][0-9]','aA9fdsgsfdgf'):
#   print('Match')
# else :
#   print('No match')

