# # Function to print all quadruplet present in a list with a given sum
# 2 inputs: #array  and int number for the target sum
# 1 2 3 4 5 6 7 0 9 6
# 8 
# sum output: 
# [0, 1, 2, 5]
# [0, 1, 3, 4]


# def quadTuple(A, target):
 
#     # sort the list in ascending order
#     A.sort()
 
#     # check if quadruplet is formed by `A[i]`, `A[j]`, and a pair from
#     # sublist `A[j+1…n)`
#     for i in range(len(A) - 3):
#         for j in range(i + 1, len(A) - 2):
 
#             # `k` stores remaining sum
#             k = target - (A[i] + A[j])
 
#             # check for sum `k` in sublist `A[j+1…n)`
#             low = j + 1
#             high = len(A) - 1
 
#             while low < high:
#                 if A[low] + A[high] < k:
#                     low = low + 1
#                 elif A[low] + A[high] > k:
#                     high = high - 1
#                 # quadruplet with a given sum found
#                 else:
#                     print((A[i], A[j], A[low], A[high]))
#                     # low+=1
#                     # high-=1
#                     (low, high) = (low + 1, high - 1)
 
 
# if __name__ == '__main__':
 
#     A = list(map(int,(input().split())))
#     target = int(input())

#     quadTuple(A, target)
 



# def quadruple(arr,target):
#     arr.sort()
#     i=0
#     while i<len(arr):
#         j=i+1
#         while j<len(arr):
#             remaining_sum=target-(arr[i]+arr[j])
#             low=j+1
#             high=len(arr)-1
#             while low<high:
#                 if arr[low]+arr[high]<remaining_sum:
#                     low+=1
#                 elif arr[low]+arr[high]>remaining_sum:
#                     high-=1
#                 else:
#                     print([arr[i],arr[j],arr[low],arr[high]])
#                     low+=1
#                     high-=1
#             j+=1
#         i+=1
# arr=list(map(int,input().split()))
# target=int(input())
# quadruple(arr,target)




# str=""
# for Row in range(0,7):
#     for Col in range(0,7):
#         if Col == 1 or ((Row == 0 or Row == 3 or Row == 6) and (Col < 5 and Col > 1)) or (Col == 5 and (Row != 0 and Row != 3 and Row != 6)):
#             str=str+"*"
#         else:
#             str=str+" "
#     str=str+"\n"
# print(str)




print(13*18)