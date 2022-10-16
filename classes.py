# Create class
class Korisnik:
    #Constructor
    def __init__(self, ime, godine, mail):
        self.ime= ime
        self.godine= godine
        self.mail= mail
        
    def greating(self):    
        return f'Moje ime je {self.ime} i ja imam {self.godine} godina'
    
    def rođendan(self):
        self.godine += 1
        
# Extend class
class Musterija(Korisnik):
    def __init__(self, ime, godine, mail):
        self.ime= ime
        self.godine= godine
        self.mail= mail
        self.stanje= 0
    def postavi_stanje(self, stanje):
        self.stanje= stanje
        
    def greating(self):    
        return f'Moje ime je {self.ime} i ja imam {self.godine} godina. Stanje na računu je {self.stanje}.'            
        
# Init user object
danny= Korisnik('Danijel Dupor', 23, 'sitnajaja@gmail.com')

# Init customer
đenis= Musterija('Denis Kodijen', 23, 'denis@malajaja.com')

đenis.postavi_stanje(4500)

danny.rođendan()

print(danny.greating())
print(đenis.greating())
