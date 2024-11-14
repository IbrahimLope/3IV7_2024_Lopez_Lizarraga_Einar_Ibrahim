import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk  
import os

# Archivo donde se guardaran los datos
ARCHIVO = "personajeshp.txt"

# Lista de personajes
personajes = []

#Cargar los datos desde el archivo
def cargar_datos():
    global personajes
    personajes = []  
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 9:  # 9 partes por personaje
                    nombre = partes[0]
                    casa = partes[1]
                    animago = partes[2]
                    especie = partes[3]
                    rol = partes[4]
                    personalidad = partes[5]
                    varita = partes[6]
                    patronus = partes[7]
                    familia = partes[8]
                    #Personaje
                    personaje = {
                        "nombre": nombre,
                        "casa": casa,
                        "animago": animago,
                        "especie": especie,
                        "rol": rol,
                        "personalidad": personalidad,
                        "varita": varita,
                        "patronus": patronus,
                        "familia": familia
                    }
                    personajes.append(personaje)

#Guardar los datos en el archivo
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for personaje in personajes:
            f.write(f"{personaje['nombre']},{personaje['casa']},{personaje['animago']},{personaje['especie']},{personaje['rol']},{personaje['personalidad']},{personaje['varita']},{personaje['patronus']},{personaje['familia']}\n")

def registrar_personaje():
    # Crear la ventana de registro
    global ventana_registro
    ventana_registro = tk.Tk()
    ventana_registro.title("Registrar Personaje")
    ventana_registro.geometry("400x600")  # Tamaño de la ventana
    ventana_registro.config(bg="#FAF6E3")  

    # Etiquetas y cajas de texto para cada campo
    tk.Label(ventana_registro, text="Nombre:", bg="#FAF6E3").pack(pady=5)
    global entry_nombre
    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.pack(pady=5)

    tk.Label(ventana_registro, text="Casa:", bg="#FAF6E3").pack(pady=5)
    global entry_casa
    entry_casa = tk.Entry(ventana_registro)
    entry_casa.pack(pady=5)

    tk.Label(ventana_registro, text="Animago: ", bg="#FAF6E3").pack(pady=5)
    global entry_animago
    entry_animago = tk.Entry(ventana_registro)
    entry_animago.pack(pady=5)

    tk.Label(ventana_registro, text="Especie:", bg="#FAF6E3").pack(pady=5)
    global entry_especie
    entry_especie = tk.Entry(ventana_registro)
    entry_especie.pack(pady=5)

    tk.Label(ventana_registro, text="Rol:", bg="#FAF6E3").pack(pady=5)
    global entry_rol
    entry_rol = tk.Entry(ventana_registro)
    entry_rol.pack(pady=5)

    tk.Label(ventana_registro, text="Personalidad:", bg="#FAF6E3").pack(pady=5)
    global entry_personalidad
    entry_personalidad = tk.Entry(ventana_registro)
    entry_personalidad.pack(pady=5)

    tk.Label(ventana_registro, text="Varita:", bg="#FAF6E3").pack(pady=5)
    global entry_varita
    entry_varita = tk.Entry(ventana_registro)
    entry_varita.pack(pady=5)

    tk.Label(ventana_registro, text="Patronus:", bg="#FAF6E3").pack(pady=5)
    global entry_patronus
    entry_patronus = tk.Entry(ventana_registro)
    entry_patronus.pack(pady=5)

    tk.Label(ventana_registro, text="Familia:", bg="#FAF6E3").pack(pady=5)
    global entry_familia
    entry_familia = tk.Entry(ventana_registro)
    entry_familia.pack(pady=5)

    # Botón para registrar el personaje
    tk.Button(ventana_registro, text="Registrar Personaje", command=obtener_datos).pack(pady=20)

    # Ejecutar la ventana
    ventana_registro.mainloop()


#funcion de referencia
 # Función para obtener los datos y cerrar la ventana
def obtener_datos():
    # Obtener los valores de los campos de texto
    nombre = entry_nombre.get()
    casa = entry_casa.get()
    animago = entry_animago.get()
    especie = entry_especie.get()
    rol = entry_rol.get()
    personalidad = entry_personalidad.get()
    varita = entry_varita.get()
    patronus = entry_patronus.get()
    familia = entry_familia.get()

    # Verificar si el personaje ya existe
    if any(p['nombre'].lower() == nombre.lower() for p in personajes):
        messagebox.showinfo("Error", "El personaje ya está registrado.")
        return

    # Definir al personaje
    personaje = {
        "nombre": nombre,
        "casa": casa,
        "animago": animago,
        "especie": especie,
        "rol": rol,
        "personalidad": personalidad,
        "varita": varita,
        "patronus": patronus,
        "familia": familia
        }

    # Agregar el personaje a la lista
    personajes.append(personaje)
    guardar_datos()

    messagebox.showinfo("Éxito", "Personaje registrado exitosamente")
    ventana_registro.quit()  # Cerrar la ventana


