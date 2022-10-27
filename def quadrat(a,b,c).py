a = int(input("Insert a)"))
b = int(input("Insert b)"))
c = int(input("Insert c)"))
def quadrat(a,b,c):
    det = ((b**2)-(4*a*c))
    if (det<0):
        print("No existen raíces")
    elif (det==0):
        raiz = (-b/(2*a))
        return (raiz)
    else:
        x1 = (-b+((det)**(0.5)))/(2*a)
        x2 = (-b-((det)**(0.5)))/(2*a) 
        return (x1, x2)


print (quadrat(a, b, c))




