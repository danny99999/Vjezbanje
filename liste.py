# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:01:49 2022

@author: Danny
"""
# A list is a collection which is oredered and changeable. Allows duplicate
# members.

#Stvaranje liste
brojevi = [1, 2, 3, 4, 5, 6]
voće = ['Jabuke', 'Naranče', 'Banane', 'Jagode']

#Korištenje konstruktora
#brojevi2 = list((1, 2, 3, 4, 5, 6))

#Dobivanje vrijednosti iz liste
print(voće[0])
#Dobivanje dužine stringa
print(len(voće))
#Dodavanje na kraju liste
voće.append('Limun')
print(voće)
#Brisanje s liste
voće.remove('Banane')
print(voće)
#Insert i brisanje iz određene pozicije
voće.insert(2, 'Šljiva')
voće.pop(2)
print(voće)
#Okretanje liste
voće.reverse()
#Sortiranje i obrnuto sortiranje liste
voće.sort()
voće.sort(reverse=True)
#Mijenjanje vrijednosti u listi
voće[0]= 'Borovnica'
print(voće)



