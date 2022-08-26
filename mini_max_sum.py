# arr=[1,3,5,7,9]
# the minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24

# Sample Input
# 1 2 3 4 5
# Sample Output
# 10 14



arr=[7, 69, 2, 221, 8974]
arr.sort()
max_sum=(arr[1:])
min_sum=(arr[:-1])
min=0
max=0
i=0
while i<len(max_sum) or i<len(min_sum):
    min+=min_sum[i]
    max+=max_sum[i]
    i+=1
print(min,max)
