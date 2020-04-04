import secrets
import string

#La función generarContraseña construye una contraseña con las librería 'secrets' y strings. La primera para generar acceder a todos los caracteres que la componen.
#Con la librería 'secrets', el programa selecciona los caracteres de forma aleatoria y criptográficamente segura. 

lista = []

def generarContraseña():
    while True:
        alfabeto = string.ascii_letters + string.digits
        contraseña = ''.join(secrets.choice(alfabeto) for i in range(10))
        if (any(c.islower() for c in contraseña)
            and any(c.isupper() for c in contraseña)
            and sum(c.isdigit() for c in contraseña) >= 3):
            break
    return contraseña

#En la función main, se generan 10 contraseñas las cuales se añaden a 'lista'.
#Se crea un archivo 'passwords.txt' en el cual se escriben las contraseñas guardadas en 'lista'.

def main():
    archivo = open("passwords.txt", "w")
    while(len(lista)<10):
        lista.append(generarContraseña())
    for e in lista:
        archivo.write(e+'\n')
    archivo.close
    return lista

if __name__ == "__main__": 
    main()