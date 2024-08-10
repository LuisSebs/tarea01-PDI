from PIL import Image
from tkinter import Scale, HORIZONTAL, VERTICAL, Label, Entry, Frame

# Filtro Original
def filtro_original(imagen: Image):
    """
    Funcion regresa una copia de la imagen.

    Parameters :
    ----------

    imagen:
        Imagen en formato Pillow

    Returns :
    ---------

    Pillow imagen, copia de la imagen original.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Imagen por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            nueva_imagen.putpixel((x,y), pixel)

    # Regresamos la nueva imagen
    return nueva_imagen

# Filtro de color rojo
def filtro_rojo(imagen: Image):
    """
    Funcion que aplica el filtro de color rojo a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    -----------

    imagen: 
        Imagen en formato Pillow.

    Returns :
    ---------

    Pillow imagen con el filtro de color rojo aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Imagen por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Conservamos el canal rojo
            nuevo_pixel = (pixel[0], 0, 0)
            nueva_imagen.putpixel((x,y), nuevo_pixel)

    # Regresamos la nueva imagen
    return nueva_imagen

# Filtro de color verde
def filtro_verde(imagen: Image):
    """
    Funcion que aplica el filtro de color verde a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    -----------

    imagen: 
        Imagen en formato Pillow.

    Returns :
    ---------

    Pillow imagen con el filtro de color verde aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Conservamos el canal verde
            nuevo_pixel = (0, pixel[1], 0)
            nueva_imagen.putpixel((x,y), nuevo_pixel)

    # Regresamos la nueva imagen
    return nueva_imagen

# Filtro de color azul
def filtro_azul(imagen: Image):
    """
    Funcion que aplica el filtro de color azul a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    -----------

    imagen: 
        Imagen en formato Pillow.

    Returns :
    ---------

    Pillow imagen con el filtro de color azul aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Conservamos el canal azul
            nuevo_pixel = (0, 0, pixel[2])
            nueva_imagen.putpixel((x,y), nuevo_pixel)

    # Regresamos la nueva imagen
    return nueva_imagen

# Filtro Brillo
def filtro_brillo(imagen: Image, factor: float):
    """
    Funcion que aplica el filtro de brillo a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    ------------

    imagen: 
        Imagen en formato Pillow.

    fact: 
        factor de brillo.

    Returns :
    ---------

    Pillow imagen con el filtro de brillo aplicado.
    """

    # Caso en el que el factor sea negativo, poder obscurecer la foto
    factor = (factor + 1)/2

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Desestructuracion del pixel original. Ejemplo: r, g, b = (255,0,255)
            r, g, b = pixel 
            # No pueden ser valores flotantes, ademas el valor debe estar entre 0 y 255, por eso se usa max y min
            nuevo_pixel = (
                max(0, min(255, int(r * factor))),
                max(0, min(255, int(g * factor))),
                max(0, min(255, int(b * factor)))
            )
            nueva_imagen.putpixel((x,y), nuevo_pixel)

    # Regresamos la nueva imagen
    return nueva_imagen

# Filtro Escala de Grises
def filtro_escala_de_grises(imagen: Image):
    """
    Funcion que aplica el filtro de escala de grises a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    ------------

    imagen: 
        Imagen en formato Pillow.

    Returns :
    ---------

    Pillow imagen con el filtro de escala de grises aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Desestructuracion del pixel original
            r, g, b = pixel
            promedio = int((r + g + b) / 3)
            nuevo_pixel = (
                promedio,
                promedio,
                promedio
            )
            nueva_imagen.putpixel((x,y), nuevo_pixel)
    
    return nueva_imagen

# Filtro Alto Contraste
def filtro_alto_contraste(imagen: Image):
    """
    Funcion que aplica el filtro de alto contraste a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    ------------

    imagen: 
        Imagen en formato Pillow.

    Returns :
    ---------

    Pillow imagen con el filtro de alto contraste aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Desestructuracion del pixel original
            r, g, b = pixel
            promedio = int((r + g + b) / 3)
            pixel_blanco = (0, 0, 0)
            pixel_negro = (255, 255, 255)
            nuevo_pixel = pixel_blanco if (promedio > 127) else pixel_negro
            nueva_imagen.putpixel((x,y), nuevo_pixel)
    
    return nueva_imagen

