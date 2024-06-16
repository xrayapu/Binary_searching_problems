# problem 14: minimum difference of the element in sorted array.

# [4,6,8]tar: 6 -> output: 6
# 6,6,6 (subtraction with target)
# 2,0, 2 (output of the subtraction)
# -,|,- (chose the closest element)
# [4,6,9] tar: 7 -> output: 6

def helper(arr,k):
    lo, hi =0, len(arr)-1
    while(lo <= hi):
        mid = lo +(hi -lo)//2
        if arr[mid]== k:
            return mid 
            
        elif arr[mid]> k:
            hi= mid-1
        else: lo = mid +1

    return lo

def sol(arr, tar):
    it= helper(arr, tar)
    #print(it)
    no1= abs(arr[it] - tar)
    no2=abs(arr[it-1] - tar)
    if no1 > no2: return arr[it -1]
    else : return arr[it]

print(sol([4,7,8,9,12],5))
