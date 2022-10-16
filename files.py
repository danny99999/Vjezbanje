import os

# Open a file
myFile= open('Kodijen.txt', 'w')

# Get some info
print('Ime:', myFile.name)
print('Je zatvoren:', myFile.closed)
print('Opening mode:', myFile.mode)

# Write to file
myFile.write('Cico voli Denisova mala jaja')
myFile.write(' i njegovu kokoš bez glave')
myFile.close()

#Append file

myFile= open('Kodijen.txt', 'a')
myFile.write('. Osim ako je propucana u cs-u')
myFile.close()

# Read
myFile= open('Kodijen.txt', 'r+')
text= myFile.read(90)
print(text)
myFile.close()

#Remove
if os.path.exists('Kodijen.txt'):
    os.remove('Kodijen.txt')
    print('Datoteka je izbrisana')
else:
    print('Datoteka ne postoji booookte')    
