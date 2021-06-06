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
    
    csvfile = open('stock.csv')
    stock = list(csv.DictReader(csvfile))
    csvfile.close()

    stock_tornillos = 0

    for fila in stock:
        print(fila['tornillos'])
        
        try:
            stock_tornillos = stock_tornillos + int(fila['tornillos'])
        except:
            print('Ocurrió un error en la lectura de la variable')
    
    print('El stock total de tornillos es:', stock_tornillos) 

    return


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

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

    csvfile = open('propiedades.csv')
    propiedades = list(csv.DictReader(csvfile))
    csvfile.close()

    i = 0
    dpto_dos_ambientes = 0
    dpto_tres_ambientes = 0

    for fila in propiedades:
        try:
            ambientes = int(fila['ambientes'])
        except:
            print('El valor de la fila,', i, 'no se pudo leer correctamente')
        i += 1

        if ambientes == 2:
            dpto_dos_ambientes += 1
        elif ambientes == 3:
            dpto_tres_ambientes += 1

    print('La cantidad de departamentos de 2 ambientes disponible es:', dpto_dos_ambientes)
    print('La cantidad de departamentos de 3 ambientes disponible es:', dpto_tres_ambientes)
            
    return


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
