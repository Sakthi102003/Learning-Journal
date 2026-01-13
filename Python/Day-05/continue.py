for i in range(5):
    if i==2 or i==4:
        continue
    print(i)

#While loop with continue
n=0
while n<=10:
    n+=1
    if n%2 != 0:
        continue
    print(n, end=' ')