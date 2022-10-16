r= []
for x in range(20):
    r.append(x)
    
print(r)
print([x if x%2==0 else -1 for x in range(20)])    