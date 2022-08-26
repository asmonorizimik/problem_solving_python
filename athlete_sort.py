nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k=int(input())
arr.sort(key=lambda x: x[k])
i=0
while i<len(arr):
    j=0
    s=""
    while j<len(arr[i]):
        s+=str(arr[i][j])+" "
        j+=1
    print(s)
    i+=1






# Sample Input 0
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# Sample Output 0
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
# Explanation 0
# The details are sorted based on the second attribute, since K is zero-indexed.

# Output Format
# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.