# problem 19: allocate minimum number of pages for the students.

#Given that there are N books and M students. Also given are the number of pages in each book 
#in ascending order. The task is to assign books in such a way that the maximum number of pages 
#assigned to a student is minimum, with the condition that every student is assigned to read some 
#consecutive books. Print that minimum number of pages.

def isvalid(arr,k,tar):
    student=1
    ans=0
    for i in range(len(arr)): 
        ans+=arr[i] # s1= 10 +20+30 (X)-> mid 50 , out of range and so add another student to read ! 
                    # s2= 30+40(X)
# s3= 40 , 2 students given in the question, here we get 3 ! so, we have to add more pages for 2 student
        if ans > tar:
            student+=1
            ans= arr[i]

    return student == k

def sol(arr,k):
    ans=-1
    lo= max(arr) # minimum 1 book, that's why biggest number ! 
    hi= sum(arr)
    if len(arr) < k:
        return -1
    while lo<= hi:
        mid= lo+(hi-lo)//2 # max number of pages will never cross mid number 
        
        if isvalid(arr,k,mid)== True: # check if student number is valid ! 
                                    #then try to find more minimum pages for students !!!  
            ans= mid
            hi= mid -1
        else: lo= mid+1
    return ans

print(sol([12, 34, 67, 90],5))
