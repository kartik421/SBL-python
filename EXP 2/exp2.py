a=int (input("enter the number 1:"))
b=int (input("enter the number 2:"))
c=int (input("enter the number 3:"))

if (a>b and b>c):
    print("max is", a)

elif (b>a and b>c):
    print("max is ",b)

else:
    print("max is",c)

if(a%2==0):
    print("even")

else:
    print("odd")

print("to find the first 10 natural numbers")
for i in range (1,11,1):
    print(i)


