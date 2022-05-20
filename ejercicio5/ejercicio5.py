numero= int(input("ingrese el numero: "))
contador=0

while numero>0:
    numero=numero//10
    contador=contador+1

print("el numero ingresado tiene %s digitos"% (contador))