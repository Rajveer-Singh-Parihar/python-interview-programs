arr = [ 1,2,3,4,5,6,7] # 7
min = arr[0]

n=len(arr)

for i in range(1,n):
    if arr[i]<max:
        min = arr[i]

        print(min)