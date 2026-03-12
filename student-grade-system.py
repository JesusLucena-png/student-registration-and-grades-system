# ==============================
# IMPORTACIONES
# ==============================

import os

# ==============================
# BASE DE DATOS
# ==============================
Estudiantes = [
    ["JESUS LUCENA", 123456789,
        {"Materia":"MATEMATICAS","Nota1":9.5,"Nota2":8.0,"Nota3":7.5,"Promedio":(9.5+8.0+7.5)/3},
        {"Materia":"FISICA","Nota1":6.0,"Nota2":7.0,"Nota3":8.0,"Promedio":(6.0+7.0+8.0)/3}
    ],

    ["JOSE JOSE", 123456788,
        {"Materia":"QUIMICA","Nota1":5.0,"Nota2":6.5,"Nota3":7.0,"Promedio":(5.0+6.5+7.0)/3},
        {"Materia":"HISTORIA","Nota1":8.0,"Nota2":7.5,"Nota3":6.5,"Promedio":(8.0+7.5+6.5)/3}
    ],

    ["MARIA GOMEZ", 123456787,
        {"Materia":"BIOLOGIA","Nota1":9.0,"Nota2":8.5,"Nota3":7.5,"Promedio":(9.0+8.5+7.5)/3},
        {"Materia":"LITERATURA","Nota1":6.0,"Nota2":7.0,"Nota3":8.0,"Promedio":(6.0+7.0+8.0)/3}
    ],

    ["CARLOS PEREZ", 123456786,
        {"Materia":"GEOGRAFIA","Nota1":5.0,"Nota2":6.0,"Nota3":7.0,"Promedio":(5.0+6.0+7.0)/3},
        {"Materia":"EDUCACION FISICA","Nota1":9.0,"Nota2":8.5,"Nota3":9.5,"Promedio":(9.0+8.5+9.5)/3}
    ],

    ["ANA TORRES", 123456785,
        {"Materia":"ARTES","Nota1":8.0,"Nota2":9.0,"Nota3":7.5,"Promedio":(8.0+9.0+7.5)/3},
        {"Materia":"MUSICA","Nota1":6.5,"Nota2":7.0,"Nota3":8.0,"Promedio":(6.5+7.0+8.0)/3}
    ]
]


Materias = ["MATEMATICAS","FISICA","QUIMICA","HISTORIA","BIOLOGIA","LITERATURA","GEOGRAFIA","EDUCACION FISICA","ARTES","MUSICA"]

# ==============================
# FUNCIÓN PARA MOSTRAR TÍTULOS
# ==============================
def Titulo(titulo):
    # Centra el título con guiones a los lados
    if len(titulo) % 2 == 0:
        Lado = (58 - len(titulo)) // 2
        print("\n\033[34m" + "-"*Lado + " " + titulo + " " + "-"*Lado + "\033[0m")
    else:
        Lado = ((58 - 1) - len(titulo) + 1) // 2
        print("\n\033[34m" + "-"*Lado + " " + titulo + " -" + "-"*Lado + "\033[0m")

# ==============================
# FUNCIÓN PARA REGISTRAR ESTUDIANTES
# ==============================
def Registro_Estudiante():
    Titulo("Registro De Estudisntes")

    # Entrada del usuario
    try:

        Nombre = input("\n\033[34m >> \033[0mIngresa El Nombre Del Estudiante: ").upper()
        Identificaion = int(input("\n\033[34m >> \033[0mIngresa El Identificador Del Estudiante: "))

        for Estudiante in Estudiantes:

            if Nombre in Estudiante and Identificaion in Estudiante:
                print("\n\033[1;31m" + "-"*60)
                print("Error: Estudiante Ya Existente")
                print("-"*60 + "\033[0m")

                break

            elif Identificaion in Estudiante:
                print("\n\033[1;31m" + "-"*60)
                print("Error: Repeticion De Datos")
                print("-"*60 + "\033[0m")

                break
            
            else:
                Estudiantes.append([Nombre,Identificaion])
 
                print("\n\033[1;32m" + "-"*61)
                print(f"Estudiante {Nombre} Creado Con Exito")
                print("-"*61 + "\033[0m")

                break

    except ValueError:

        print("\n\033[1;31m" + "-"*60)
        print("Error: Valor Ingresado Inadecuado")
        print("-"*60 + "\033[0m")
    
    print("\033[34m" + "-"*60 + "\033[0m")

