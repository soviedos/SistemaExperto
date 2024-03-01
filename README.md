# SistemaExperto
Sistema Experto que permite hacer consultas a una base de conocimientos y a una base de hechos.
El sistema debe ser inicializado y permitirle al usuario integrar nuevos hechos y reglas.

Los detalles sobre el sistema son los siguientes:
- Debe ser inicializado con cinco reglas.
- Debe ser inicializado con cinco hechos.
- Debe inicializar todos los operadores: hermano, hemana, padre, madre, familia, hijo, hija, descendencia, ascendencia, esposo, esposa, pareja.
- Debe tener una interfaz con el usuario de forma textual.
- Debe permitir la entrada de nuevos hechos.
- Debe permitir la entrada de nuevas reglas.
- Debe permitir guardar los nuevos hechos y reglas encontradas.
- Debe mostrar el proceso de inferencia.
- Puede integrar uno de los varios mecanismos de inferencia: encadenamiento hacia adelante, hacia atras o hıbrido.
- La base de conocimientos y hechos debe ser persistente.

El contexto del problema a solucionar es el de la representacion de un  arbol genealogico.

## Funcionalidades

- Mostrar la base de conocimientos actualizada, incluyendo hechos y reglas.
- Agregar nuevos hechos a la base de conocimientos.
- Agregar nuevas reglas a la base de conocimientos.
- Consultar relaciones utilizando encadenamiento hacia adelante.
- Reiniciar los hechos y las reglas a los valores predeterminados.

## Requisitos

- Python 3.x

## Instalación del sistema

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git

2. Ejecuta el programa:

   ```bash
   python sistema_experto.py

3. Selecciona las opciones del menú según tus necesidades.

   ```bash
      --- Menú ---
      1. Mostrar base de conocimientos
      2. Agregar nuevo hecho
      3. Agregar nueva regla
      4. Consultar con encadenamiento hacia adelante
      5. Reiniciar hechos y reglas a valores predeterminados
      6. Salir
      Ingrese el número de la opción deseada: 

## Ejemplos de Uso

   1. Crear Nuevo Hecho
      
   Agregar hecho sobre una nueva persona:
   Selecciona la opción 2 en el menú y sigue las instrucciones para ingresar el nombre de la persona y la descripción del hecho.
   
   *Nombre de la Persona:* Pablo
   *Descripción del Hecho:* es hijo de Marta y José.
   
   El sistema agregará el hecho "Pablo: es hijo de Marta y José" a la base de conocimientos.
   
   2. Crear Nueva Regla
      
   Agregar regla sobre una nueva relación familiar:
   Selecciona la opción 3 en el menú y sigue las instrucciones para ingresar la relación y los elementos de la regla.
   
   *Relación:* nieto
   *Elementos:* Ana, Marta, José
   
   El sistema agregará la regla "nieto de Ana y José es Marta" a la base de conocimientos.



