M = int(input())
N = int(input())
MN = []
index = []

for i in range(M):
    MN.append(list(map(int, input().split())))

# 코드 자체ㅔㅇ서만 
# 목표 MN[M-1][N-1]
# 시작점 M[0]N[0]

#def FindIndex(Value):
 #   index.clear()
 #   for i in range(M):
 #      for j in range(N):
 #          if MN[i][j] == Value:
