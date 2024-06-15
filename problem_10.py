# problem 10 : find the ceil of the target in the sorted array

def sol(arr, tar):
    lo, hi= 0, len(arr)-1
    ans=0
    while lo <= hi:
        #print(str(lo) +'for '+str(hi))
        mid= lo+(hi-lo)//2
        if arr[mid] ==tar:
            return tar
        elif arr[mid] > tar:
            ans= arr[mid]
            hi= mid -1
        else:
             
            lo = mid+1

    return ans

print(sol([1,2,3,4,8,10,12,15,18,20],5))
