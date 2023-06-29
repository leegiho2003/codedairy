croatia = input()
croatia1 = list(croatia.split('='))
result = []
i = 0
j = 0
for i in range(len(croatia1)-1):
    a = croatia1[i]
    croatia2 = list(a.split('-'))
    result.append(croatia2)
    i += 1
for j in range(len(croatia2)-1):
    a = croatia2[i]
    croatia3 = list(a.split('j'))
    result.append(croatia3)
    j += 1
    
