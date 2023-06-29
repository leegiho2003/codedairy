croatia = ['c=','c-','dz=','d-','d-','lj','nj','s=','z=']
input = input()
for i in croatia:
    input = input.replace(i, '/')
print(len(input))
