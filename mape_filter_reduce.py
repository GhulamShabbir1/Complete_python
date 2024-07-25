def func(a):
    return a*a*a

print(func(3))

list1=[1,2,3,4,5,6,7,8,9]
#map
newl=list(map(func,list1))
print(newl)

#fiter

y=lambda x:x+3
newl1=filter(y,list1)
print(newl1)

#reduce reduce function need to import 
from functools import reduce
newl2=reduce(lambda x,y:x+y,list1)
print(newl2)
