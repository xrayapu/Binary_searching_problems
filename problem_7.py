# problem 7: find a element on the rotated sorted array.

# arr=[11,12,14,15,2,3,4,6], target= 15, output= 3[index of 15] , if not found give -1
# [11,12,14,15] <->[2,3,4,6]
# 1st find small element's index , then try binary search to find target element
# small element's index helper
# step 2: 
    #1st element detect in mid possition
    # 2nd which side to go
def helper(arr):
    lo=0
    n= len(arr)
    hi=n-1
    while lo <= hi:
        mid = lo+(hi- lo)//2
        prv= (mid-1+n)% n
        nx= (mid+1) % n
        # small element's index 
        if arr[mid] < arr[prv] and arr[mid] < arr[nx]: 
            return mid
        elif arr[mid] < arr[hi]:
            hi = mid-1
        else: lo= mid+1

def helper_bs(arr, lo, hi,x):
    while (lo<= hi):
        mid= lo +(hi-lo)//2
        # if found return mid
        if arr[mid] ==x:
            return mid 
        #try mid's left side  [11,12,14,15],x=15
        # 12<15
        elif arr[mid] < x: 
            lo = mid+1

        else: hi= mid -1

    return -1 # if not found then -1


# main part of the code
def sol(arr, tar):
    small_index= helper(arr)
    left= helper_bs(arr,0,small_index-1,tar)
    right=helper_bs(arr,small_index,len(arr)-1,tar)
    return left+right+1 #left/right will get -1, so that's why +1 

print(sol([11,12,14,15,2,3,4,6],4))
