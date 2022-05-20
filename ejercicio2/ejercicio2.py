a=int(input("dame el valor de a: "))
b=int(input("dame el valor de b: "))

if a<b:
    a=a+1
    cant_num=0
    while a<b:
        a=a+1
        cant_num=cant_num+1
    print("la cantidad de nummeros que hay es de= ",cant_num)
else:
    print("a debe ser menor que b pendejo")

  