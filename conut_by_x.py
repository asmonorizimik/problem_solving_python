def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    i=1
    l=[]
    while i<=n:
        l.append(x*i)
        i+=1
    return l
x=int(input())
n=int(input())
print(count_by(x,n))


# input:
# 2
# 5
# output:
# [2, 4, 6, 8, 10]