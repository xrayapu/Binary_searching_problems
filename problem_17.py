
# biotonic means: stright increasing , get to a pick element , then stright decreasing .

# 1,3,5,6,7,4,3,1 -> bitonic . 1,3,4,5,6,7,7,5,3,2,1 -> not bitonic 

# problem 17: search an element's index in boitonic array
# 1st find the peak element of the boitonic array then just search through binary search

def helper(arr):
    lo,hi=0, len(arr)-1
    while lo<= hi:
        mid=lo+(hi-lo)//2
        if arr[mid-1] < arr[mid] >arr[mid+1]:
            return mid
        elif arr[mid-1] < arr[mid]<arr[mid+1]:
            lo=mid+1
        else: hi= mid

    return 0
def helper_bs(arr,lo,hi,tar):
    while lo<= hi:
        mid= lo+(hi-lo)//2
        if arr[mid]== tar:
            return mid
        elif arr[mid]> tar:
            hi= mid-1
        else: lo=mid+1

    return -1
    
def helper_bs1(arr,lo,hi,tar): # decreasing part
    while lo<= hi:
        mid= lo+(hi-lo)//2
        if arr[mid]== tar:
            return mid
        elif arr[mid]> tar:
            lo= mid+1
        else: hi=mid-1

    return -1

def sol(arr, tar):
    index= helper(arr)
    left= helper_bs(arr,0,index,tar)
    right=helper_bs1(arr,index+1,len(arr)-1,tar)
    return right+left+1


print(sol([1,2,5,9,4],11))
