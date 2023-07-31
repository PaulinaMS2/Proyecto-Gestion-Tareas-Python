from Clases.Proyecto import Proyecto
import colorama

colorama.init()
import datetime


class Tarea:
    def __init__(self, nombre, fecha_inicio):
        self.nombre = nombre
        self.estado = False
        self.fecha_inicio = fecha_inicio

    def crear_tarea(nombre, proyecto):
        fecha_inicio = datetime.date.today()
        fecha_inicio = fecha_inicio.strftime("%d/%m/%Y")
        tarea = Tarea(nombre, fecha_inicio)
        proyecto.tareas.append(tarea)

    def finalizar_tarea(tarea):
        tarea.estado = True
        print("Tarea completada")

    def eliminar_tarea(tarea, proyecto):
        proyecto.tareas.remove(tarea)
        del tarea
        print("La tarea ha sido eliminada exitosamente.")

    def mostrar_tareas(proyecto):
        print(colorama.Fore.LIGHTBLUE_EX + "   Proyecto" + proyecto.nombre + colorama.Style.RESET_ALL)
        for i in proyecto.tareas:
            estado_texto = 'Completada' if i.estado else 'En curso'
            color = colorama.Fore.GREEN if i.estado else colorama.Fore.YELLOW

            print(f"         {i.nombre} -  {color}{estado_texto}{colorama.Style.RESET_ALL}  - Tarea creada {i.fecha_inicio} ")

    def tareas_finalizadas(proyecto):
        print(colorama.Fore.LIGHTCYAN_EX + "         Tareas completadas " + proyecto.nombre + colorama.Style.RESET_ALL)
        for j in proyecto.tareas:
            if j.estado == True:
                estado_texto = 'Completada' if j.estado else 'En curso'
                color = colorama.Fore.GREEN if j.estado else colorama.Fore.YELLOW
                print(f"         {j.nombre} -  {color}{estado_texto}{colorama.Style.RESET_ALL}  - Tarea creada {j.fecha_inicio} ")

    def tareas_enCurso(proyecto):
        print(colorama.Fore.LIGHTCYAN_EX + "        Tareas en curso " + proyecto.nombre + colorama.Style.RESET_ALL)
        for k in proyecto.tareas:
            if k.estado == False:
                estado_texto = 'Completada' if k.estado else 'En curso'
                color = colorama.Fore.GREEN if k.estado else colorama.Fore.YELLOW
                print(
                    f"         {k.nombre} -  {color}{estado_texto}{colorama.Style.RESET_ALL}  - Tarea creada {k.fecha_inicio} ")


