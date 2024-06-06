# 1st and last occurence of the element in array.

def bs_left(arr,x):
    lo,hi=0,len(arr)-1
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if arr[mid] ==x:
            if mid ==0 or arr[mid-1] != x:
                return mid
            else: hi = mid -1

        elif arr[mid] > x: 
            hi= mid-1
        else:
            lo = mid +1

    return -1

def bs_right(arr,x):
    lo,hi=0,len(arr)-1
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if arr[mid] ==x:
            if mid ==len(arr)-1 or arr[mid+1] != x:
                return mid
            else: lo = mid +1

        elif arr[mid] > x: 
            hi= mid-1
        else:
            lo = mid +1

    return -1


def sol(arr,x):

    left= bs_left(arr,x)
    right= bs_right(arr,x)
    return [left, right]


