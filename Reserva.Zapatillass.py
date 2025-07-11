import os
os.system('cls')
stock=10
reservados=[]

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