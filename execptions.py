# Sample Input
# 3
# 1 0
# 2 $
# 3 1

# Sample Output
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3






# n=int(input())
# i=0
# while i<n:
#     try:
#         a,b=input().split()
#         print(int(a)//int(b))
#     except ZeroDivisionError as e:
#         print("Error Code:",e)
#     except ValueError as d:
#         print("Error Code:",d)
#     i+=1





# s=input()
# x=eval(s)


# N,n = int(input()),input().split()
# print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))


