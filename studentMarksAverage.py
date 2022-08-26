a,b=map(int,input().split())
i=1
m={}
while i<=b:
    marks=list(map(str,input().split()))
    m[i]=marks
    i+=1
def average(m,i):
    sum=0
    for key in m:
        sum+=float(m[key][i])
    return sum/len(m)

def all_mark(m):
    i=0
    while i<a:
        x=average(m,i)
        print(x)
        i+=1
all_mark(m)




# Sample Input
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5

# Sample Output
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5        

# Marks obtained by student 1: 89,90,91
# Average marks of student 1:270/3 =90.0


