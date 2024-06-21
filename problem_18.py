# problem 18: search the element in 2d matrix , if find return true else return false
#            | a[0][n-1] -> check with target ! if tar is > , then i++, if not then j-- 
#[[1,4,7,11,15],
# [2,5,8,12,19],
# [3,6,9,16,22],
#[10,13,14,17,24],
#[18,21,23,26,30]]
# tar: 5

# def sol(arr,x):
#     i=0 
#     n= len(arr[0])
#     m=len(arr)
#     j= n-1
#     while i < m and j>=0:
#         if arr[i][j] == x:
#             return True
#         elif arr[i][j] > x:
#             j-=1
#         else: i+=1

#     return False
# print(sol([[11],[0]],1))
