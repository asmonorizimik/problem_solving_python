if __name__ == '__main__':
    n=int(input("enter no:"))
    s=[]
    y=[]
    i=0
    while i<n:
        x=[]
        name = input("name")
        score = float(input("score"))
        x.append(name)
        x.append(score)
        y.append(x)
        s.append(score)
        i+=1
    s.sort()
    b=s[1]
    for i,j in y:
        if j==b:
            print(i)


# if __name__ == '__main__':
#     y=[]
#     s=[]
#     for _ in range(int(input("no"))):
#         x=[]
#         name = input("name")
#         score = float(input("score"))
#         x.append(name)
#         x.append(score)
#         y.append(x)
#         s.append(score)
#     b=sorted(list(set(s)))
#     a=s[1]
#     for i,j in sorted(y):
#         if j==a:
#             print(i)


# list=["harry","berry","ane","raju"]
# list.sort()
# print(list)