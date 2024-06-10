# problem 7: searching an element in nearly sorted array.

# [5,10,30,20,40] , tar= 20

# nearly sorted array. it means, the item can be in, ith index, i-1 index, i+1 index .



def sol(arr,x):
    lo,hi= 0, len(arr)-1
    while lo <= hi:
        mid= lo+(hi- lo)//2
        if arr[mid]==x :
            return mid
        if mid-1>=0 and arr[mid-1] == x: # edge case , when mid = 0 
            return mid -1
        if mid+1<=len(arr)-1 and arr[mid+1]== x: # edge case, when mid = len(arr)
            return mid+1
        
        elif arr[mid] > x:
            hi= mid -1
        else: lo = mid+1

    return -1

print(sol([10, 3, 40, 20, 50, 80, 70],40))
