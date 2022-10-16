# Create function
def reciMjau(ime= 'Cico'):
    print(f'Mjau {ime}')
    
    
reciMjau()    

# Create values
def zbroji(br1, br2):
    zbroj= br1 + br2
    return zbroj

#print(zbroji(3, 4))
br= zbroji(3, 4)
print(br)

#Lambda functions
zbroji= lambda br1, br2: br1 + br2
print(zbroji(10, 12))