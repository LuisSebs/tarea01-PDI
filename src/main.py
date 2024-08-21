import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from core.filtros import *

class App(Tk):

    MAX_SIZE = (400,400)

    FILTROS = {
        'Original': FiltroOriginal,
        'Rojo': FiltroRojo,
        'Verde': FiltroVerde,
        'Azul': FiltroAzul,
        'Brillo': FiltroBrillo,
        'Escala de grises': FiltroEscalaDeGrises,
        'Alto contraste': FiltroAltoContraste,
        'Bajo contraste': FiltroBajoContraste,
        'Negativo': FiltroNegativo,
        'Mica': FiltroMica,
        'Mosaico': FiltroMosaico,
        'Blur': FiltroBlur,
        'Motion Blur': FiltroMotionBlur,
        'Sharpen': FiltroSharpen,
        'Promedio': FiltroPromedio
    }

    def __init__(self):
        super().__init__()
        
        self.title("Tarea01 - Proceso Digital de Imagenes")
        self.iconbitmap("./assets/morsa.ico")
        self.geometry('820x680')
    
        # Panel para mostrar la imagen
        self.panel_imagen = Label(self)
        self.panel_imagen.pack()

        # Boton para cargar la imagen
        self.boton_abrir_imagen = Button(self, text="Cargar Imagen", command=self.abril_imagen)
        self.boton_abrir_imagen.pack(pady=24)

        # Imagenes (referencias)
        self.imagen_original = None
        self.imagen_modificada = None

        # Filtro activo
        self.filtro_activo = None

        # Lista desplegable de filtros
        self.lista_desplegable = None

    def abril_imagen(self):

        ruta_imagen = filedialog.askopenfilename(
            initialdir="./",
            title="Selecciona una imagen",
            filetypes=(
                (
                    'Imagenes jpg',
                    '*.jpg'
                ),
                (
                    'Imagenes jpeg',
                    '*.jpeg'                    
                ),
                (
                    'Imagenes png',
                    '*.png'
                )
            )            
        )

        if ruta_imagen:
            # Cargamos la imagen
            self.imagen_original = PIL.Image.open(ruta_imagen)

            # Redimensionamos la imagen original
            self.imagen_original.thumbnail(self.MAX_SIZE)

            # Copia de la imagen original
            self.imagen_modificada = self.imagen_original.copy()

            # Mostramos las imagenes
            self.mostrar_imagenes()  

            # Reseteamos los valores de la lista desplegable
            if self.lista_desplegable:
                self.lista_desplegable.destroy()

            # Eliminamos todos los widgets del filtro activo
            if self.filtro_activo:
                self.filtro_activo.remover_widgets()   

            # Una mostramos los filtros disponibles
            self.crear_widget_lista() 
            
    def mostrar_imagenes(self):
        # Crear una imagen combinada con la original y la modificada
        imagen_combinada = Image.new('RGB', (self.imagen_original.width + self.imagen_modificada.width, max(self.imagen_original.height, self.imagen_modificada.height)))
        imagen_combinada.paste(self.imagen_original, (0, 0))
        imagen_combinada.paste(self.imagen_modificada, (self.imagen_original.width, 0))
            
        # Imagen que tkinter pueda entender
        tkinter_imagen = PIL.ImageTk.PhotoImage(imagen_combinada)
        
        # Actualizamos el panel de la imagen
        self.panel_imagen.config(image=tkinter_imagen)
        self.panel_imagen.image = tkinter_imagen

    def crear_widget_lista(self):
        # Opciones de la lista desplegable
        opciones = list(self.FILTROS.keys())
        # Creamos la lista
        self.lista_desplegable = ttk.Combobox(self, state='readonly', values=opciones)
        # Primera opcion por defecto
        self.lista_desplegable.current(0)
        self.lista_desplegable.pack(pady=20)

        # Evento de cambio
        self.lista_desplegable.bind("<<ComboboxSelected>>", self.on_select)

    def on_select(self, event):
        # Removemos los widgets que haya agregado el filtro activo
        if self.filtro_activo:
            self.filtro_activo.remover_widgets()
        # Obtenemos el filtro seleccionado
        filtro_seleccionado = self.FILTROS.get(self.lista_desplegable.get())
        # Instanciamos el filtro
        self.filtro_activo = filtro_seleccionado(self)
        # Llamamos a su funcion aplicar_filtro
        self.filtro_activo.aplicar_filtro(self.imagen_original)
            
app = App()
app.mainloop()