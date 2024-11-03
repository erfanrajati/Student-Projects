g=0
print('A magical square is a table with numbers, that the sum of every line is equal with others.') 
while g%2!=1:
    g=int(input('write an odd number, to set a magical square: '))
v=[]
for q in range(g):
    x=(g*q)+1
    u=g*(q+1)+1
    o=list(range(x,u))
    v.append(o)
for h in range(g):
    a1=v[h]
    for d2 in range(g):
        a1[d2]=0
j=int((g-1)/2)
i=0

for l in range(g*g):
    n=v[i]
    if l+1-n[j]==g and n[j]!=0:
        j+=1
        i+=2
        n=v[i]
    n[j]=l+1
    i-=1
    j-=1
    if j<=-g:
        j=0
    if i<=-g:
        i=0

for row in v:
    for col in row:
        shift = 3 - len(str(col))
        print(col,' '*shift, end='')
    print()


# written by Setayesh Sabbagh 11/03/2024