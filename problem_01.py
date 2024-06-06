# binary search normal implementation
def sol(arr, x):
    lo=0
    hi=len(arr)
    while lo<= hi:
        mid=lo+ (hi-lo)//2 # mid = (lo +hi )//2 is not used because it gives overflow problems, so it's safe in this way.
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            hi = mid-1

        
        elif arr[mid] < x: 
            lo= mid +1

    return -1
    
