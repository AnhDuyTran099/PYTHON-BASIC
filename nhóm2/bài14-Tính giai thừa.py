import math
def fac(n):
  if n==0:
    return 1
  return n*fac(n-1)
n=int(input())
"""
  hàm
  print(math.factorial(n))
"""
print(fac(n))
