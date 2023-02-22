list = []
a = int(input())

for i in range(0,a):
  addi = int(input())
  list.append(addi) 

mex = max(list)
men = min(list)

print(men)
print(mex)