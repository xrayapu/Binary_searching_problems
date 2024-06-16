# problem 12: find the 1st 1 binary sorted infinite array.

# 1st find 1 in infinite array then find the 1st one .

def sol(arr, tar):
    lo,hi=0,1
    while lo<=hi:
        mid= lo+(hi-lo)//2
        if arr[mid] == tar :
            if mid >0 and arr[mid-1] != tar : # binary sorted array, so [0] must have to in the array ! if not return -1
              
                return mid
            else: hi = mid -1
        elif arr[mid] > tar:
            hi= mid-1
        else:
            lo= hi 
            hi= hi *2

    return -1  
print(sol([0,0,1,1,1,1,1],1))