# Filtro Bajo Contraste
def filtro_bajo_contraste(imagen: Image):
    """
    Funcion que aplica el filtro de bajo contraste a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    ------------

    imagen: 
        Imagen en formato Pillow.

    Returns :
    ---------

    Pillow imagen con el filtro de bajo contraste aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Desestructuracion del pixel original
            r, g, b = pixel
            promedio = int((r + g + b) / 3)
            pixel_blanco = (0, 0, 0)
            pixel_negro = (255, 255, 255)
            nuevo_pixel = pixel_blanco if (promedio < 127) else pixel_negro
            nueva_imagen.putpixel((x,y), nuevo_pixel)
    
    return nueva_imagen

# Filtro Negativo
def filtro_negativo(imagen: Image):
    """
    Funcion que aplica el filtro negativo a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    ------------

    imagen: 
        Imagen en formato Pillow.

    Returns :
    ---------

    Pillow imagen con el filtro negativo aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Desestructuracion del pixel original
            r, g, b = pixel
            nuevo_pixel = (
                255 - r, # Negativo del rojo
                255 - g, # Negativo del verde
                255 - b  # Negativo del azul
            )
            nueva_imagen.putpixel((x,y), nuevo_pixel)
    
    return nueva_imagen

# Filtro Mica
def filtro_mica(imagen: Image, color: tuple):
    """
    Funcion que aplica el filtro mica a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    ------------

    imagen: 
        Imagen en formato Pillow.

    color:
        color de la mica

    Returns :
    ---------

    Pillow imagen con el filtro mica aplicado.
    """

    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            # Desestructuracion del pixel original
            r, g, b = pixel
            # Desestructuracion del color de la mica
            r_, g_, b_ = color
            # Mezclar el color del píxel con el color de la mica
            nuevo_pixel = (
                min(255, int((r + r_) / 2)),
                min(255, int((g + g_) / 2)),
                min(255, int((b + b_) / 2))
            )
            nueva_imagen.putpixel((x,y), nuevo_pixel)
            
    return nueva_imagen

# Filtro Mosaico
def filtro_mosaico(imagen: Image, size: tuple):
    """
    Funcion que aplica el filtro mosaico a una imagen y regresa una copia de la imagen con el filtro aplicado.

    Parameters :
    ------------

    imagen: 
        Imagen en formato Pillow.

    size:
        tamaño del mosaico

    Returns :
    ---------

    Pillow imagen con el filtro mosaico aplicado.
    """
 
    # Tamaño de la imagen
    size_x, size_y = imagen.size

    # Nueva imagen
    nueva_imagen = Image.new(mode="RGB", size=(size_x, size_y))

    # Tamaño del mosaico
    x_, y_ = size

    for x in range(0 ,imagen.width ,x_):        
        for y in range(0 ,imagen.height, y_):
            suma_r = 0
            suma_g = 0
            suma_b = 0 
            # Ubicaciones de los pixeles del mosaico
            ubicaciones = []
            for i in range(x_):
                for j in range(y_):
                    if ((x + i) < imagen.width) and ((y + j) < imagen.height):
                        ubicacion = ((x + i),(y + j))            
                        pixel = imagen.getpixel(ubicacion)
                        # Desestructuracion del pixel
                        r, g, b = pixel
                        suma_r += r
                        suma_g += g
                        suma_b += b
                        ubicaciones.append(ubicacion)

            # Promedios de los canales de color
            promedio_r = int(suma_r / len(ubicaciones))
            promedio_g = int(suma_g / len(ubicaciones))
            promedio_b = int(suma_b / len(ubicaciones))
            
            # Aplicamos el color promedio a todos los pixeles del bloque de la nueva imagen
            for ubicacion in ubicaciones:                
                nuevo_pixel = (promedio_r, promedio_g, promedio_b)
                nueva_imagen.putpixel(ubicacion, nuevo_pixel)

    return nueva_imagen

