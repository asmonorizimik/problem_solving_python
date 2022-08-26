l=[[10,11,1,3],[12,13,2,3],[14,10,3,3],[10,23,2,3]]
i=0
l2=[]
while i<len(l):
    s=0
    j=0
    le=len(l[i])
    while j<len(l):
        s+=l[j-le][i-le]
        j+=1
    i+=1
    l2.append(s)
print(l2[:len(l[0])])


## [46, 57, 8, 12]
