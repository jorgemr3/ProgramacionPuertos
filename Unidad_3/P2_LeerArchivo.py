def cargarArchivo():
    archivo = open("../Unidad_3/Archivos/ejemplo.csv")
    contenidoArchivo = archivo.readlines()
    lineas = [i[0:-2].split(",") for i in contenidoArchivo]
    listaNueva = []
    for i in lineas:
        listaNueva.append([i[0], int(i[1])])
    return listaNueva
if __name__ == "__main__":
    a = cargarArchivo()
    print(a)
