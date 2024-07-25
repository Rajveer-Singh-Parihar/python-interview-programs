# prime number is greater than one and have two factors 
# 1 and 19 is prime number - 1,2,3,4,5,6,7,8,9,---11,,13,17,29

num=5
count=0

if(num>1):
    for i in range(1,num+1):
        if(num%i)== 0:
            count = count+1

    if count==2:
        print("number is prime")
    else:
        print("number is not prime")