# ==============================
# FUNCIÓN PARA REGISTRAR MATERIAS Y NOTAS
# ==============================
def Registrar_Materias_Notas():

    ws = True
    while ws:
        Titulo("Registro De Materis y Notas")

        print("""
    1. Crear Materias
    2. Asignación de Materias y Notas

    3.Exit
        """)
        print("\033[34m" + "-"*60 + "\033[0m")

        Opcion = input("\n\033[34m >> \033[0mIngresa La Opcion: ")

        if Opcion == "1":


            Nombre_Materia = input("\n\033[34m >> \033[0mIngresa La Nueva Materia: ").upper()
            
            if Nombre_Materia in Materias:
                print("\n\033[1;31m" + "-"*60)
                print("Error: Repeticion De Datos")
                print("-"*60 + "\033[0m")

            else:
                Materias.append(Nombre_Materia)

                os.system("cls" if os.name == "nt" else "clear")

                print("\n\033[1;32m" + "-"*61)
                print(f"La Materia De {Nombre_Materia} Se Creo Con Exito")
                print("-"*61 + "\033[0m")

        elif Opcion == "2":

            try:

                Identificaion = int(input("\n\033[34m >> \033[0mIngresa El Identificador Del Estudiante: "))

                for Estudiante in Estudiantes:

                    if Identificaion in Estudiante:

                        Nombre_Materia = input("\n\033[34m >> \033[0mIngresa La Nueva Materia: ").upper()
            
                        if Nombre_Materia in Materias:

                            Titulo(f"{Nombre_Materia} - {Estudiante[0]}")
                            
                            Promedio = 0
                            Registro = {
                                "Materia" : Nombre_Materia,
                                }
                            
                            for i in range(3):

                                while True:
                                    try:
                                        Nota = float(input(f"\n\033[34m >> \033[0mIngresa La Nota {i+1} Estudiante: "))

                                        if Nota < 0 or Nota > 10:
                                            print("\n\033[1;31m" + "-"*60)
                                            print("Error: Valor No Esta Entre [0 y 10]")
                                            print("-"*60 + "\033[0m")
                                        
                                        else:
                                            Registro["Nota" + str(i+1)] = Nota
                                            Promedio = Nota + Promedio

                                            break

                                    except ValueError:

                                        print("\n\033[1;31m" + "-"*60)
                                        print("Error: Valor Ingresado Inadecuado")
                                        print("-"*60 + "\033[0m")

                                
                            Registro["Promedio"] = round(Promedio / 3,2)
                            Estudiante.append(Registro)

                        else:

                            print("\n\033[1;31m" + "-"*60)
                            print("Error: Materia No Existente")
                            print("-"*60 + "\033[0m")

                            break

                    else:

                        print("\n\033[1;31m" + "-"*60)
                        print("Error: Estudiante No Existente")
                        print("-"*60 + "\033[0m")

                        break

            except ValueError:

                print("\n\033[1;31m" + "-"*60)
                print("Error: Valor Ingresado Inadecuado")
                print("-"*60 + "\033[0m")

        elif Opcion == "3":
            ws = False
        else:

            print("\n\033[1;31m" + "-"*61)
            print("Error: Opcion Invalida")
            print("-"*61 + "\033[0m")

    print("\033[34m" + "-"*60 + "\033[0m")

# ==============================
# FUNCIÓN PARA VISUALIZAR LA INFORMACION
# ==============================
def Vizualizar_Informacion():
    Titulo("Visualización De Información")

    for Estudiante in Estudiantes:

        Promedio_Total = 0
        Cont = 0

        print("\033[34m" + "-"*60 + "\033[0m")
        print(f"Nombre: {Estudiante[0]} - ID: {Estudiante[1]}")
        print(f"\n{'MATERIA':<20}{'NOTA1':<10}{'NOTA2':<10}{'NOTA3':<10}{'PROMEDIO':<10}")

        if Estudiante[2:]:
            for Notas in Estudiante[2:]:
                print(f"{Notas['Materia']:<25}{Notas['Nota1']:<10}{Notas['Nota2']:<10}{Notas['Nota3']:<10}{Notas['Promedio']:<10}")
                Promedio_Total += Notas['Promedio']
                Cont += 1
                print("\033[34m" + "-"*60 + "\033[0m")
        else:

            print("\033[1;31m" + "-"*61)
            print("Error: No Hay Notas")
            print("-"*61 + "\033[0m")

        try:
            print(f"Promedio Total: {Promedio_Total/Cont}")
        except ZeroDivisionError:
            print(f"Promedio Total: -")
        print("\033[34m" + "-"*60 + "\033[0m")


