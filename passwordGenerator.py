import random
import secrets
import string


lista = []

def generarContraseña():
    while True:
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
            break
    return password

def main():
    archivo = open("passwords.txt", "w")
    while(len(lista)<10):
        lista.append(generarContraseña())

    for e in lista:
        archivo.write(e+'\n')
    archivo.close
    return lista

if __name__ == "__main__": main()