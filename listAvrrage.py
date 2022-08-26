# Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]


l=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# li=[]
# li1=[]
# li2=[]
# i=0
# while i<len(l):
#     print(len(l[i]))
#     if len(l[i])==5:
#         li.append(l[i])
#     if len(l[i])==4:
#         li1.append(l[i])
#     if len(l[i])==3:
#         li2.append(l[i])
#     i+=1
# li3=li+li1+li2
# print(li3)

i=0
l2=[]
while i<len(l):
    j=0
    l1=[]
    le=len(l[i])
    while j<len(l):
        l1.append(l[j-le][i-le])
        j+=1
    # print(l1)
    sum=0
    k=0
    while k<len(l1):
        sum+=l1[k]
        k+=1
    a=sum/len(l1)
    l2.append(a)
    i+=1
    # print(l2)
print(l2)










# def average(d,i):
#     sum=0
#     for key in d:
#         sum+=d[key][i]
#     return sum/len(d[key])

# def all_mark(d):
#     i=0
#     while i<3:
#         x=average(d,i)
#         print(x)
#         i+=1
# d={"abi":[10,20,30],"biju":[60,23,45],"ruchi":[50,30,56]}
# all_mark(d)