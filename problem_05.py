# problem 4: count the element in the sorted array
from collections import Counter
def solution_1(arr, el):
    x= Counter(arr)
    if el not in arr:
        return -1
    return x[el]

print(solution_1([1,2,2,2,3,4],1))

# using binary search -> just last occurence and 1st occurence +1 , we will get the count.
def bs_left(arr,x):
    lo=0
    hi=len(arr)-1
    while lo<= hi:
        mid = lo+(hi-lo)//2
        if arr[mid]==x :
            if mid==0 or arr[mid-1] !=x:
                return mid
            else: hi= mid-1

        elif arr[mid] > x:
            hi= mid-1

        else: lo = mid+1

    return -1
def bs_right(arr,x):
    lo=0
    hi=len(arr)-1
    while lo<= hi:
        mid = lo+(hi-lo)//2
        if arr[mid]==x :
            if mid==len(arr)-1 or arr[mid+1] !=x:
                return mid
            else: lo= mid+1

        elif arr[mid] > x:
            hi= mid-1

        else: lo = mid+1

    return -1
def sol(arr, x):
    left= bs_left(arr,x)
    right= bs_right(arr,x)
    return right-left+1

print(sol([1,2,2,2,3,4],2))