#Consultar personajes en la tabla
def consultar_personajes():
    # Crear una nueva ventana para mostrar los personajes
    ventana_consulta = tk.Toplevel()
    ventana_consulta.title("Consultar Personajes")
    ventana_consulta.geometry("950x400")
    ventana_consulta.config(bg="#FAF6E3")  

    #Tabla de personajes
    columns = ("Nombre", "Casa", "Animago", "Especie", "Rol", "Personalidad", "Varita", "Patronus", "Familia")
    
    treeview = ttk.Treeview(ventana_consulta, columns=columns, show="headings", height=15)
    treeview.pack(fill="both", expand=True, padx=10, pady=10)

    #Columnas
    for col in columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=100, anchor="center")

    #Registros de personajes
    if not personajes:
        messagebox.showinfo("Información", "No hay personajes registrados.")
        ventana_consulta.destroy()
        return

    #Datos en la tabla
    for personaje in personajes:
        treeview.insert("", "end", values=(
            personaje["nombre"], 
            personaje["casa"], 
            personaje["animago"], 
            personaje["especie"], 
            personaje["rol"], 
            personaje["personalidad"], 
            personaje["varita"], 
            personaje["patronus"], 
            personaje["familia"]
        ))

    ventana_consulta.mainloop()

def editar_personaje():
    # Crear ventana principal
    ventana_editar = tk.Tk()
    ventana_editar.title("Editar Personaje")
    ventana_editar.geometry("400x670")
    ventana_editar.config(bg="#FAF6E3") 

    def buscar_personaje():
        nombre = nombre_entry.get()
        for personaje in personajes:
            if personaje['nombre'].lower() == nombre.lower():
                cargar_datos(personaje)
                return
        messagebox.showinfo("Error", "No se encontró el personaje.")

    def cargar_datos(personaje):
        # Cargar los datos actuales
        casa_entry.delete(0, tk.END)
        casa_entry.insert(0, personaje['casa'])
        animago_entry.delete(0, tk.END)
        animago_entry.insert(0, personaje['animago'])
        especie_entry.delete(0, tk.END)
        especie_entry.insert(0, personaje['especie'])
        rol_entry.delete(0, tk.END)
        rol_entry.insert(0, personaje['rol'])
        personalidad_entry.delete(0, tk.END)
        personalidad_entry.insert(0, personaje['personalidad'])
        varita_entry.delete(0, tk.END)
        varita_entry.insert(0, personaje['varita'])
        patronus_entry.delete(0, tk.END)
        patronus_entry.insert(0, personaje['patronus'])
        familia_entry.delete(0, tk.END)
        familia_entry.insert(0, personaje['familia'])

    def guardar_ediciones():
        nombre = nombre_entry.get()
        for personaje in personajes:
            if personaje['nombre'].lower() == nombre.lower():
                personaje['casa'] = casa_entry.get() or personaje['casa']
                personaje['animago'] = animago_entry.get() or personaje['animago']
                personaje['especie'] = especie_entry.get() or personaje['especie']
                personaje['rol'] = rol_entry.get() or personaje['rol']
                personaje['personalidad'] = personalidad_entry.get() or personaje['personalidad']
                personaje['varita'] = varita_entry.get() or personaje['varita']
                personaje['patronus'] = patronus_entry.get() or personaje['patronus']
                personaje['familia'] = familia_entry.get() or personaje['familia']
                
                guardar_datos()
                messagebox.showinfo("Éxito", "Personaje editado correctamente")
                ventana_editar.destroy() 
                return
        messagebox.showinfo("Error", "No se encontró el personaje.")

    nombre_label = tk.Label(ventana_editar, text="Nombre del Personaje", bg="#FAF6E3")
    nombre_label.pack(pady=5)
    nombre_entry = tk.Entry(ventana_editar)
    nombre_entry.pack(pady=5)

    buscar_btn = tk.Button(ventana_editar, text="Buscar", command=buscar_personaje)
    buscar_btn.pack(pady=5)

    casa_label = tk.Label(ventana_editar, text="Casa", bg="#FAF6E3")
    casa_label.pack(pady=5)
    casa_entry = tk.Entry(ventana_editar)
    casa_entry.pack(pady=5)

    animago_label = tk.Label(ventana_editar, text="Animago", bg="#FAF6E3")
    animago_label.pack(pady=5)
    animago_entry = tk.Entry(ventana_editar)
    animago_entry.pack(pady=5)

    especie_label = tk.Label(ventana_editar, text="Especie", bg="#FAF6E3")
    especie_label.pack(pady=5)
    especie_entry = tk.Entry(ventana_editar)
    especie_entry.pack(pady=5)

    rol_label = tk.Label(ventana_editar, text="Rol", bg="#FAF6E3")
    rol_label.pack(pady=5)
    rol_entry = tk.Entry(ventana_editar)
    rol_entry.pack(pady=5)

    personalidad_label = tk.Label(ventana_editar, text="Personalidad", bg="#FAF6E3")
    personalidad_label.pack(pady=5)
    personalidad_entry = tk.Entry(ventana_editar)
    personalidad_entry.pack(pady=5)

    varita_label = tk.Label(ventana_editar, text="Varita", bg="#FAF6E3")
    varita_label.pack(pady=5)
    varita_entry = tk.Entry(ventana_editar)
    varita_entry.pack(pady=5)

    patronus_label = tk.Label(ventana_editar, text="Patronus", bg="#FAF6E3")
    patronus_label.pack(pady=5)
    patronus_entry = tk.Entry(ventana_editar)
    patronus_entry.pack(pady=5)

    familia_label = tk.Label(ventana_editar, text="Familia", bg="#FAF6E3")
    familia_label.pack(pady=5)
    familia_entry = tk.Entry(ventana_editar)
    familia_entry.pack(pady=5)

    # Botón para guardar las ediciones
    guardar_btn = tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_ediciones)
    guardar_btn.pack(pady=20)

