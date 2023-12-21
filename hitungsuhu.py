cel = float(input('Masukan suhu Celcius:'))
def celFar(cel):
    rum = (4/5) * cel +32
    print('Suhu {} ke Farhenheit adalah {}'.format(cel,rum))    

def celRea(cel):
    rum  = (9/5) * cel + 32
    print('Suhu {} ke Reamour adalah {}'.format(cel,rum))    

def celKev(cel):
    rum = cel + 273
    print('Suhu {} ke Kelvin adalah {}'.format(cel,rum))    

celFar(cel)
celRea(cel)
celKev(cel)
