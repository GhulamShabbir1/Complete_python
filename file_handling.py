# f=open('myfile.txt','r') #read if you open read mood then you only read
# print(f)
# text=f.read()
# print(f)
# f.close()
# # rb means you want to open file in binary and this is for jpg and for picture

# f=open('myfile.txt','w') #write if you on file that not exit then file is create by python
# f.write("this is new content in this file ")
# f.close()

# f=open('myfile.txt','a') #append mean add new content in the respective file
# f.write("this is another new content in this file ")
# f.close()

# #modern system includes 
# with open('myfile.txt','a') as f:
#     f.write("hello")

# # readline method is use to read file line by line
# f=open('myfile.txt','r')
# while True:
#     line=f.readlines()
#     print(line)
#     if not line:
#       break

# # sometime we need to read a values so we use 
f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    
    if not line:
      break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]

print(f"the marks of student {0} is :{m1}")
print(f"the marks of student {1} is :{m2}")
print(f"the marks of student {2} is :{m3}")
print(line)

#writeliness

t=open('myfile.txt','w')
lines=['lines1\n','lines1\n','lines1\n']
f.writeliness(lines)
f.close()

#seek() used to give a order where you start reading eg seek(3) means start read from first 4
#tell()  tell number of character to read  onword from seek

f=open('myfile.txt','r')
f.seek(3)
print(f.tell())
print(f.readline())
print(f.tell())

#truncate is used to set size of file
f=open('myfile.txt','r')
f.truncate(5)
print(f.read())
f.close()

