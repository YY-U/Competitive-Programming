#標準入力
import sys

N, M, K = list(map(int, input().split()))  #店の数、自分以外のユーザー数、基準数
s = list(map(int, input().split()))    #自分のリスト

u = []

for i in range(M):

    t = list(map(int, input().split()))  #自分以外のリスト

    count = 0
    for j in range(N):
        if s[j] == t[j] and s[j] == 3:
            count += 1

    # 基準数より大きいユーザーに対して
    if count >= K:
        for j in range(N):
            if s[j] == 0 and t[j] == 3:
                u.append(j+1)

u=set(u)
u=sorted(u)

if len(u) == 0:
    print('no')
else:
    u=[str(a) for a in u]
    u=" ".join(u)
    print(u)

sys.exit()

N,M,K = list(map(int, input().split()))
#s = list(map(str, input().split())) #リストで受け取る場合
#trans = list(map(str, input().split()))

#list_s=list(map(int, input().split()))
#my=[]
#my.append(list(map(int, input().split())))
my=list(map(int, input().split()))
#print(" my : "+str(my))
#your=[]
#print(" your : "+str(your))
#for i in range(1,M+1):your.append(list(map(int, input().split())))
#for i in range(M):yours=[i for i in list(map(int, input().split()))]
yours=[list(map(int, input().split())) for _ in range(M)]
#print(" yours : "+str(yours))

#sys.exit(0)

sub=[]
#print(sub)

p=[]

for m in range(M):
    #for i in range(N):# 差分sub[0,3,0,1]を作成
    #     sub.append(abs(my[i]-yours[m][i]))
    #print(sub)
    #if sub.count(0)==K
    if yours[m].count(3)>=K and my.count(3)==K:
        for j in range(N):
            if my[j]==0 and yours[m][j]==3:p.append(j)
    #         print("p "+str(p))
    #sub=[]
#print(p)
p=set(p)
p=sorted(p)

if len(p)==0:
    print("no")
else:
     p=[str(a+1) for a in p]
     p=' '.join(p)
     print(p)


sys.exit()



for m in range(0,M):
    for i in range(N):
         diff=(abs(my[0][i]-your[m][i]))
         if diff==0 and my[0][i]==3:
             sub[i]=0
         #else :sub.append('F')

#print(sub)

pri=[]
for i in range(len(sub)):
    if my[0][i] ==0 :
         if sub[i] == -1 and sub.count(0)==K:
             #print(str(i+1)+" ")
             pri.append(i+1)

pri=sorted(pri)
if len(pri)!=0:
     pri=[str(a) for a in pri]
     pri=' '.join(pri)
     print(pri)
else:print("no")