# ==============================
# FUNCIÓN PARA VISUALIZAR LA INFORMACION DE ESTUDIANTE
# ==============================
def Vizualizar_Informacion_Estudiante():
    Titulo("Visualización Notas De Estudiante")

    try:

        Identificaion = int(input("\n\033[34m >> \033[0mIngresa El Identificador Del Estudiante: "))

        for Estudiante in Estudiantes:

            Promedio_Total = 0
            Cont = 0

            if Identificaion in Estudiante:
                print("\033[34m" + "-"*60 + "\033[0m")
                print(f"Nombre: {Estudiante[0]} - ID: {Estudiante[1]}")
                print(f"\n{'MATERIA':<20}{'NOTA1':<10}{'NOTA2':<10}{'NOTA3':<10}{'PROMEDIO':<10}")
                print("\033[34m" + "-"*60 + "\033[0m")

                if Estudiante[2:]:
                    for Notas in Estudiante[2:]:
                        print(f"{Notas['Materia']:<25}{Notas['Nota1']:<10}{Notas['Nota2']:<10}{Notas['Nota3']:<10}{Notas['Promedio']:<10}")
                        Promedio_Total += Notas['Promedio']
                        Cont += 1
                        print("\033[34m" + "-"*60 + "\033[0m")
                else:

                    print("\033[1;31m" + "-"*61)
                    print("Error: No Hay Notas")
                    print("-"*61 + "\033[0m")

                try:
                    print(f"Promedio Total: {Promedio_Total/Cont}")
                except ZeroDivisionError:
                    print(f"Promedio Total: -")

                print("\033[34m" + "-"*60 + "\033[0m")
                break
            
        if not Identificaion in Estudiante:
            print("\033[1;31m" + "-"*61)
            print("Error: No Hay Estudiantes Con Ese ID")
            print("-"*61 + "\033[0m")
    except ValueError:
        print("\n\033[1;31m" + "-"*60)
        print("Error: Valor Ingresado Inadecuado")
        print("-"*60 + "\033[0m")


def Tabla_De_Honor():
    Titulo("Lista De Honor")

    ranking = []

    for Estudiante in Estudiantes:

        Promedio_Total = 0
        Cont = 0

        if Estudiante[2:]:
            for Notas in Estudiante[2:]:
                Promedio_Total += Notas['Promedio']
                Cont += 1

            Promedio_General = Promedio_Total / Cont
            ranking.append((Estudiante[0], Estudiante[1], Promedio_General))

        else:
            print("\033[1;31m" + "-"*61)
            print("Error: No Hay Notas")
            print("-"*61 + "\033[0m")

    # Ordenar de mayor a menor por promedio
    ranking.sort(key=lambda x: x[2], reverse=True)

    print("\033[34m" + "-"*60 + "\033[0m")

    for estudiante in ranking:
        print(f"Nombre: {estudiante[0]} - ID: {estudiante[1]} - Promedio General: {estudiante[2]:.2f}")
        print("\033[34m" + "-"*60 + "\033[0m")



def List_Opciones():
    Titulo("Menu De Opciones")

    print("""
\033[34m    1.\033[0m Registrar Estudiantes
\033[34m    2.\033[0m Reqistrar Materias Y Notas
\033[34m    3.\033[0m Vizuanlizar Notas De Estudiantes
\033[34m    4.\033[0m Buscar Notas De Estudiante
\033[34m    5.\033[0m Lista De Honor
            
\033[31m    6.\033[0m Salir
    """)

    print("\033[34m" + "-"*60 + "\033[0m\n")

ws = True
while ws:

    List_Opciones()

    Opcion = input("\033[34m >> \033[0mIngresa Un Opcion : ")

    os.system("cls" if os.name == "nt" else "clear")

    if Opcion == "1":
        Registro_Estudiante()

    elif Opcion == "2":
        Registrar_Materias_Notas()

    elif Opcion == "3":
        Vizualizar_Informacion()

    elif Opcion == "4":
        Vizualizar_Informacion_Estudiante()

    elif Opcion == "5":
        Tabla_De_Honor()

    elif Opcion == "6":
        ws = False

    else:

        print("\n\033[1;31m" + "-"*61)
        print("Error: Opcion Invalida")
        print("-"*61 + "\033[0m")