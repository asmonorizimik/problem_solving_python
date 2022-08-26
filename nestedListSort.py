list=[[1,4,5],[1,3,4],[2,6]]
a=[]
for n in list:
    for num in n:
        a.append(num)
j=0
while j<len(a):
    i = 0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
        i = i+1
    j+=1
print(a,"the sorted numbers")