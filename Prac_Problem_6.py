''' The first line contains n and x separated by a space.
The next x lines contains the space separated marks obtained by students in a particular subject. '''

n,x = input().split()
m = []

for i in range(int(x)):
    x = map(float,input().split())
    m.append(x)
    
for i in zip(*m):
    print(sum(i)/len(i))