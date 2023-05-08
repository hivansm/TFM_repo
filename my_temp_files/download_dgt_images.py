import requests
from bs4 import BeautifulSoup #Hay que instalar
import time

while True:
    try:
        url = 'https://www.camarasdgt.es/madrid/a-1/km-21-000-a-121000/' # URL de la página web de la DGT
        response = requests.get(url) # Hacer una solicitud HTTP GET
        soup = BeautifulSoup(response.content, 'html.parser') # Analizar el HTML con BeautifulSoup

        # Encontrar la URL de la imagen más reciente
        img = soup.find_all('img', {'title': 'Cámara Carretera A-1 P.k.:  Via de Servicio A-121.000'})[0]
        img_url = img['src']

        # Descargar la imagen
        img_data = requests.get(img_url).content
        with open('imagen.jpg', 'wb') as f:
            f.write(img_data)

        print('Imagen descargada correctamente')
    except Exception as e:
        print('Error al descargar la imagen: ' + str(e))

    time.sleep(3) # Esperar 5 segundos antes de descargar la próxima imagen