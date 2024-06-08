# problem 6: how many times sorted array rotated 
def sol(arr):
    n=len(arr)
    lo,hi=0,len(arr)-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        
        nx=(mid+1)%n
        #print(nx)
        pv=(mid-1+n)%n
        if arr[mid] < arr[pv] and arr[mid] < arr[nx]:
            #print(nx)
            return mid
        elif arr[mid] < arr[hi]:
            hi= mid -1
        else:
            lo=mid+1  

print(sol([2,5,6,7,8]))