def eliminar_personaje():
    # Crear ventana principal
    ventana_eliminar = tk.Tk()
    ventana_eliminar.title("Eliminar Personaje")
    ventana_eliminar.geometry("300x200")
    ventana_eliminar.config(bg="#FAF6E3")  

    # Función para buscar el personaje y eliminarlo
    def buscar_y_eliminar():
        nombre = nombre_entry.get()
        for personaje in personajes:
            if personaje['nombre'].lower() == nombre.lower():
                personajes.remove(personaje)  # Eliminar el personaje
                guardar_datos()  # Guardar los cambios
                messagebox.showinfo("Éxito", f"Personaje {nombre} eliminado correctamente.")
                ventana_eliminar.destroy()  # Cerrar la ventana después de eliminar
                return
        messagebox.showinfo("Error", "No se encontró el personaje.")

    nombre_label = tk.Label(ventana_eliminar, text="Nombre del personaje: ", bg="#FAF6E3")
    nombre_label.pack(pady=20)
    
    nombre_entry = tk.Entry(ventana_eliminar)
    nombre_entry.pack(pady=5)

    eliminar_btn = tk.Button(ventana_eliminar, text="Eliminar Personaje", command=buscar_y_eliminar)
    eliminar_btn.pack(pady=20)

    ventana_eliminar.mainloop()

#Menú en ventana
def menu():
    #Ventana principal
    ventana = tk.Tk()
    ventana.title("Harry Potter")
    ventana.geometry("500x500")
    ventana.config(bg="#FAF6E3")  
    img = tk.PhotoImage(file = '06\ImgHarry.png')
    img_lb = tk.Label(ventana, image = img)
    img_lb.place(x = 100, y = 100)
    img_lb.configure(bg = '#FAF6E3')
    
    
    # Cargar los datos desde el archivo
    cargar_datos()

    #Titulo ventana
    bienvenida = tk.Label(ventana, text="Gestión de personajes | Harry Potter", font=("Arial", 16, "bold"), bg="#FAF6E3", fg="#B59F78")
    bienvenida.pack(pady=20)

    #Funciones en el menú
    def on_registrar():
        registrar_personaje()

    def on_consultar():
        consultar_personajes()

    def on_editar():
        editar_personaje()

    def on_eliminar():
        eliminar_personaje()

    def on_salir():
        ventana.quit()

    #Botones del menú
    tk.Button(ventana, text="Registrar", command=on_registrar, width=40, height=2, bg="#B59F78", fg="white").pack(pady=10)
    tk.Button(ventana, text="Consultar", command=on_consultar, width=40, height=2, bg="#B59F78", fg="white").pack(pady=10)
    tk.Button(ventana, text="Buscar y Editar", command=on_editar, width=40, height=2, bg="#B59F78", fg="white").pack(pady=10)
    tk.Button(ventana, text="Eliminar Personaje", command=on_eliminar, width=40, height=2, bg="#B59F78", fg="white").pack(pady=10)
    tk.Button(ventana, text="Salir", command=on_salir, width=20, height=2, bg="#EE4E4E", fg="white").pack(pady=10)

    
    ventana.mainloop()

# Ejecutar el menú
if __name__ == "__main__":
    menu()




    #FUENTES:
    # https://www.youtube.com/watch?v=y69rqjEfwYI&list=PLqlQ2-9ypflQQEepQJvGQ6RJ8llnzk6Kj&index=3&pp=iAQB
    # https://www.youtube.com/watch?v=jqRHhWjKDD8&list=PLqlQ2-9ypflQQEepQJvGQ6RJ8llnzk6Kj&index=5&pp=iAQB
    # https://www.youtube.com/watch?v=MpkTYMzhV0A