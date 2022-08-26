# A recursive solution for subset sum
# problem
  
# Returns true if there is a subset
# of set[] with sun equal to given sum
  
  
# def isSubsetSum(set, n, sum):
  
#     # Base Cases
#     if (sum == 0):
#         return True
#     if (n == 0):
#         return False
  
#     # If last element is greater than
#     # sum, then ignore it
#     if (set[n - 1] > sum):
#         return isSubsetSum(set, n - 1, sum)
  
#     # else, check if sum can be obtained
#     # by any of the following
#     # (a) including the last element
#     # (b) excluding the last element
#     return isSubsetSum(
#         set, n-1, sum) or isSubsetSum(
#         set, n-1, sum-set[n-1])
  
  
# # Driver code
# set = [3, 34, 4, 12, 5, 2]
# sum = 8
# n = len(set)
# if (isSubsetSum(set, n, sum) == True):
#     print("Found a subset with given sum")
# else:
#     print("No subset with given sum")
  
# # This code is contributed by Nikita Tiwari.




# input:
# 12 2 34 5 2 6 4
# 14
# output:
# the subset sum of 14 is:  (2, 12)



def subsetsum(arr,sum):
    i=0
    while i<len(arr):
        j=0
        while j<len(arr):
            if arr[i]+arr[j]==sum:
                p=arr[i]+arr[j]
                s=((arr[i]),arr[j])
            j+=1
        i+=1
    if p==sum:
        print("the subset sum of",sum,"is: ",s)
    else:
        print("there is no subset")
arr=list(map(int,input().split()))
sum=int(input())
subsetsum(arr,sum)



