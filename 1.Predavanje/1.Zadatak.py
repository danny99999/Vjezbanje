
def funkcija1(x):
    #if isinstance(x, list) == False:
    #    print('not')
        
    #assert isinstance(x, list)
    return [y if y%4==0  else round(y**0.5, 2) for y in x]

print(funkcija1([213,14,23,6543,232]))
