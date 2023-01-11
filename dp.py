import numpy as np
import random as rd 
# rd.seed(1)
def random_seq():
    s1=''
    chars = ['a','c','g','t']
    l = 16
    d={'a':0,'c':0,'g':0,'t':0}
    while len(s1) < l:
        ch = rd.choice(chars)
        if ch=='a' and d[ch]<4:
            s1+=ch
            d[ch]+=1
        elif ch=='c' and d[ch]<4:
            s1+=ch
            d[ch]+=1
        elif ch=='g' and d[ch] < 4:
            s1+=ch 
            d[ch]+=1
        elif ch == 't' and d[ch] < 4:
            s1+=ch
            d[ch]+=1
    return s1






a = random_seq() #rows
b = random_seq() #columns

cols = len(b)
rows = len(a)

arr = np.zeros((rows+1, cols+1), dtype=int)

Parent = [[(0,0)]*(cols+1) for i in range(rows+1)]
score = 2
penalty = -1


for i in range(1, rows+1):

    for j in range(1, cols+1):

        if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1]+score
            Parent[i][j] = (i-1, j-1)

        else:
            m = max(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])

            if arr[i-1][j-1] > arr[i-1][j] and arr[i-1][j-1] > arr[i][j-1]:
                Parent[i][j] = (i-1, j-1)
                
            elif arr[i-1][j] > arr[i-1][j-1] and arr[i-1][j] > arr[i][j-1]:
                Parent[i][j] = (i-1, j)
                
            elif arr[i][j-1] > arr[i-1][j] and arr[i][j-1] > arr[i-1][j-1]:
                Parent[i][j] = (i, j-1)

            arr[i][j] = m + penalty

maxx = arr[rows].max()


# print('max_val',np.amax(arr)
# print(np.where(arr==arr.max())[0])
z, x = np.where(arr == maxx)
z = z[0]
x = x[0]

print(z,x)
print(arr)

ans = []
p=[]
while(True):
    if z == 0 and x == 0:
        break

    ans.append(arr[z][x])
    p.append((z,x))
    idx = Parent[z][x]
    print(idx)
    z = idx[0]
    x = idx[1]

print('\n', ans)

s1=''
s2=''
for i in range(len(p)):
    t=p[i]
    t1=t[0]-1
    t2=t[1]-1
    # print(t1,t2)
    if a[t1]==b[t2]:
        s1+=a[t1]
        s2+=a[t1]
    else:
        prev=p[i+1]
        # print("prev : ",prev)
        if t1<prev[0] and t2==prev[1]:
            s1+='_'
            s2+=b[t2]
        elif t1==prev[0] and t2<prev[1]:
            s2+='_'
            s1+=a[t1]
    # print(s1,s2)


s1=s1[::-1]
s2=s2[::-1]
print('\n')
print(s1)   
print(s2)