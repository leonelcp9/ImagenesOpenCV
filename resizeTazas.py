import cv2
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

def encuentra_nombre(cadena):
    return
if __name__ == '__main__':
    guardarDatos()
    
