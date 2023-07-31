from Clases.Tarea import Tarea
from Clases.Usuario import Usuario
from Clases.Proyecto import Proyecto
import colorama
colorama.init()

usuarios = []
def main():
    opcion = "0"
    while opcion != "3":
        print("""
                **************************************************
                *                                                *
                *     BIENVENIDO/A AL PROGRAMA DE  GESTIÓN DE    *
                *                  TAREAS                       *
                *                                                *
                *     Aquí podrás organizar tus tareas con fechas  *
                *       
                *                                                 *
                **************************************************
                
                Seleccione una opcion:
                    1. Crear usuario
                    2. Iniciar sesion
                    3. Salir
            """)
        opcion = input("opcion: ")
        if opcion == "1":
            nombre = input("Nombre de Usuario: ")
            clave = input("Contraseña: ")
            usuario=Usuario.crear_usuario(nombre, clave)
            usuarios.append(usuario)
            print("usuario creado exitosamente")

        elif opcion == "2":
            nombreU = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña:")

            for usuario in usuarios:
                if nombreU == usuario.nombre and contraseña == usuario.clave:
                        if usuario.proyectos == []:
                            Proyecto.crear_proyecto(input("Crea tu primer proyecto: "), usuario)
                        else:
                            Proyecto.mostrar_Proyectos(usuario)
                            proyecto = input(""
                                             "Ingrese el nombre del proyecto al que quiere ingresar:"
                                             "")
                            for p in usuario.proyectos:
                                if p.nombre == proyecto:
                                    option = "0"
                                    while option !="9" :

                                        print("""
                1. Agregar tarea            2. Ver tareas en curso
                3. Ver tareas completadas   4. Completar proyecto
                5. Agregar proyecto         6.Entrar a una tarea
                7.Eliminar proyecto         8.atras
                9.Salir
                                                           """)
                                        option = input("Ingrese una opción: ")
                                        if option == "1":
                                            Tarea.crear_tarea(input("Nombre de la tarea:"),p)
                                            print("Tarea creada exitosamente")

                                        elif option == "2":
                                            Tarea.tareas_enCurso(p)

                                        elif option == "3":
                                            Tarea.tareas_finalizadas(p)

                                        elif option == "4":
                                            Proyecto.finalizar_proyecto(p)

                                        elif option == "5":
                                            nombre = input(""
                                                           "Ingresa el nombre del nuevo proyecto: "
                                                           "")
                                            Proyecto.crear_proyecto(nombre, usuario)
                                            print("proyecto creado correctamente")

                                        elif option == "6":
                                            tarea = input(""
                                                          "Ingrese el nombre de la tarea a la que quiere ingresar: "
                                                          " ")
                                            for t in p.tareas:
                                                if tarea == t.nombre:
                                                    op = "0"
                                                    while op !="3":
                                                        print(
                                                            colorama.Fore.LIGHTRED_EX + "      " + t.nombre + colorama.Style.RESET_ALL)
                                                        print(""" 
                                                            1. Eliminar tarea 
                                                            2. Marcar como completada
                                                            3. Atrás
                                                        """)
                                                        op=input(""
                                                                 "Opción:"
                                                                 " ")
                                                        if op == "1":
                                                            Tarea.eliminar_tarea(t,p)

                                                        elif op =="2":
                                                            Tarea.finalizar_tarea(t)

                                                        elif opcion != "3":
                                                            print(
                                                                "Opción inválida. Por favor, seleccione una opción válida.")

                                        elif option == "7":
                                            Proyecto.eliminar_proyecto(p, usuario)

                                else:
                                   print("El proyecto al que quieres ingresar no existe")
                else:
                    print("El usuario o contraseña son incorrectos")
        elif opcion != "3":
            print("Opción inválida. Por favor, seleccione una opción válida.")


main()

