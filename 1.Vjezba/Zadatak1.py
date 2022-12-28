import numpy as np

prva_varijabla= 1
print(prva_varijabla)
druga_varijabla= 2
print(druga_varijabla)

lista= list()

lista= []
print(lista)

lista.append(4)

lista= np.arange(20)

print([x for x in range(20)])

r=[]
for x in range (20):
    r.append(x)

print(r)    

print([x for x in range(20) if x%2==0])
print([x if x%2==0 else -1 for x in range(20)])

dictionary= dict()
print(dictionary)
d= {"kluc":"vrijednost"}

d["jedan"]= 1
d[(1,2,3)]= "dva"
print(d)

t=((1,2,3),23,"jedan")
print(t)

s= {1,23,5,4,1}
print(s)

lista1= [x for x in range(19)]
d2= {k:v if v%3==0 else 0 for k,v in enumerate(lista1)}

print(d2)

def fun1(x):
    return x*2, x/4
print(fun1(44))
x, y = fun1(55)
print(x)    
print(y) 

for k,v in d2.items():
    print(k)
    print(v) 

x= [(k,v) for k,v in d2.items()]




