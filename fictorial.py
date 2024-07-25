x=5
if x==0 or x==1:
    print("1")
else:
    fact=1
    for i in range(x):
        fact=fact*x
        x=x-1

print("the factorial of a number is ",fact)



def name(*name):
    print("Hello",name[0],name[1])
name("ghulam Shabbir","Shadab Ali")


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")



# fabonacci Sequence

n=100

f=[0,1]
f[0]=0
f[1]=1
for i in range(2,n):
    f.append(f[i-1]+f[i-2])
print(f)

