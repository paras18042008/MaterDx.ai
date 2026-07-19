

l=[1,2,3]
n=len(l)
nu=0
x=0
while x<n:
  
    for j in reversed(l):
        nu=nu + j*(10**x)
        x=x+1
        
nn=nu+1
fl=[]
for digit in str(nn):
    fl.append(int(digit))

