x=3
y=4
def myfunc():
    global y
    y=2
    d=5
    print(d)
    print(y)
myfunc()
print(x,y)
print(y)    