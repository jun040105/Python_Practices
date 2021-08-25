M = int(input())
N = int(input())
MN = []
index = []
#index.clear()

for i in range(M):
    MN.append(list(map(int, input().split())))

print(MN)

def FindIndex(Value):
    for i in range(M):
        for j in range(N):
            if MN[i][j] == Value:
                MN[i][j] = -1
                coor = (i+1) * (j+1)
                if coor == 1:
                    print("yes")
                    return("yes")
                else: FindIndex(coor)
            elif MN[i][j] == -1:
                print("no")
                return("no")
                

FindIndex(M*N)



# 코드 자체에서만 
# 목표 MN[M-1][N-1]
# 시작점 MN[0][0]