class FiltroOriginal:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro original"
        self.filtro = filtro_original
        self.tkinter_app = tkinter_app

    def aplicar_filtro(self, imagen): 
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        pass

class FiltroRojo:
    
    def __init__(self, tkinter_app):
        self.nombre = "Filtro rojo"
        self.filtro = filtro_rojo
        self.tkinter_app = tkinter_app
    
    def aplicar_filtro(self, imagen): 
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        pass

class FiltroVerde:
    
    def __init__(self, tkinter_app):
        self.nombre = "Filtro verde"
        self.filtro = filtro_verde
        self.tkinter_app = tkinter_app

    def aplicar_filtro(self, imagen): 
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        pass

class FiltroAzul:
    
    def __init__(self, tkinter_app):
        self.nombre = "Filtro azul"
        self.filtro = filtro_azul
        self.tkinter_app = tkinter_app

    def aplicar_filtro(self, imagen): 
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        pass

class FiltroBrillo:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro brillo"
        self.filtro = filtro_brillo
        self.tkinter_app = tkinter_app

    def aplicar_filtro(self, imagen):
        self.imagen = imagen
        self.crear_widget_deslizador()
    
    def crear_widget_deslizador(self):
        """
            Crea un deslizador para poder controlar el brillo
        """
        # Deslizador
        self.tkinter_app.deslizador = Scale(
            self.tkinter_app,
            from_=-1,
            to=10,
            resolution=0.1,
            orient=HORIZONTAL,
            command=self.on_change
        )
        # Valor por defecto
        self.tkinter_app.deslizador.set(1)
        # Lo agregamos a la interfaz
        self.tkinter_app.deslizador.pack(pady=12)

    def on_change(self, factor):
        """
            Funcion de evento de modificacion para aplicar el filtro
        """
        self.tkinter_app.imagen_modificada = self.filtro(self.imagen, float(factor))
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        """
            Elimina los widgets creados
        """
        self.tkinter_app.deslizador.destroy()
    
class FiltroEscalaDeGrises:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro escala de grises"
        self.filtro = filtro_escala_de_grises
        self.tkinter_app = tkinter_app

    def aplicar_filtro(self, imagen):
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        pass

class FiltroAltoContraste:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro Alto Contraste"
        self.filtro = filtro_alto_contraste
        self.tkinter_app = tkinter_app
    
    def aplicar_filtro(self, imagen):
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()
    
    def remover_widgets(self):
        pass

class FiltroBajoContraste:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro Bajo Contraste"
        self.filtro = filtro_bajo_contraste
        self.tkinter_app = tkinter_app
    
    def aplicar_filtro(self, imagen):
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()
    
    def remover_widgets(self):
        pass

class FiltroNegativo:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro Negativo"
        self.filtro = filtro_negativo
        self.tkinter_app = tkinter_app
    
    def aplicar_filtro(self, imagen):
        self.tkinter_app.imagen_modificada = self.filtro(imagen)
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        pass

