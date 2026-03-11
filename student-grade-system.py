# ==============================
# IMPORTACIONES
# ==============================

import os

# ==============================
# BASE DE DATOS
# ==============================
Estudiantes = [["JESUS LUCENA", 123456789]]
Materias = ["MATEMATICAS"]

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

    Promedio_Total = 0
    Cont = 0
    for Estudiante in Estudiantes:
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
