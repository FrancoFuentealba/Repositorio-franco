import os
os.system('cls')
stock=10
reservados=[]

def codigo(nom):
    global stock
    clave=input("Digite la clave secreta para reservar: ")
    if clave != "EstoyEnListaDeReserva":
        print("Clave incorrecta")
        return
    elif stock==0:
        print("No hay stock suficiente.")
        return 
    else:
        usuarios={
            "nombre": nom,
            "zapatillas": 1,
            "tipo": "estandar"
        }
        reservados.append(usuarios)
        stock-=1
        print(f"Reserva realizada exitosamente a {nom}")
        return 


def reserva_zapatillas():
    while True:
        nom=input("Nombre del comprador: ")
        if any(usuario["nombre"]==nom for usuario in reservados):
            print(f"{nom} ya tiene reserva.")
            return
        else:  
            resultado=codigo(nom)
            if resultado:
                return
            else:
                return


def buscar_zapatillas():
    global stock
    nom=input("Ingrese nombre del comprador a buscar: ")
    for comprador in reservados:
        if comprador["nombre"]==nom and comprador["tipo"]=="VIP":
            print("Usted ya es VIP.")
            return
        else:
            print(f"Reserva encontrada: {nom} - {comprador["zapatillas"]} par(es) - {comprador["tipo"]}")
            while True:
                op=input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
                if op not in ["s","n"]:
                    print("Ingrese una opcion en pantalla.")
                elif op== "s":
                    print(f"Resevera actualizada a VIP. Ahora {nom} tiene 2 pares")
                    stock-=1
                    comprador["tipo"]="VIP"
                    comprador["zapatillas"]+=1
                    return
                else:
                    print("Manteniendo reserva actual.")
                    return
    print("El comprador no existe.")
    return


def cancelar_reserva():
    nom=input("Ingrese nombre del comprador: ")
    for comprador in reservados:
        if comprador["nombre"]==nom:
            print(f"Reserva de {nom} cancelada correctamente.")
            reservados.remove(comprador)
            return
    print("El comprador no existe.")


def menu():
    while True:
        try:
            print("****MENU****")
            print("1.Reservar zapatillas")
            print("2.Buscar zapatillas reservadas")
            print("3.Cancelar reserva de zapatillas")
            print("4.Salir")
            num=int(input("Seleccione: "))
            if num==4:
                print("Adios....")
                break
            elif num==1:
                if stock!=0:
                    reserva_zapatillas()
                else:
                    print("Ya no queda mas stock.")
            elif num==2:
                if stock!=0:
                    buscar_zapatillas()
                else:
                    print("Ya no queda mas stock.")
            elif num==3:
                    cancelar_reserva()
            else:
                print("Seleccione un numero del menu.")
        except ValueError:
            print("Elija correctamente.")
menu()