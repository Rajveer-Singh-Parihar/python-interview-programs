#input : 153 -- 1*1*1 5*5*5* 3*3*3 = 153
# output: ARMSTRONG NUMBER
n=int(input("enter a number")) # 153
temp = n #153
sum = 0
while n>0: # 153>0
    r=n%10 # remainder 3 
    sum = sum+r*r*r # 3*3*3=27  5*5*5=125 1*1*1=1 ---- 27+125+1=153
    n=n//10 # n = 15

    if temp==sum:
        print("ARMSTRONG NUMBER")
    
    else:
        print("not armstrong number")