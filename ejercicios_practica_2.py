# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
   
    
    # Leer todos los datos y almacenarlos en una 
    # lista de diccionarios
    with open(archivo, "r") as archivo_csv:
        total= 0
        lista = list(csv.DictReader(archivo_csv))
        for fila in lista: 
            for item, cantidad in fila.items():
                if item == "tornillos":
                    total += int(cantidad)
        
        print ("La cantidad de tornillos: ", total)

    archivo_csv.close()


def ej4():
    print('Ejercicios con archivos CSV 2º')
    
    
    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo = 'propiedades.csv'
    departamento_2_ambientes= 0
    departamento_3_ambientes= 0
    with open(archivo, "r") as propiedades_csv: 
        lista = list(csv.DictReader(propiedades_csv))
        for fila in lista:
            for k, v in fila.items():
                if k == "ambientes":
                    if v == "2":
                        departamento_2_ambientes +=1 
                    elif v == "3":
                        departamento_3_ambientes +=1
    
        print("Departamentos diponibles de 2 ambientes: ", departamento_2_ambientes, "Departamentos  disponibles de 3 ambientes", departamento_3_ambientes)
        propiedades_csv.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()

                    















if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
