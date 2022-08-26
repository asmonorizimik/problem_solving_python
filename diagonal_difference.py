list=[[1,2,3],[4,5,6],[9,8,9]]
c=0
d=0
f=(len(list)-1)
d1=0
d2=0
while c<len(list):
    d1=d1+list[c][d]
    d2=d2+list[c][f]
    c+=1
    d+=1
    f-=1
if d1>d2:
    print(d1-d2)
else:
    print(d2-d1)




# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal =1+5+9 . The right to left diagonal =3+5+9 . Their absolute difference is 15-17=2.

# Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Sample Output
# 15