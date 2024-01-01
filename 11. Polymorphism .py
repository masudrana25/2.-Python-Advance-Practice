# polymorphism = bohu-rup

# Build-in polymorphic functions
print( len('I am polymorphic'))
print( len( [1,2,3,4,5]))
# here "len" is a polymorphic function because "len" aki sathy akathik jinis a kaj korey. aki somoi different value niye kaj korty parry


#### user-defined polymorphic functions
def add(x,y, z=0) :
  sum = x+y+z
  return sum

print(add(20,30)) ; print(add(20,30,40))
#  aikhan a "add" akta polymorphic function = aki sathy akadhik value niye kaj korty parchy