import cv2
from PIL import Image
nombres_fotos=[]
coordenadas=[]

def guardarDatos():
    archivo = open("mediciones.txt","r")
    lineas = archivo.readlines()
    for linea in lineas:
        coordenada_imagen=[]
        nombre=linea.strip()[2:len(linea.strip())]
        indice = nombre.index(" ")
        nombre=nombre[0:indice]
        nombres_fotos.append(nombre)
        indice+=3
        for i in range(3):
            nombre = linea.strip()[indice:len(linea.strip())]
            indice2 = nombre.index(" ")
            coordenada_imagen.append(int(nombre[0:indice2]))
            indice+=indice2+1
        coordenada_imagen.append(int(nombre[indice2+1:]))
        coordenadas.append(coordenada_imagen)
    for linea in nombres_fotos:
        print(linea)
    for linea in coordenadas:
        print(linea)
    return

def recortar():
    contador = 0
    for linea in nombres_fotos:
        image_obj = Image.open(linea)
        cropped_image = image_obj.crop(coordenadas[contador])
        cropped_image.save(linea)
        contador+=1
    return

def resize():
    count=0
    for linea in nombres_fotos:
        img = cv2.imread(linea, cv2.IMREAD_UNCHANGED)
        dim = (96,96)
        resized=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
        cv2.imwrite(linea,resized)
    return

if __name__ == '__main__':
    guardarDatos()
    #recortar()
    resize()

