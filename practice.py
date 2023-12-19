# 1>
""" 
a=int(input("Enter degree in celcius: "))
print("Fahrenheit= ",((a*9)/5)+32) """

# 2>
""" 
a=int(input("Enter the number of lines: "))
b=0
for i in range(1,a+2,1):
    print("")
    for j in range(1,i,1):
        b+=1
        print(b,end="\t")
 """

#  3>
""" 
a=10
for i in range(0,a,1):
    for j in range(0,2*i-1,1):
        print(" ",end="")
    for k in range(0,a-i,1):
        print(" *",end=" ")
    print()
     """
#4
""" 
a=int(input("Enter the number to check prime: "))
b=0
c=0
for i in range(2,int(a/2),1):
    if(a%i==0):
        c=i
        b=1
        
if(b==0):
    print(a," is prime")
elif(b==1):
    print(a," is not prime,it is divisible by ",c)
 """

#  5>
""" 
a=0
p=0
c=0
while(a!=-1):
    a=int(input("Enter the number: "))
    b=1
    for i in range(2,int(a/2),1):
        if(a%i==0):
            b=0
    if(b==1):
        p+=1
    else:
        c+=1
print("Prime number count= ",p)
print("Composite number count= ",c)
 """

 #6
""" 
a=input("Enter string: ")
b=a [::-1]
if(a==b):
    print("Palindrome")
else:
    print("Non-Palindrome")
 """

#7
""" 
a=input("Enter string: ")
b=a[len(a)-1]
print(a)
for i in range(0,len(a)-2,1):
    if(a[i]==b):
        a[i]='*'
    b.append(a[i])
print(b)
 """
 #8>
""" 
l=[1,2,3,4,5,7,8]
l1=[2,34,2,3,4,5]
l3=[]
for i in range(0,len(l)-1,1):
    b=0
    for j in range(0,len(l1)-1,1):
        if(l[i]==l1[j]):
            b=1
    if(b==0):
        l3.append(l[i])
print("l1",l)
print("l2",l1)
print("l3",l3)
 """

#9>
""" 
a,b=input("Enter 1st number: "),input("2nd number: ")
try:
    print(int(a)+int(b))
except: 
    print("String and number cannot be added") """

try:
    f=open('F.txt')
    print('File is opened successfully')
    print('File Nmae:',f.name)
    print('File mode:',f.mode)
    print('Closed:',f.closed)
    f.close()
    print('Closed:',f.closed)
except:
    print('File does not exist')
    print('Check file name')