## SistemaExperto
## Práctica 1 - Sistemas Basados en Conocimiento
## Maestría Ing. Software - CENFOTEC

## Estudiantes:
- Sergio Oviedo
- Duncan Zenteno

## Requerimientos
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
- Consultar hechos
- Agregar hecho

## Requisitos
- Python 3.9
- Logpy

## Instalación del sistema
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/soviedos/SistemaExperto.git
   ```
    
2. Revisar el archivo relaciones.json el cual tiene los hechos predeterminados:
    ```json
    {
      "padre": [
        {
          "juan": "guillermo"
        },
        {
          "juan": "david"
        },
        {
          "juan": "adam"
        },
        {
          "guillermo": "stephanie"
        },
        {
          "david": "julia"
        },
        {
          "david": "pedro"
        },
        {
          "roberto": "joel"
        }
      ],
      "madre": [
        {
          "megan": "guillermo"
        },
        {
          "megan": "david"
        },
        {
          "megan": "adam"
        },
        {
          "emma": "stephanie"
        },
        {
          "olivia": "julia"
        },
        {
          "olivia": "pedro"
        }
      ],
      "hermano": [],
      "hermana": [],
      "hijo": [
        {
          "joel": "roberto"
        }
      ],
      "hija": [
        {
          "claudia": "olivia"
        }
      ],
      "esposo": [
        {
          "guillermo": "megan"
        }
      ],
      "esposa": [
        {
          "megan": "guillermo"
        }
      ],
      "ascendencia": [],
      "descendencia": [],
      "pareja": []
    }
    ```

3. Ejecuta el programa:
   ```bash
   python sistema_experto.py
   ```

4. Selecciona las opciones del menú según tus necesidades.
   ```bash
    Bienvenido al Sistema Experto
    1. Consultar hechos
    2. Agregar hecho
    3. Agregar regla (En construccion)
    4. Salir
    Por favor, elige una opción:
   ```

## Ejemplos
### 1. Consultar hechos
Actualmente el sistema solo soporta hechos de padre, madre, hijo, hija, hermano, hermana, esposo, esposa. Para consultar hechos, elija la primera opción y siga las indicaciones.
Ejemplos: 
    ```bash
    Por favor, introduzca el nombre de la persona: juan
    Por favor, introduzca la relacion que quiere consultar: padre
    Juan es padre de: 
    David
    ```
    ```bash
    Por favor, introduzca el nombre de la persona: guillermo
    Por favor, introduzca la relacion que quiere consultar: hermano
    Guillermo es hermano(a): 
    Adam
    David
    ```

### 2. Agregar hecho    
Para agregar un hecho, elija la primera opción y siga las indicaciones.
 
Ejemplo:
    ```bash
    Ingresar el nombre del hecho 'z' (padre, madre, hijo, hija, etc): padre
    Ingresa el nombre de la persona 'x' (Ex: 'x' es madre de 'y'): roberto
    Ingresa el nombre la persona 'y' (Ex: 'x' es madre de 'y'): joel 
    Se agrego el siguiente hecho: roberto es padre de joel.
    ```
    ```bash
    Ingresar el nombre del hecho 'z' (padre, madre, hijo, hija, etc): hijo
    Ingresa el nombre de la persona 'x' (Ex: 'x' es madre de 'y'): joel
    Ingresa el nombre la persona 'y' (Ex: 'x' es madre de 'y'): roberto
    Se agrego el siguiente hecho: joel es hijo de roberto.
    ```
    
### 4. Salir
Para salir del sistema.

