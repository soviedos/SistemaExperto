import json

class SistemaExperto:
    def __init__(self):
        self.base_hechos = self.cargar_base_hechos()
        self.base_reglas = self.cargar_base_reglas()

        # Valores predeterminados solo si la base está vacía
        if not self.base_hechos or not self.base_reglas:
            self.inicializar_valores_predeterminados()

    def inicializar_valores_predeterminados(self):
        valores_predeterminados_hechos = {
            "Juan": "hijo de Karla y Pedro",
            "Ana": "hija de Karla y Pedro",
            "Karla": "esposa de Pedro",
            "Pedro": "esposo de Karla",
            "Carlos": "hijo de Ana y Juan"
        }
        self.base_hechos = valores_predeterminados_hechos
        self.guardar_base_hechos()

        valores_predeterminados_reglas = [
            ("hijo", ["Juan", "Karla", "Pedro"]),
            ("hija", ["Ana", "Karla", "Pedro"]),
            ("esposo", ["Pedro", "Karla"]),
            ("esposa", ["Karla", "Pedro"]),
            ("hermano", ["Carlos", "Ana", "Juan"])
        ]
        self.base_reglas = valores_predeterminados_reglas
        self.guardar_base_reglas()

    def mostrar_base_conocimientos(self):
        print("Base de Hechos:")
        for hecho, descripcion in self.base_hechos.items():
            print(f"{hecho}: {descripcion}")

        print("\nBase de Reglas:")
        for regla, elementos in self.base_reglas:
            print(f"{regla} de {' y '.join(elementos[1:])} es {elementos[0]}")

    def agregar_hecho(self, persona, descripcion):
        self.base_hechos[persona] = descripcion
        print(f"Hecho agregado: {persona}: {descripcion}")
        self.guardar_base_hechos()

    def agregar_regla(self, relacion, elementos):
        self.base_reglas.append((relacion, elementos))
        print(f"Regla agregada: {relacion} de {' y '.join(elementos[1:])} es {elementos[0]}")
        self.guardar_base_reglas()
        
    def encadenamiento_hacia_adelante(self, consulta):
        for regla, elementos in self.base_reglas:
            if regla == consulta:
                if all(elemento in self.base_hechos for elemento in elementos[1:]):
                    nuevo_hecho = f"{elementos[0]} es {consulta} de {' y '.join(elementos[1:])}"
                    self.base_hechos[elementos[0]] = nuevo_hecho
                    print(f"Inferencia exitosa: {nuevo_hecho}")
                    self.guardar_base_hechos()
                    return True
        print(f"No se pudo inferir {consulta}")
        return False

    def cargar_base_hechos(self):
        try:
            with open("base_hechos.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def cargar_base_reglas(self):
        try:
            with open("base_reglas.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def guardar_base_hechos(self):
        with open("base_hechos.json", "w") as file:
            json.dump(self.base_hechos, file)

    def guardar_base_reglas(self):
        with open("base_reglas.json", "w") as file:
            json.dump(self.base_reglas, file)

# Ejemplo de uso
sistema = SistemaExperto()

while True:
    print("\n--- Menú ---")
    print("1. Mostrar base de conocimientos")
    print("2. Agregar nuevo hecho")
    print("3. Agregar nueva regla")
    print("4. Consultar con encadenamiento hacia adelante")
    print("5. Reiniciar hechos y reglas a valores predeterminados")
    print("6. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        sistema.mostrar_base_conocimientos()
    elif opcion == "2":
        persona = input("Ingrese el nombre de la persona: ")
        descripcion = input("Ingrese la descripción del hecho: ")
        sistema.agregar_hecho(persona, descripcion)
    elif opcion == "3":
        relacion = input("Ingrese la relación (ej. hijo, hija, esposo): ")
        elementos = input("Ingrese los elementos de la regla separados por comas (ej. Juan, María, Pedro): ").split(", ")
        sistema.agregar_regla(relacion, elementos)
    elif opcion == "4":
        consulta = input("Ingrese la consulta a inferir: ")
        sistema.encadenamiento_hacia_adelante(consulta)
    elif opcion == "5":
        sistema.inicializar_valores_predeterminados()
        print("Hechos y reglas reiniciados a los valores predeterminados.")
    elif opcion == "6":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
