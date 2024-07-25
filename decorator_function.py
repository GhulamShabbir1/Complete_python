def greet(fx):
    def mfx():
        print("Hello from inner function")
        fx()
        print("Goodbye from inner function")
    return mfx  
@greet
def hello():
    print("Hello from outer function")
# hello()    

# For argumental function
def greet(fx):
    def mfx(*args,**kwargs):
        print("Hello from inner function")
        fx(*args,**kwargs)
        print("Goodbye from inner function")
    return mfx  
def hello1(a,b):
    print(a+b)
greet(hello1) (1,4)  




