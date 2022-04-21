from PyPDF4 import PdfFileReader
from googletrans import Translator

translator = Translator()

# // Ruta de origen y destino e idioma //
ask = input("Introduzca la ruta del PDF >")
origen = open(ask,'rb')
destino = open("traduccion.txt","w")
idioma = "es"


reader = PdfFileReader(origen)
num_pages = reader.numPages

# // Por cada página del pdf --> Extraer el texto --> Traducirlo //
# // Problemas a la hora de traducir páginas de mas de 5000 caractéres //

for i in range(num_pages):
    page = reader.getPage(i)
    text = page.extractText()

    if len(text) > 5000 or len(text) == 0:
        print("ERROR Página demasiado larga o vacía")

    else:
        traduccion = translator.translate(str(text), dest=idioma)
        print(traduccion.text)
        destino.write(traduccion.text)
    
destino.close()
