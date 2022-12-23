from sys import exit

def brain(strn):
    outp = strn[0]
    for i in range(1, len(strn)):
        if strn[i-1] == ' ':
            outp += strn[i]
        
        outp = outp.upper()
    return f"Resultado : {outp}"
def about():
    print("""
    Selecciona La Opcion 1 Ingresa La Palabra Ejemplo

    'Astartes & Miembros'

    Resultado : A&M""")
option = input("""
        Creador De Acronimos

        1) Crear Acronimos
        2) Ayuda
        3) Salir

        Selecciona Una Opcion : """)

if option == '1':
    var = input("Palabra A Tratar : ")
    print(brain(var))
elif option == '2':
    about()
elif option == '3':
    exit()
