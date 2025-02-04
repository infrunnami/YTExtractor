import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
import sys
import os

ventana = tk.Tk()

# Verificar si estamos ejecutando como un ejecutable
if getattr(sys, 'frozen', False):  # Si está en un ejecutable
    ruta_icono = os.path.join(sys._MEIPASS, 'logardo.ico')
else:
    ruta_icono = 'logardo.ico'

# Configuración de la ventana
ventana.title("YTExtractor")
ventana.configure(bg="#181818")
ventana.resizable(False, False)
ventana.iconbitmap(ruta_icono)

# Establecer el tamaño de la ventana
ancho_ventana = 600
alto_ventana = 500
ventana.geometry(f"{ancho_ventana}x{alto_ventana}")

# Centrar la ventana en la pantalla
ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
x = (ancho // 2) - (ancho_ventana // 2)
y = (alto // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Función para descargar el video
def descargar():
    url = entrada.get()
    entrada.delete(0, tk.END)
    if not url:
        messagebox.showerror(title="Error", message="URL inválida")
        return

    try:
        Label2.config(text="Descargando...")
        opciones = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'outtmpl': filedialog.askdirectory() + '/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        messagebox.showinfo(title="Éxito", message="Se ha descargado exitosamente")
        Label2.config(text="Introduce la URL del video")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Ocurrió un error: {e}")
        Label2.config(text="Introduce la URL del video")

# Label1
Label1 = tk.Label(ventana, text="Descargador de videos de YouTube", bg="#FF0000", fg="white", font=("Roboto", 20, "bold"))
Label1.place(relx=0.5, y=75, anchor="center")

# Contenedor
Contenedor = tk.Frame(ventana, bg="#202020", width=550, height=300)
Contenedor.place(relx=0.5, y=300, anchor="center")

# Label2
Label2 = tk.Label(Contenedor, text="Introduce la URL del video", bg="#202020", fg="white", font=("Roboto", 14))
Label2.place(relx=0.5, y=70, anchor="center")

# Buscador
ancho_buscar = 500
alto_buscar = 30
entrada = tk.Entry(Contenedor, bg="#121212", fg="white", font=("Roboto", 12))
entrada.config(insertbackground='white')
x_buscar = (550 // 2) - (ancho_buscar // 2)
y_buscar = (270 // 2) - (alto_buscar // 2)
entrada.place(x=x_buscar, y=y_buscar, width=ancho_buscar, height=alto_buscar)

# Botón Descargar
ancho_btn1 = 100
alto_btn1 = 50
Boton1 = tk.Button(Contenedor, bg="#FF0000", text="Descargar", command=descargar, fg="white", font=("Roboto", 12, "bold"))
x_btn1 = (550 // 4) - (ancho_btn1 // 2)
y_btn1 = (350 // 2) + (alto_btn1 // 2)
Boton1.place(x=x_btn1, y=y_btn1, width=ancho_btn1, height=alto_btn1)

# Botón Salir
ancho_btn2 = 100
alto_btn2 = 50
Boton2 = tk.Button(Contenedor, bg="#FF0000", text="Salir", command=ventana.quit, fg="white", font=("Roboto", 12, "bold"))
x_btn2 = (3 * 550 // 4) - (ancho_btn2 // 2)
y_btn2 = (350 // 2) + (alto_btn2 // 2)
Boton2.place(x=x_btn2, y=y_btn2, width=ancho_btn2, height=alto_btn2)

# Mantener ventana
ventana.mainloop()
