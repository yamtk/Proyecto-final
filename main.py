import tkinter as tk
from tkinter import messagebox
import smtplib


# Productos del restaurante italiano
productos = [
    {"nombre": "Pizza Margherita", "precio": 12.00},
    {"nombre": "Lasagna", "precio": 7.00},
    {"nombre": "Spaghetti Carbonara", "precio": 8.00},
    {"nombre": "Tiramisu", "precio": 6.00},
    {"nombre": "Ravioli Ricotta", "precio": 8.00}
]
#Diccionario - facilitar el uso de los datos




# Función para calcular el total
def calcular_total():
    total = 0
    for i, prod in enumerate(productos): #Acceder tanto al indice, como al diccionario facilmente
        cantidad = cantidades[i].get()#devuelve el valor actual almacenado (en este caso, la cantidad ingresada por el usuario para el producto i en la interfaz gráfica).
        total += cantidad * prod["precio"]
    return total




# Función para realizar el pedido
def realizar_pedido():
    domicilio = entrada_domicilio.get()
    correo = entrada_correo.get()
    if not domicilio or not correo:
        messagebox.showwarning("Advertencia", "Por favor, ingrese domicilio y correo.")
        return
    
    # Resumen del pedido
    resumen = "Pedido realizado:\n"
    for i, prod in enumerate(productos):
        cantidad = cantidades[i].get()
        if cantidad > 0:
            resumen += f"{prod['nombre']} x{cantidad} - ${cantidad * prod['precio']:.2f}\n"#:.2f asegura que el número tenga dos decimales, como es común para precios en dólares
    resumen += f"\nTotal: ${calcular_total():.2f}\n"
    resumen += f"Domicilio: {domicilio}\nCorreo: {correo}"
    


    # Mostrar el resumen
    messagebox.showinfo("Pedido Confirmado", resumen)
    


    # Enviar correo de confirmación
    enviar_correo(correo, resumen)




# Función para enviar el correo
def enviar_correo(destinatario, mensaje):
    try:
        # Configuración del servidor SMTP
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()#es un protocolo que se usa para notificar a un servidor de correo electrónico 
        #que el cliente quiere actualizar una conexión insegura a una segura
        servidor.login("italianaventa@gmail.com", "italia1945")  
        
        asunto = "Confirmación de Pedido - Restaurante Italiano"
        cuerpo = f"Subject: {asunto}\n\n{mensaje}"
        
        servidor.sendmail("italianaventa@gmail.com", destinatario, cuerpo)
        servidor.quit()
        messagebox.showinfo("Correo Enviado", "Se ha enviado un correo de confirmación.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Restaurante Italiano - Pedidos a Domicilio")





# Lista de cantidades
cantidades = [tk.IntVar(value=0) for _ in productos]#tk.IntVar es una clase variable en la biblioteca GUI de Python, Tkinter, que se utiliza 
#para almacenar valores enteros para diferentes operaciones de widgets





# Crear la interfaz gráfica
tk.Label(ventana, text="Seleccione sus productos:", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
#tk.Label:Mostrar texto o imahenes en la interfaz gráfica
#columnspan: Especifica la cantidad de columnas que tendrá un widget
#pady: Es el espacio vertical entre el widget y las celdas



for i, producto in enumerate(productos):
    tk.Label(ventana, text=f"{producto['nombre']} - ${producto['precio']:.2f}", font=("Arial", 12)).grid(row=i+1, column=0, sticky="w")
    tk.Spinbox(ventana, from_=0, to=1000, textvariable=cantidades[i], width=5).grid(row=i+1, column=1)

#Row: Cuadricula en la que se colocan las palabras o imagenes
#Sticky: Alineación dentro de la celda
#from_=0: Define el valor mínimo que el usuario puede seleccionar en el Spinbox. En este caso, el mínimo es 0.
#to=10: Establece el valor máximo que el usuario puede seleccionar. Aquí, el valor máximo es 10.
#textvariable=cantidades[i]:almacenar el valor que se selecciona en el Spinbox
#width=5: Define el ancho del Spinbox
#.grid(row=i+1, column=1): Este método coloca el widget en la ventana usando un sistema de rejilla



tk.Label(ventana, text="Domicilio:", font=("Arial", 12)).grid(row=len(productos)+1, column=0, pady=10, sticky="w")
entrada_domicilio = tk.Entry(ventana, width=30)
entrada_domicilio.grid(row=len(productos)+1, column=1)

#+1: Al sumar 1 a len(productos), se desplaza una posición posterior a la última fila donde se colocan los productos
#tk.Entry: Crea un widget de entrada de texto
#width=30:Define el ancho del campo de entrada en términos de caracteres(30 caracteres en este caso)



tk.Label(ventana, text="Correo Electrónico:", font=("Arial", 12)).grid(row=len(productos)+2, column=0, pady=10, sticky="w")
entrada_correo = tk.Entry(ventana, width=30)
entrada_correo.grid(row=len(productos)+2, column=1)

tk.Button(ventana, text="Realizar Pedido", command=realizar_pedido, bg="green", fg="white", font=("Arial", 12)).grid(row=len(productos)+3, column=0, columnspan=2, pady=20)
#columnspan=2: Le indica al widger, cuaántas columnas debe de ocupar. Si esta tiene 2, entonces debe de ocupar 2

# Iniciar la aplicación
ventana.mainloop()
