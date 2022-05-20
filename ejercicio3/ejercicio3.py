a=int(input("dame el valor de a: "))
b=int(input("dame el valor de b: "))

if a<b:
    a=a+1
    cant_num=0
    while a<b:
        r=a%2
        if r==0:
            cant_num=cant_num+1
        a=a+1
    print("la cantidad de numeros pares es de= ", cant_num)

else:
    print("a tiene que ser menor que b no sea menso")
        