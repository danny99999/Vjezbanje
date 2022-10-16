# A tuple is a collection which is ordered and unchangeable. Allows
# duplicate members

#Create tuple




auti= ('Audi', 'BMW', 'Mercedes', 'Mazda', 'Hyundai', 'Toyota')
# S konstruktorom
#auti2= tuple(('Audi', 'BMW', 'Mercedes', 'Mazda', 'Hyundai', 'Toyota'))


# Kod jedne vrijednosti treba ostaviti zarez na kraju
auti3= ('Mercedes',)
#print(auti3, type(auti3))

# Dobivanje vrijednosti
#print(auti[5])

# Ne može se promijeniti vrijednost
# auti[0]= 'Lexus'

# Delete tuple
#del auti3
#print(auti3)

# Dobivanje dužine 
#print(len(auti))
# A set is a collection which is unordered and unindexed.
# No duplicate members

# Stvaranje seta
rucni_satovi= {'Seiko', 'Casio', 'Rolex', 'Longines', 'Omega', 'Citizen'}

# Provjeravanje što je u setu
#print('cicio' in rucni_satovi)

# Dodavanje u set
rucni_satovi.add('Victorinox')

# Dodavanje duplikata
rucni_satovi.add('Victorinox')
print(rucni_satovi)


# Brisanje iz seta
#rucni_satovi.remove('Victorinox')


# Brisanje cijelog seta
#rucni_satovi.clear()


# Delete
#del rucni_satovi


