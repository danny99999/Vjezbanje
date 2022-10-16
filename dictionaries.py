# A dictionary is a collection which is unordered, changeable and indexed.
# No duplicate members

# Create dict
osoba= {
    'Ime': 'Cico',
    'Prezime': 'Peder',
    'godina': 22
}

# S konstruktorom
#osoba2= dict(Ime= 'Denis', prezime= 'Penis')
#print(osoba2, type(osoba2))
# Dobivanje vrijednosti
print(osoba['Ime'])
print(osoba.get('Prezime'))

# Add key/value
osoba['broj']= '0064564065'

# Get dict keys
print(osoba.keys())

# Get dict items
print(osoba.items())

# Copy dict
osoba2= osoba.copy()
osoba2['Grad']= 'Pula'

# Remove item
del(osoba['godina'])
osoba.pop('broj')

# Clear
osoba.clear()

# Get length
#print(len(osoba2))

# List of dict

osobe= [
    {'ime': 'Martino', 'godina': 27},
    {'ime': 'Joško', 'godina': 19}
    ]
print(osobe[0] ['ime'])