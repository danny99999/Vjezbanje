def funkcija2(x,y):
    return {k:v for k,v in zip(x,y) if len(x)== len(y)}

print(funkcija2([1,2,3], [4,3,2] ))
print(funkcija2([1,2], [4,3,2] ))
