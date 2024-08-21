"""
La librería debe soportar por lo menos las siguientes operaciones entre números complejos:
    -Suma
    -Producto
    -Resta
    -División
    -Módulo
    -Conjugado
    -Conversión entre representaciones polar y cartesiano, en los dos sentidos.
    -Retornar la fase de un número complejo.
"""
import math

def suma(m,n):
    sumaReales=m[0]+n[0]
    sumaImaginarios=m[1]+n[1]
    return(sumaReales,sumaImaginarios)

def producto(m,n):
    productoa=((m[0]*n[0])-(m[1]*n[1]))
    productob=((m[0]*n[1])+m[1]*n[0])
    return(productoa,productob)

def resta(m,n):
    restaReales=m[0]-n[0]
    restaImaginarios=m[1]-n[1]
    return(restaReales,restaImaginarios)

def division(m,n):
    parteReal=((m[0]*n[0])+(m[1]*n[1]))/(n[0]**2+n[1]**2)
    parteImaginaria=((n[0]*m[1])-(m[0]*n[1]))/(n[0]**2+n[1]**2)
    return(parteReal,parteImaginaria)

def modulo1(m):
    modulo=((m[0]**2)+(m[1]**2))**(1/2)
    return(modulo)

def modulo2(m,n):
    modulo2=((m[0]**2)*(m[1]**2))+((n[0]**2)*(n[1]**2))+((m[0]**2)*(n[1]**2))+((m[1]**2)*(n[0]**2))
    return(modulo2)

def conjugado(m):
    return(m[0],m[1]*(-1))

def polarAcartesiano(m):
    a=m[0]*math.cos(m[1])
    b=m[0]*math.sin(m[1])
    return(a,b)    

def cartesianoApolar(m):
    c=modulo1(m)
    angulo=math.atan(m[1]/m[0])
    return(c,angulo)

def fase(m):
    fase=math.atan(m[1]/m[0])
    return(fase)


def main():
    print("--PRUEBA--")
    print("")
    print("SUMA")
    print("suma #1",suma((-2,1),(1,2)))
    print("suma #2",suma((3,-1),(4,5)))

    print("\nPRODUCTO")
    print("producto #1",producto((-2,1),(1,2)))
    print("producto #2",producto((3,-1),(4,5)))

    print("\nRESTA")
    print("resta #1",resta((-2,1),(1,2)))
    print("resta #2",resta((3,-1),(4,5)))

    print("\nDIVISION")
    print("division #1",division((-2,1),(1,2)))
    print("division #2",division((3,-1),(4,5)))

    print("\nMODULO 1")
    print("modulo #1",modulo1((-2,1)))
    print("modulo #2",modulo1((3,-1)))

    print("\nMODULO 2")
    print("modulo #1",modulo2((-2,1),(1,2)))
    print("modulo #2",modulo2((3,-1),(4,5)))

    print("\nCONJUGADO")
    print("conjugado #1",conjugado((-2,1)))
    print("conjugado #2",conjugado((3,-1)))

    print("\nPOLAR A CARTESIANO")
    print("polarAcartesiano #1",polarAcartesiano((2,math.pi/4)))
    print("polarAcartesiano #2",polarAcartesiano((5,math.pi/3)))

    print("\nCARTESIANO A POLAR")
    print("cartesianoApolar #1",cartesianoApolar((-2,1)))
    print("cartesianoApolar #2",cartesianoApolar((3,-1)))

    print("\nFASE")
    print("fase #1",fase((-2,1)))
    print("fase #2",fase((3,-1)))

main()



    




