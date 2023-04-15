#s=input()#標準入力

#Input=input()
fr = list(map(str, input().split()))
s = list(map(str, input().split())) #リストで受け取る場合
#trans = list(map(str, input().split()))
list_t=[list(map(str, input().split())) for l in range(0,int(fr[2]))]

print(" fr : "+str(fr))
print(" s  : "+str(s))
#print(" trans : "+str(trans))
print(" list_t : "+str(list_t))



s_x=int(s[0]);s_y=int(s[1]);print(str(s_x)+" "+str(s_y))


n=int(fr[2]) #回数
#trans_n=int(list_t[n-1][1])-1
#trans_d=str(list_t[n-1][0])
fr_w=int(fr[0]);fr_h=int(fr[1])

for i in range(0,n):
    if str(list_t[i][0]) == 'U':
        s_y=(s_y+int(list_t[i][1]))%fr_h
    if str(list_t[i][0]) == 'D':
        s_y=(s_y-int(list_t[i][1]))%fr_h
    if str(list_t[i][0]) == 'R':
        s_x=(s_x+int(list_t[i][1]))%fr_w
    if str(list_t[i][0]) == 'L':
        s_x=(s_x-int(list_t[i][1]))%fr_w
    print("回数"+str(i+1))
    print(str(s_x)+" "+str(s_y))

print(str(s_x)+" "+str(s_y))