
archivo = open("../Unidad_3/Archivos/ejemplo.csv", "w")

listaNombres = [
    ["Clemente",26],
    ["Cristobal",17],
    ["Ana",5],
    ["Rene",30],
    ["Orozco",8],
    ["Jorge",72],
    ["Aquino",13],
    ["Badillo",37],
    ["Segoviano",40],
    ["Salazar",75],
    ["Eduardo",50],
    ["Natalia",12],
    ["Rodrigo",11],
    ["Miguel",99],
    ["Amando",69],
    ["Raul",14],
    ["Lexiss",3],
    ["Mariana",33],
    ["Angel",10],
    ["Emmanuel",51],
    ["Isaac",70],
    ["Sergio",85],
    ["Paniagua",82]
]

print(listaNombres)

for datosNombre in listaNombres:
    for dato in datosNombre:
        archivo.write(str(dato) + ",")
    archivo.write("\n")

archivo.flush()
archivo.close()