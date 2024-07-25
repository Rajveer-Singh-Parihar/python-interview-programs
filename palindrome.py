# input  121 --- 121 
n = int(input(" enter a number"))
temp = n #141
sum = 0
while n>0: # 141>0
    r=n%10 # remainder 1
    sum=sum*10+r #1 - 4 - 1 = 141
    n=n//10 # 14 1

    if temp==sum:
        print("palindrome number")
    else:
        print(" not a palindrome number ")