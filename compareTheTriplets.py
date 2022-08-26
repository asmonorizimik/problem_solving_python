# Sample Input 0
# 5 6 7
# 3 6 10

# Sample Output 0
# 1 1


# Sample Input 1
# 17 28 30
# 99 16 8

# Sample Output 1
# 2 1

# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.


# def compareTriplets(a, b):
#     i=0
#     a_score=0
#     b_score=0
#     while i<len(a) or i<len(b):
#         if a[i]>b[i]:
#             a_score+=1
#         elif b[i]>a[i]:
#             b_score+=1
#         else:
#             a_score=0
#             b_score=0
#         i+=1
#     x=[a_score,b_score]
#     return x
# a = list(map(int, input().rstrip().split()))
# b = list(map(int, input().rstrip().split()))
# print(compareTriplets(a,b))



def compareTriplets(a, b):
    i=0
    a_score=0
    b_score=0
    while i<len(a) or i<len(b):
        if a[i]>b[i]:
            a_score+=1
        elif b[i]>a[i]:
            b_score+=1
        i+=1
    return str(a_score)+" "+str(b_score)
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
print(compareTriplets(a,b))

