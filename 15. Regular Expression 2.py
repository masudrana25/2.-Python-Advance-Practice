import re
pattern = r'name'
text = 'My name is Masud, I am 23 years old.'

match = re.search(pattern, text)
if match:
  print(match.start()) # match string er starting letter er index dekhabey
  print(match.end()) # match string er ending letter er index dekhabey
  print(match.span()) # match string er starting and ending letter er index dekhabey aksathy



