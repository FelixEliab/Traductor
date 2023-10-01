def cargar_diccionario(archivo):
    diccionario = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                clave, valor = linea.strip().split('=')
                diccionario[clave] = valor
    except FileNotFoundError:
        diccionario = {}
    return diccionario

def guardar_diccionario(archivo, diccionario):
    with open(archivo, 'w') as f:
        for clave, valor in diccionario.items():
            f.write(f"{clave}={valor}\n")

def agregar_traduccion(archivo, palabra_origen, palabra_destino):
    diccionario = cargar_diccionario(archivo)
    diccionario[palabra_origen] = palabra_destino
    guardar_diccionario(archivo, diccionario)

def traducir(archivo, codigo, palabra):
    diccionario = cargar_diccionario(archivo)
    if codigo == "EN-ES" and palabra in diccionario:
        return diccionario[palabra]
    elif codigo == "ES-EN":
        for clave, valor in diccionario.items():
            if valor == palabra:
                return clave
    return "Traducción no encontrada"

def main():
    archivo_diccionario = "EN-ES.txt"
    
    while True:
        print("\n1. Agregar nueva traducción")
        print("2. Traducir palabra")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            palabra_origen = input("Ingrese la palabra en inglés: ")
            palabra_destino = input("Ingrese la traducción en español: ")
            agregar_traduccion(archivo_diccionario, palabra_origen, palabra_destino)
            print("Traducción agregada exitosamente.")
        elif opcion == "2":
            codigo = input("Ingrese el código de traducción (EN-ES o ES-EN): ")
            palabra = input("Ingrese la palabra a traducir: ")
            resultado = traducir(archivo_diccionario, codigo, palabra)
            print(f"Traducción: {resultado}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
