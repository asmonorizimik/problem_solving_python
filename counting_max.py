# arr=[3,2,1,3]
# # arr=[3,5,10,8,9,5,10,10]
# def birthdayCakeCandles(arr):
#     i=0
#     max=arr[i]
#     while i<len(arr):
#         if arr[i]>max:
#             max=arr[i]
#         i+=1
#     j=0
#     c=0
#     while j<len(arr):
#         if max ==arr[j]:
#             c+=1
#         j+=1
#     return c
# arr=list(map(int, input().rstrip().split()))
# print(birthdayCakeCandles(arr))




# Returns
# int: the number of candles that are tallest

# Sample Input 0
# 4
# 3 2 1 3

# Sample Output 0
# 2

# Explanation 0

# Candle heights are [3,2,1,3] . The tallest candles are 3 units, and there are 2 of them.

