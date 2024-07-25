# input = 4567
# add = 22
n = int(input(" enter a number"))
sum=0

while n>0: # 341>0
    r=n%10 # 1 4 3
    sum=sum+r #1+4 = 5+3 -8 ANS
    n=n//10 #34 #3
    print(" sum of digits :",sum)