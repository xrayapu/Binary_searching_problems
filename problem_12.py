# problem_11: find position of an element in an infinite array.

# we don't know the length of array so, hi =1.

def sol(arr, tar):
    lo,hi=0,1
    while lo<=hi:
        mid= lo+(hi-lo)//2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            hi= mid-1
        else:# main factor of the whole part is here
            lo= hi 
            hi= hi *2

    return -1  

print(sol([1,2,3,4,5,6,7,8,9,12,13,17,43],4))
