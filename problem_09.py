# problem 9: find floor of the element in sorted array

# [1,2,3,4,8,10,12,15,18,20] ,tar =5 ,=> output: 4

# if mid== tar: then we just return the target. if not found in the array, then we return 

#the max number which is less then the target.   

def sol(arr, tar):
    lo, hi= 0, len(arr)-1
    ans=0
    while lo <= hi:
        mid= lo+(hi-lo)//2
        if arr[mid] ==tar:
            return tar
        elif arr[mid] > tar:
            hi= mid -1
        else:
            ans= arr[mid] # tell us to find floor , that's why, we store the (mid/ number) here ! 
            lo = mid+1

    return ans

print(sol([1,2,3,4,8,10,12,15,18,20],5))
