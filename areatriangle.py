# AREA OF TRIANGLE =area- (s*(s-a)*(s-b)*(s-c))**)0.5
# SEMI PERIMETER = s - (a+b+c)/2

a = int(input("enter first side "))
b = int(input("enter first side "))
c = int(input("enter first side "))

s = (a+b+c)/2 #9
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(" area of trinagle ",area)