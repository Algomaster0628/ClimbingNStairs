memo = {}
def possibleSol(n): # Returns ways to climb n stairs using 1,2,3 steps using DP.
  if n in memo:
    return memo[n]
  if n == 0:
    memo[n] = 0
    return memo[n]
  elif n == 1:
    memo[n] = 1
    return memo[n]
  elif n == 2:
    memo[n] = 2
    return memo[n]
  else:
    x = possibleSol(n - 1) + possibleSol(n - 2) + possibleSol(n - 3)
  memo[n] = x
  return memo[n]
x = possibleSol(4)
print(x)
