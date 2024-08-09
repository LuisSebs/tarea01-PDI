from PIL import Image

# Filtro de color rojo
def filtro_rojo(imagen: Image):
    """
    Funcion que aplica el filtro de color rojo a una imagen.

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
    Funcion que aplica el filtro de color verde a una imagen.

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
    Funcion que aplica el filtro de color azul a una imagen.

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
    Funcion que aplica el filtro de brillo a una imagen.

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
    Funcion que aplica el filtro de escala de grises a una imagen.

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
    Funcion que aplica el filtro de alto contraste a una imagen.

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
    Funcion que aplica el filtro de bajo contraste a una imagen.

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
    Funcion que aplica el filtro negativo a una imagen.

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
    Funcion que aplica el filtro mica a una imagen.

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
    Funcion que aplica el filtro mosaico a una imagen.

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

class FiltroRojo:
    
    def __init__(self, tkinter_app):
        self.nombre = "Filtro rojo"
        self.filtro = filtro_rojo
        self.tkinter_app = tkinter_app

class FiltroVerde:
    
    def __init__(self, tkinter_app):
        self.nombre = "Filtro verde"
        self.filtro = filtro_verde
        self.tkinter_app = tkinter_app

class FiltroAzul:
    
    def __init__(self, tkinter_app):
        self.nombre = "Filtro azul"
        self.filtro = filtro_azul
        self.tkinter_app = tkinter_app

