def dfs(i, f):
  if i == N - 1:
    return sum(list(map(int, f.split("+"))))
    
  return dfs(i+1, f + S[i+1]) + dfs(i+1, f + "+" + S[i+1])



S = input()
N = len(S)
print(dfs(0, S[0]))