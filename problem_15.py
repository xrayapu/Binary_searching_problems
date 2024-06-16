# problem 15: find peak element's  index in unsorted array

#[1,2,3,1] peak element is 3, it's index 2. output : 2

# peak element-> both it's side elements are smaller then it,
# arr[0] > arr[1] and arr[len(arr)-1] > arr[len(arr)-2] , if this true, edge case
#then they are also peak elements 

def sol(arr):
    lo, hi= 0, len(arr)-1
    if len(arr)==1:
        return 0
    elif arr[0] > arr[1]:
        return 0
    elif arr[hi] > arr[hi-1]:
        return hi
    else:
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
                lo = mid+1
            else: hi = mid

print(sol([1,2,3,1]))
