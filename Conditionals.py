


x= 10
y= 20

# Simple if
#/if x > y:
#    print(f'{x} je veći od {y}')
#else:
#    print(f'{y} je veći od {x}')

# elif
#if x > y:
#    print(f'{x} je veći od {y}')
#elif x == y:
#    print(f'{x} je jednak {y}')
    
#else:
#    print(f'{y} je veći od {x}')

# Nested if
#if x > 2:
#    if x <= 10:
#        print(f'{x} je veći od 2 i manji ili jednak 10')
        
# Logički operatori
if x > 2 and x <= 10:
    print(f'{x} je veći od 2 i manji ili jednak 10')
             
             
if x > 2 or x <= 10:
             print(f'{x} je veći od 2 i manji ili jednak 10')
             
# not
#if not(x == y):
#    print(f'{x} nije jednak {y}')
#else:
#    print(f'{x} je jednak {y}')  

# Membership operators (not, not in)
brojevi= [1,2,3,4,5]

if x in brojevi:
    print(x in brojevi) 
    
if x not in brojevi:
    print(x not in brojevi)       