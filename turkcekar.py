
# girilen parolada turkce karakter oldugunda hata veren program
turkce_karakterler = 'şğüöçİı'

parola = input('parola: ')

for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola turkce karakterler iceremez!')
    else:
        pass
print('valid password')