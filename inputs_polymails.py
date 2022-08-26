# 1 4
# x**3 + x**2 + x + 1

# Input Format

# The first line contains the space separated values of x and k.
# The second line contains the polynomia P .

# Output Format
# Print True if P(x)=k . Otherwise, print False.

# Sample Input
# 1 4
# x**3 + x**2 + x + 1

# Sample Output
# True

# Explanation
# P(1)=1**3+1**2+1+1


x,k=map(int,input().split())
p=input()
a=eval(p)
if a==k:
    print(True)
else:
    print(False)
