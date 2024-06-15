# problem 10: find next alphabet in the sorted array, if not return -1

# we will try to solve same as celing problem.

# [a,b,f,h] tar: f output: h

def sol(arr, tar):
    lo,hi=0,len(arr)-1
    ans=''
    if tar >= arr[hi] : 
        return arr[0]
    while lo<=hi:
        #print(lo,hi)
        mid=lo+(hi-lo)//2
        if mid+1<= len(arr)-1 and arr[mid] == tar and arr[mid] != arr[mid+1]:
            # [e,e,e,e,e,e,e,n,n,n,n,n,n,n] -> needed 3rd condition's,tar-> e, output  -> n
            return arr[mid+1]
        elif arr[mid] > tar:
            ans= arr[mid]
            hi =mid -1
        else: lo =mid+1

    return ans

print(sol(['e','e','e','e','e','e','n','n','n','n','n'],'e'))
