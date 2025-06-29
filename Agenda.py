import os
os.system('cls')

contactos=[]

def agregar_contacto():
    nom=input("Ingrese nombre del contacto para agregar: ").lower().strip()
    for guardado in contactos:
        if guardado["nombre"]==nom:
            print("El contacto ya existe.")
            return
    else:
        while True:
            try:
                telefono=int(input(f"Ingrese numero de telefono de {nom}: "))
                guardado={
                    "nombre" : nom,
                    "telefono" : telefono
                }
                contactos.append(guardado)
                print("Contacto guardado con exito!!")
                break
            except ValueError:
                print("Ingrese bien los valores.")

def buscar_contacto():
    busc=input("Ingrese nombre del contacto que busca: ").lower().strip()
    encotrado=False
    for guardado in contactos:
        if guardado["nombre"]==busc:
            print(f"Contacto encontrado: {guardado["nombre"]} {guardado["telefono"]}")
            encotrado=True
    if encotrado==False:
        print("El contacto no existe.")
        return

def modificar_contacto():
    edit=input("Ingrese nombre del contacto para moficar: ").lower().strip()
    encontrado=False
    for guardado in contactos:
        if guardado["nombre"]==edit:
            encontrado=True
            modi=int(input(f"Ingrese nuevo numero de {edit}: "))
            guardado["telefono"]=modi
            print("Numero editado con exito!")
    if encontrado==False:
        print("Ese contacto no existe.")

def eliminar_contacto():
    eli=input("Ingrese nombre del contacto ha eliminar: ").lower().strip()
    encontrado=False
    for guardado in contactos:
        if guardado["nombre"]==eli:
            encontrado=True
            contactos.remove(guardado)
            print("Contacto eliminado con exito!")
    if encontrado==False:
        print("El contacto no exite.")
    
def mostrar_contactos():
    if not contactos:
        print("No tienes contactos que mostrar.")
    else:
        for guardado in contactos:
            print(guardado)

def menu():
    while True:
        try:
            print("****Agenda de contactos****")
            print("esto es una prueba")
            num=int(input("\n1.Agregar contacto\n2.Buscar contacto\n3.Modificar contacto\n4.Eliminar contacto\n5.Mostar contactos\n6.Salir\nSeleccione: "))
            if num==6:
                print("¡Hasta luego!")
                break
            elif num==1:
                agregar_contacto()
            elif num==2:
                buscar_contacto()
            elif num==3:
                modificar_contacto()
            elif num==4:
                eliminar_contacto()
            elif num==5:
                mostrar_contactos()
            else:
                print("Numero invalido.")
        except ValueError:
            print("Numero invalido.")    
menu()