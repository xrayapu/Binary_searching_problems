# search an element in reversed array.

def sol(arr, x):
    lo=0
    hi=len(arr)-1
    while lo<= hi:
        mid=lo+ (hi-lo)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            lo = mid+1

        else:
          hi = mid -1 

    return -1

#print(sol([11,10,9,7,4,3,2,1],1)) # output:7
