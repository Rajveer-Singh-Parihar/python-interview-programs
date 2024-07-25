a = int(input(" enter the first number"))
b = int(input(" enter the first number"))
c = int(input(" enter the first number"))

if (a>b and a>c):
    max = a
elif (b>a and b>c):
    max=b
else:
    max =c 

print(" maximum of three numbers is ", max)