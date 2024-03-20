a = int(input("Enter your first number "))
b = int(input("Enter your second number "))
c = int(input("Enter your third number "))
d = int(input("Enter your fourth number "))

if(a>b and a>c and a>d):
    print("a is the largest number")
elif(b>c and b>d):
    print("b is the largest number")
elif(c>d):
    print("c is the largest number")
else:
    print("d is the largest number")