class FiltroMica:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro Mica"
        self.filtro = filtro_mica
        self.tkinter_app = tkinter_app
    
    def aplicar_filtro(self, imagen):
        self.imagen = imagen
        self.crear_widget_color()
        
    def crear_widget_color(self):
        """
            Crea un controlador para poder elegir el color de la mica
        """
        # Contenedor de controladores RGB
        contenedor_rgb = Frame(self.tkinter_app)

        # Validacion que verifica que la entrada sea correcta
        # Verificamos que la longitud sea menor/igual a 3
        # Verificamos que el contenido sea un numero y menor a 255
        # Permitimos que el campo este vacio (en la funcion del evento se maneja este caso)
        validacion = (lambda caracter_ingresado, contenido: (len(contenido) <= 3 and contenido.isdigit() and int(contenido) <= 255) or len(contenido) == 0)
                
        # Registramos la funcion de validacion de numeros
        registro_validacion = self.tkinter_app.register(validacion)
        
        # Etiquetas
        # Rojo
        label_r = Label(contenedor_rgb, text="R")
        label_r.grid(row=0, column=0, padx=5, pady=5)
        # Verde
        label_g = Label(contenedor_rgb, text="G")
        label_g.grid(row=0, column=2, padx=5, pady=5)
        # Azul
        label_b = Label(contenedor_rgb, text="B")
        label_b.grid(row=0, column=4, padx=5, pady=5)

        # Inputs
        # %S caracter ingresado
        # %P contenido de la entrada + el caracter ingresado
        # Rojo
        entrada_r = Entry(contenedor_rgb, validate="key", validatecommand=(registro_validacion, "%S", "%P"))
        entrada_r.insert(0, "255") # Valor por defecto
        entrada_r.grid(row=0, column=1, padx=5, pady=5)
        # Verde
        entrada_g = Entry(contenedor_rgb, validate="key", validatecommand=(registro_validacion, "%S", "%P"))
        entrada_g.insert(0, "0") # Valor por defecto
        entrada_g.grid(row=0, column=3, padx=5, pady=5)
        # Azul
        entrada_b = Entry(contenedor_rgb, validate="key", validatecommand=(registro_validacion, "%S", "%P"))
        entrada_b.insert(0, "255") # Valor por defecto
        entrada_b.grid(row=0, column=5, padx=5, pady=5)

        # Evento de modificacion
        entrada_r.bind("<KeyRelease>", self.on_change)
        entrada_g.bind("<KeyRelease>", self.on_change)
        entrada_b.bind("<KeyRelease>", self.on_change)

        # Referencias a los input
        self.entrada_r = entrada_r
        self.entrada_g = entrada_g
        self.entrada_b = entrada_b

        self.tkinter_app.contenedor_rgb = contenedor_rgb
        self.tkinter_app.contenedor_rgb.pack()

        # Obtenemos el color por defecto
        r = int(entrada_r.get())
        g = int(entrada_g.get())
        b = int(entrada_b.get())

        # Aplicamos el filtro por defecto
        self.tkinter_app.imagen_modificada = self.filtro(self.imagen, (r,g,b))
        self.tkinter_app.mostrar_imagenes()

    def on_change(self, event):
        """
            Funcion de evento de modificacion que aplica el filtro
        """
        # Obtenemos los valores de las entradas
        r = self.entrada_r.get()
        g = self.entrada_g.get()
        b = self.entrada_b.get()

        # Caso en el que la entrada sea vacia
        if r.isdigit() and g.isdigit() and b.isdigit():
            color_mica = (int(r), int(g), int(b))
            self.tkinter_app.imagen_modificada = self.filtro(self.imagen, color_mica)
            self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        """
            Elimina los widgets creados
        """
        self.tkinter_app.contenedor_rgb.destroy()

class FiltroMosaico:

    def __init__(self, tkinter_app):
        self.nombre = "Filtro Mosaico"
        self.filtro = filtro_mosaico
        self.tkinter_app = tkinter_app

    def aplicar_filtro(self, imagen):
        self.imagen = imagen
        self.crear_widget_deslizador()

    def crear_widget_deslizador(self):
        """
            Crea un deslizador para poder controlar el tamaño del mosaico
        """

        self.tkinter_app.deslizador = Scale(
            self.tkinter_app,
            from_=1,
            to=15,
            resolution=1,
            orient=HORIZONTAL,
            command=self.on_change
        )
        # Valor por defecto
        self.tkinter_app.deslizador.set(2)
        # Lo agregamos a la interfaz
        self.tkinter_app.deslizador.pack(pady=12)

    def on_change(self, factor):
        """
            Funcion de evento de modificacion para aplicar el filtro
        """
        # Tamaño del mosaico
        size_mosaico = (int(factor), int(factor))
        self.tkinter_app.imagen_modificada = self.filtro(self.imagen, size_mosaico)
        self.tkinter_app.mostrar_imagenes()

    def remover_widgets(self):
        """
            Elimina los widgets creados
        """
        self.tkinter_app.deslizador.destroy()
