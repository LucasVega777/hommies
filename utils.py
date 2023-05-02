from ascii_magic import AsciiArt

def get_image_link(link):
    # Extraer el ID de la imagen del enlace
    file_id = link.split("/d/")[1].split("/view")[0]
    
    # Construir el enlace de descarga directa de la imagen
    direct_link = "http://drive.google.com/uc?export=view&id=" + file_id
    
    # Devolver el enlace de descarga directa de la imagen
    return direct_link

def get_html(url):
    codigo_html = AsciiArt.from_url(
        get_image_link(url),
    )
    return codigo_html.to_html(columns=200)
