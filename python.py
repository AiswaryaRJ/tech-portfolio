planet="Pluto is a planet"
print(planet)
s=planet.split()
print(s)
date= "2024-06-01"
print(date)
w=date.split('-')
print(w)
d='/'.join(w)
print(d)
n=9
result=planet + " hello " + str(n) + 'hi'
print(result)
r="{} hello {} hi" .format(planet,n)
print(r)
"""from math import * helps as from not using math.pi etc each time just  use pi directly
nimpy and math  has some common functions but nimpy is more powerful than math so numpy might  overight so  use from math/numpy(whatever) import specific function to avoid this problem"""