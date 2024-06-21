#problem 16: find maximum element in the bitonic array. 
# biotonic means: stright increasing , get to a pick element , then stright decreasing .

# 1,3,5,6,7,4,3,1 -> bitonic, output-> 7 . 1,3,4,5,6,7,7,5,3,2,1 -> not bitonic 

def sol(arr):
    lo,hi=0, len(arr)-1
    while lo<= hi:
        mid=lo+(hi-lo)//2
        if arr[mid-1] < arr[mid] >arr[mid+1]:
            return arr[mid]
        elif arr[mid-1] < arr[mid]<arr[mid+1]:
            lo=mid+1
        else: hi= mid

    return 0

print(sol([1,2,5,9,4]))
