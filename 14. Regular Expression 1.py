import re # regular expression import korlam

pattern =r"color" # string ta row hobey

# re.match = match only at the beginning of the string
# if re.match(pattern,"Red is a color, it is beautiful.") :
#   print('Match')
# else : 
#   print('Not Match')

# if re.match('col',"color is a color, it is beautiful.") :
#   print('Match')
# else : 
#   print('Not Match')


# re.search = puro string er vitorey search korbey
# if re.search(pattern,"Red is a color, it is beautiful color.") :
#   print('Match')
# else : 
#   print('Not Match')

# re.findall = jotobar kono akta string khujey pabey, takey niye akta list banabey
# search_list = re.findall('color',"Red is a color, it is beautiful color.")
# search_list = re.findall('col',"Red is a color, it is beautiful color.")
# search_list = re.findall('i',"Red is a color, it is beautiful color.")
# print(search_list)
