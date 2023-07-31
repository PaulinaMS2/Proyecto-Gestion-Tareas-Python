from Clases.Usuario import Usuario
import colorama

colorama.init()

class Proyecto:

    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False
        self.tareas = []

    def finalizar_proyecto(proyecto):
        for i in proyecto.tareas:
            if i.estado != True:
                print("Hay tareas sin completar")
            else:
                proyecto.estado = True
                print("Felicitaciones proyecto completado!!!")

    def crear_proyecto(nombre, usuario):
        proyecto = Proyecto(nombre)
        usuario.proyectos.append(proyecto)

    def eliminar_proyecto(proyecto,usuario):
        usuario.proyectos.remove(proyecto)
        del proyecto
        print("El proyecto ha sido eliminado exitosamente.")

    def mostrar_Proyectos(usuario):
        print(colorama.Fore.MAGENTA + "          Tus proyectos" + colorama.Style.RESET_ALL)
        for i in usuario.proyectos:
            estado_texto = 'Finalizado' if i.estado else 'En curso'
            color = colorama.Fore.GREEN if i.estado else colorama.Fore.YELLOW

            print(f"          {i.nombre} - {color}{estado_texto}{colorama.Style.RESET_ALL}")







