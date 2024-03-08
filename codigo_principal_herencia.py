import json
from logpy import Relation, facts, run, conde, var, eq

if __name__=='__main__':
    padre = Relation()
    madre = Relation()
    hermano = Relation()
    hermana = Relation()
    hijo = Relation()
    hija = Relation()
    esposo = Relation()
    esposa = Relation()
    ascendencia = Relation()
    descendencia = Relation()
    pareja = Relation()
    
    with open('relaciones.json') as f:
        d = json.loads(f.read())

    for item in d['padre']:
        facts(padre, (list(item.keys())[0], list(item.values())[0]))

    for item in d['madre']:
        facts(madre, (list(item.keys())[0], list(item.values())[0]))

    for item in d['hermano']:
        facts(hermano, (list(item.keys())[0], list(item.values())[0]))

    for item in d['hermana']:
        facts(hermana, (list(item.keys())[0], list(item.values())[0]))

    for item in d['hijo']:
        facts(hijo, (list(item.keys())[0], list(item.values())[0]))

    for item in d['hija']:
        facts(hija, (list(item.keys())[0], list(item.values())[0]))

    for item in d['esposo']:
        facts(esposo, (list(item.keys())[0], list(item.values())[0]))

    for item in d['esposa']:
        facts(esposa, (list(item.keys())[0], list(item.values())[0]))

    for item in d['ascendencia']:
        facts(ascendencia, (list(item.keys())[0], list(item.values())[0]))

    for item in d['descendencia']:
        facts(descendencia, (list(item.keys())[0], list(item.values())[0]))

    for item in d['pareja']:
        facts(pareja, (list(item.keys())[0], list(item.values())[0]))

    x = var()

    # Verifica si 'x' es padre de 'y'
    def padres(x, y):
        return conde([padre(x, y)])
    
    # Verifica si 'x' es madre de 'y'
    def madres(x, y):
        return conde([madre(x, y)])

    # Verifica si 'x' & 'y' son hermanos
    def hermanos(x, y):
        temp = var()
        return conde(padres(temp, x), padres(temp, y), [madres(temp, x), madres(temp, y)])
    
    # Verifica si 'x' es hijo de 'y'
    def hijos(x, y):
        return conde([padre(x, y)], [madre(x, y)])
    
    def esposos(x, y):
        return conde([esposo(x, y)], [esposa(x, y)])
    
    def agregar_hecho(x, y, z):
        with open('relaciones.json', 'r') as file:
            data = json.load(file)
        
        data[z].append({x: y})
        
        with open('relaciones.json', 'w') as file:
            json.dump(data, file, indent=2)
        
        print(f"Se agrego el siguiente hecho: {x} es {z} de {y}.")

    def consultar(relacion, nombre):
        x = var()
        if relacion == 'padre':
            salida = run(0, x, padres(nombre, x))
            print(nombre.capitalize() + " es padre de: ")
            for item in salida:
                print(item.capitalize())
            print("\n")             
        elif relacion == 'madre':
            salida = run(0, x, madres(nombre, x))
            print(nombre.capitalize() + " es madre de: ")
            for item in salida:
                print(item.capitalize())
            print("\n")     
        elif relacion == 'hermano' or relacion == 'hermana':
            salida = run(0, x, hermanos(x, nombre))
            hermano = [x for x in salida if x != nombre]
            print(nombre.capitalize() + " es hermano(a): ")
            for item in hermano:
                print(item.capitalize())
            print("\n") 
        elif relacion == 'hijo' or relacion == 'hija':
            salida = run(0, x, hijos(x, nombre))
            print(nombre.capitalize() + " es hijo(a) de:")
            for item in salida:
                print(item.capitalize())
            print("\n")  
        elif relacion == 'esposo' or relacion == 'esposa':
            salida = run(0, x, esposos(nombre, x))
            print(nombre.capitalize() + " es esposo(a) de:")
            for item in salida:
                print(item.capitalize())
            print("\n")  

    def salir():
        print("Gracias por usar el sistema")
        exit(0)

    def mostrar_menu():
        while True:
            print("\nBienvenido al Sistema Experto")
            print("1. Consultar hechos")
            print("2. Agregar hecho")
            print("3. Agregar regla (En construccion)")
            print("4. Salir")
            opcion = input("Por favor, elige una opción: ")

            if opcion == '1':
                nombre = input("Por favor, introduzca el nombre de la persona: ").lower()
                relacion = input("Por favor, introduzca la relacion que quiere consultar: ").lower()
                consultar(relacion, nombre)

            elif opcion == '2':
                z = input("Ingresar el nombre del hecho 'z' (padre, madre, hijo, hija, etc): ")
                x = input("Ingresa el nombre de la persona 'x' (Ex: 'x' es madre de 'y'): ")
                y = input("Ingresa el nombre la persona 'y' (Ex: 'x' es madre de 'y'): ")
                agregar_hecho(x, y, z)
                
            elif opcion == '3':
                salir()
            
            elif opcion == '4':
                salir()

            else:
                print("Opción no válida, por favor intenta de nuevo")


    if __name__ == '__main__':
        mostrar_menu()
