l=[1,1,2,3,4,4,5,1] ##[[2,1],2,3,[3,4],5,1]
i=0
j=1
l1=[]
s=''
k=0
while i<len(l)-1:
    if l[i]==l[i+1]:
        # s+=str(l[i])
        # s+=str(l[j])
        k+=1
        l1.append([k,l[i]])
    else:
        l1.append(l[j])
    j+=1
    i+=1
print(l1)