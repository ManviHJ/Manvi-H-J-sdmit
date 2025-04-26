#print
#11112
#32222
#33334
#54444
#55556

a1=[0,0,0,0,0]
a2=[0,0,0,0,0]
a3=[0,0,0,0,0]
a4=[0,0,0,0,0]
a5=[0,0,0,0,0]

for i in range(4):
    a1[i]=1 
    a1[i+1]=2
    result="".join(map(str,a1))
print(result)
for i in range(4):
    a2[0]=3 
    a2[i+1]=2
    result="".join(map(str,a2))
print(result)
for i in range(4):
    a3[i]=3
    a3[i+1]=4
    result="".join(map(str,a3))
print(result)
set(a4)
for i in range(4):
    a4[0]=5 
    a4[i+1]=4
    result="".join(map(str,a4))
print(result)
for i in range(4):
    a5[i]=5 
    a5[i+1]=6
    result="".join(map(str,a5))
print(result)

