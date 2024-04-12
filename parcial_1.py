import os # os es un módulo de Python que proporciona funciones para interactuar con el sistema operativo subyacente en el que se ejecuta Python. Permite realizar una variedad de tareas
import requests  #  es una biblioteca de Python que permite realizar solicitudes HTTP de manera sencilla y flexible. Facilita la interacción con servicios web y la obtención de recursos a través de la red utilizando los métodos HTTP como GET, POST, PUT, DELETE, etc.
from bs4 import BeautifulSoup # Beautiful Soup es una biblioteca de Python diseñada para extraer datos de archivos HTML y XML.

# Definición de códigos de colores ANSI
color_amarillo = "\033[93m"
color_azul = "\033[94m"
color_verde = "\033[92m"
color_rojo = "\033[91m"
color_reset = "\033[0m"

class Shinigami: # Se define la clase Shinigami
    def __init__(self, nombre, arma, habilidad_especial): # Metodo magico, se inicializan las propiedades del Shinigami
        self.nombre = nombre # Nombre del Shinigami
        self.raza = "Shinigami"  # Raza del Shinigami (siempre será "Shinigami")
        self.arma = arma # Arma del Shinigami
        self.habilidad_especial = habilidad_especial # Habilidad especial del Shinigami

    def detalles(self): # Método para obtener los detalles del Shinigami
        return f"{color_azul}Nombre: {color_reset} {color_rojo}{self.nombre}{color_reset}, {color_azul}Raza: {color_reset} {color_rojo}{self.raza}{color_reset}, {color_azul}Arma: {color_reset} {color_rojo}{self.arma}{color_reset}, {color_azul}Habilidad Especial: {color_reset} {color_rojo}{self.habilidad_especial}{color_reset}"
        # Devuelve una cadena formateada con los detalles del Shinigami, incluyendo nombre, raza, arma y habilidad especial

class Quincy: # Se define la clase Quincy
    def __init__(self, nombre): # Metodo magico para inicializar las propiedades del Quincy
        self.nombre = nombre # Nombre del Quincy
        self.raza = "Quincy" # Raza del Quincy
        self.arma = None # Arma del Quincy (si la tiene)
        self.habilidad_especial = None # Habilidad del Quincy (si la tiene)

    def detalles(self): # Metodo para obtener los detalles del Quincy  
        return f"{color_azul}Nombre: {color_reset} {color_rojo}{self.nombre}{color_reset}, {color_azul}Raza: {color_reset} {color_rojo}{self.raza}{color_reset}"
        # Se devuelve la cadena formateada con los detalles del Quincy

class Hollow: # Se define la clase Hollow
    def __init__(self, nombre, habilidad_especial): # Metodo magico para inicializar las propiedades del Hollow
        self.nombre = nombre # Nombre del Hollow
        self.raza = "Hollow" # Raza del Hollow
        self.arma = None # Arma del Hollow (si la tiene)
        self.habilidad_especial = habilidad_especial # Habilidad del Hollow

    def detalles(self): # Metodo para obtener los detalles del Hollow       
        return f"{color_azul}Nombre: {color_reset} {color_rojo}{self.nombre}{color_reset}, {color_azul}Raza: {color_reset} {color_rojo}{self.raza}{color_reset}, {color_azul}Habilidad Especial: {color_reset} {color_rojo}{self.habilidad_especial}{color_reset}"

class Programa: #clase llamada Programa que contiene varios métodos estáticos útiles para el funcionamiento del programa
    personajes_creados = [] # Se define una lista para almacenar los personajes

    @staticmethod
    def limpiar_consola():
        os.system('cls' if os.name == 'nt' else 'clear') #Este es un método estático llamado limpiar_consola(), 
                                                        # que se encarga de limpiar la consola. Utiliza la función 
    @staticmethod
    def pausar_para_continuar(): #Este es otro método estático llamado pausar_para_continuar(),
        input("Presione la tecla enter para continuar...") # que pausa la ejecución del programa hasta que el usuario presione
        Programa.limpiar_consola() # la tecla Enter. Después de que el usuario presiona Enter, se llama al método limpiar_consola()

    @staticmethod
    def detalle_personaje(character_name): # método estático llamado detalle_personaje(character_name),
        url = f"https://bleach.fandom.com/es/wiki/{character_name}" # que recibe el nombre de un personaje como argumento.
        try:
            response = requests.get(url)
            if response.status_code == 200: # Se araña la URL para tomar la informacion
                soup = BeautifulSoup(response.text, "html.parser")
                paragraphs = soup.find_all("p")
                for p in paragraphs: # Si la respuesta fue exitosa, se crea un objeto BeautifulSoup
                    if character_name in p.get_text(): #para analizar el HTML de la página. Se buscan todos los elementos de párrafo (<p>)  
                        info_text = p.get_text(strip=True) # y se itera sobre ellos. Si el nombre del personaje está presente en el texto
                        return info_text #de un párrafo, se devuelve ese texto como información sobre el personaje.
                return f"No se pudo encontrar información sobre {character_name}."
            else:
                return f"Error al obtener la página: {response.status_code}"
        except requests.RequestException as e:
            return f"Error de conexión: {e}"

    @staticmethod
    def crear_personajes_shinigami(tipo_personaje):  #se encarga de crear personajes Shinigami basados en la información obtenida de una tabla en una página web
        url = "https://bleach.fandom.com/es/wiki/Lista_de_Armas" #Se define la URL de la página de la wiki de Bleach que contiene la lista de armas.
        response = requests.get(url) # Se realiza araña la URL definida y se guarda la respuesta en la variable response.
        if response.status_code == 200: # Verificar si la solicitud fue exitosa , la URL manda la señal 200 para ver si se cumple
            soup = BeautifulSoup(response.content, 'html.parser') # Se crea un objeto BeautifulSoup para analizar el contenido HTML de la respuesta
            tabla = soup.find('table')
            filas = tabla.find_all('tr') #Se encuentra la tabla en la página y se obtienen todas las filas de la tabla excepto la primera,
            contador = 1 #que generalmente contiene encabezados de columna
            nombres_personajes = []
            armas_personajes = []
            habilidades_personajes = []

            for fila in filas[1:]:
                columnas = fila.find_all('td')
                if len(columnas) >= 3:
                    nombre_personaje = columnas[1].text.strip()
                    nombres_personajes.append(nombre_personaje)
                    nombre_arma = columnas[0].text.strip()
                    armas_personajes.append(nombre_arma)
                    habilidad_especial = columnas[2].text.strip()
                    habilidades_personajes.append(habilidad_especial)
                    print(f"{contador}. {nombre_personaje}")
                    contador += 1

            seleccion = input("Por favor, seleccione el número correspondiente al personaje deseado: ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(nombres_personajes):
                indice_seleccionado = int(seleccion) - 1
                nombre_personaje = nombres_personajes[indice_seleccionado]
                arma_personaje = armas_personajes[indice_seleccionado]
                habilidad_personaje = habilidades_personajes[indice_seleccionado]
                raza_personaje = "Shinigami" if tipo_personaje == "1" else "Visored"
                Programa.personajes_creados.append(Shinigami(nombre_personaje, arma_personaje, habilidad_personaje))
                print(f"{color_amarillo}El personaje {nombre_personaje} ha sido creado.{color_reset}")
                print(f"{color_azul}Nombre del personaje: {color_reset} {color_rojo}{nombre_personaje}{color_reset}")
                print(f"{color_azul}Raza del personaje: {color_reset} {color_rojo}{raza_personaje}{color_reset}")
                print(f"{color_azul}Arma del personaje: {color_reset} {color_rojo}{arma_personaje}{color_reset}")
                print(f"{color_azul}Habilidad especial del personaje: {color_reset} {color_rojo}{habilidad_personaje}{color_reset}")
            else:
                print("Selección inválida. Por favor, seleccione un número válido.")
        else:
            print("Error al obtener la página:", response.status_code)

    @staticmethod # Metodo estatico 
    def crear_personajes_hollow(): 
        url = "https://bleach.fandom.com/es/wiki/Hollow#Menos" # URL de la página que contiene la información sobre los personajes Hollow
        start_text = "Menos Grande" # Texto que marca el comienzo de la sección de personajes Hollow
        end_text = "Arrancar" # Texto que marca el final de la sección de personajes Hollow
        response = requests.get(url)  # Realiza una solicitud GET a la URL
        if response.status_code == 200: # Verifica si la solicitud fue exitosa (código de estado 200)
            soup = BeautifulSoup(response.text, 'html.parser')  # Parsea el contenido HTML de la página
            h3_elements = soup.find_all('h3') # Encuentra todos los elementos h3 en la página
            start_capture = False # Bandera para indicar cuándo comenzar a capturar los nombres de los Hollows
            hollows = []  # Lista para almacenar los nombres y habilidades especiales de los Hollows
            for element in h3_elements: # Itera sobre todos los elementos h3 encontrados
                if element.text.strip() == start_text:  # Comprueba si el texto del elemento coincide con el texto de inicio
                    start_capture = True
                if start_capture: # Si se debe comenzar a capturar, extrae el nombre y la habilidad especial del Hollow
                    hollow_name = element.text.strip()
                    habilidad_especial = element.find_next('p').text.strip()
                    hollows.append((hollow_name, habilidad_especial))
                if element.text.strip() == end_text: # Comprueba si se ha alcanzado el final de la sección de Hollows
                    break
            for i, (nombre, _) in enumerate(hollows, 1): # Imprime la lista de Hollows disponibles y solicita al usuario que seleccione uno
                print(f"{i}. {nombre}")
            seleccion = input("Por favor, seleccione el número correspondiente al Hollow deseado: ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(hollows): # Verifica si la selección del usuario es válida
                indice_seleccionado = int(seleccion) - 1
                nombre_hollow, habilidad_especial_hollow = hollows[indice_seleccionado]
                # Imprime los detalles del Hollow seleccionado
                print(f"{color_amarillo}El Hollow {nombre_hollow} ha sido creado.{color_reset}")
                print(f"{color_azul}Nombre del Hollow: {color_reset} {color_rojo}{nombre_hollow}{color_reset}")
                print(f"{color_azul}Habilidad especial del Hollow: {color_reset} {color_rojo}{habilidad_especial_hollow}{color_reset}")
                Programa.personajes_creados.append(Hollow(nombre_hollow, habilidad_especial_hollow)) # Agrega el Hollow creado a la lista de personajes creados en la clase Programa
            else:
                print("Selección inválida. Por favor, seleccione un número válido.") # Mensaje de error si la selección del usuario no es válida
        else:
            print("Error al obtener la página:", response.status_code) # Mensaje de error si la solicitud GET falla

    @staticmethod
    def extraer_enlaces_desde_uryu_hasta_hubert():
        url = "https://bleach.fandom.com/es/wiki/Lista_de_Quincy" # URL de la página que contiene la lista de Quincy
        response = requests.get(url) # Realiza una solicitud GET a la URL
        soup = BeautifulSoup(response.text, 'html.parser') # Analiza el contenido HTML de la página
        enlaces = soup.find_all('a') # Encuentra todos los elementos de enlace <a> en la página
        enlaces_uryu_hubert = [] # Lista para almacenar los enlaces desde Uryū hasta Hubert
        empezar_almacenar = False # Bandera para indicar cuándo empezar a almacenar los enlaces
        numero_enlace = 1 # Contador para numerar los enlaces almacenados
        for enlace in enlaces: # Itera sobre todos los enlaces encontrados
            if enlace.text == "Uryū Ishida":  # Comprueba si el texto del enlace coincide con "Uryū Ishida"
                empezar_almacenar = True
            if empezar_almacenar: # Si se debe empezar a almacenar, añade el enlace a la lista junto con su número de enlace
                enlaces_uryu_hubert.append((numero_enlace, enlace.text))
                numero_enlace += 1
            if empezar_almacenar and enlace.text == "Hubert": # Comprueba si se ha alcanzado el enlace "Hubert" y termina de almacenar
                break
        return enlaces_uryu_hubert # Retorna la lista de enlaces desde Uryū hasta Hubert

    @staticmethod
    def seleccionar_quincy():
        enlaces_quincy = Programa.extraer_enlaces_desde_uryu_hasta_hubert()
        if enlaces_quincy:
            print(f"{color_amarillo}Quincies Disponibles:{color_reset}")
            for i, (_, nombre_quincy) in enumerate(enlaces_quincy, 1):
                print(f"{i}. {nombre_quincy}")
            seleccion = input("Por favor, seleccione el número correspondiente al Quincy deseado: ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(enlaces_quincy):
                indice_seleccionado = int(seleccion) - 1 # Convierte la entrada del usuario a un entero y luego resta 1 a ese valor.
                _, nombre_quincy = enlaces_quincy[indice_seleccionado]
                print(f"{color_azul}Quincy seleccionado: {color_reset} {color_rojo}{nombre_quincy}{color_reset}")
                Programa.personajes_creados.append(Quincy(nombre_quincy))
            else:
                print("Selección inválida. Por favor, seleccione un número válido.")
        else:
            print("No se pudieron encontrar Quincies disponibles en la página.")

    @staticmethod
    def validar_opcion(opcion):
        try: # Intenta convertir la opción a un entero
            opcion_int = int(opcion)
            if opcion_int < 1 or opcion_int > 5: # Verifica si la opción está dentro del rango válido (1-5)
                raise ValueError # Si la opción está fuera del rango, lanza una excepción de ValueError
            return opcion_int # Si la opción es válida, devuelve el valor convertido a entero
        except ValueError: # Si ocurre una excepción al intentar convertir la opción a entero o si la opción está fuera del rango,
            return None     # devuelve None para indicar que la opción no es válida

    @classmethod
    def ejecutar_opcion(cls, opcion):
        if opcion == 1: # Verifica la opción seleccionada por el usuario y ejecuta la acción correspondiente
            # Opción para crear un personaje
            tipo_personaje = input(f"""{color_amarillo} 
        ---------Crear Personaje--------- :{color_reset}
        1. {color_verde}Shinigami{color_reset}
        2. {color_verde}Hollow{color_reset}
        3. {color_verde}Quincy{color_reset}
        4. {color_verde}Visored (Shinigami con poderes Hollow){color_reset}
        Seleccione una opción: """)
            if tipo_personaje in ["1", "4"]: # Verifica el tipo de personaje seleccionado y llama al método correspondiente para crearlo
                cls.crear_personajes_shinigami(tipo_personaje)
            elif tipo_personaje == "2": # Opción para mostrar los personajes creados
                cls.crear_personajes_hollow()
            elif tipo_personaje == "3": # Opción para mostrar detalles de un personaje específico
                cls.seleccionar_quincy()
            else:
                print("Opción no válida.")
        elif opcion == 2:
            print("Personajes Creados:")
            for i, personaje in enumerate(cls.personajes_creados, 1):
                print(f"{i}. {personaje.detalles()}")
        elif opcion == 3:
            if cls.personajes_creados: # Opción para mostrar detalles de un personaje específico, Verifica si hay personajes creados para continuar
                for i, personaje in enumerate(cls.personajes_creados, 1): # Itera sobre cada personaje de la lista para pasar a imprimirlos
                    print(f"{i}. {personaje.nombre} - {personaje.raza}") # imprime el nombre y la raza enumerando en orden ascendente
                seleccion = input("Por favor, seleccione el número correspondiente al personaje deseado: ") # Solicitamos el numero del personaje que desea seleccionar
                if seleccion.isdigit() and 1 <= int(seleccion) <= len(cls.personajes_creados): #verificamos si la entrada del usuario es un dígito y si está dentro del rango válido de índices de la lista
                    indice_seleccionado = int(seleccion) - 1 # Convierte la entrada del usuario a un entero y luego resta 1 a ese valor.
                    personaje = cls.personajes_creados[indice_seleccionado] # Se obtiene el personaje seleccionado para 
                    print(f"Detalles del personaje seleccionado:") # Pasar a imprimir los detalles de este
                    descripcion = cls.detalle_personaje(personaje.nombre)
                    print(f"Nombre: {personaje.nombre} - {personaje.raza}")
                    print(f"Detalle: {descripcion}")
                    if personaje.raza == "Shinigami" or personaje.raza == "Visored": # Si el personaje es Shinigami o Visored,
                        print(f"Arma: {personaje.arma}")                             # imprime lo correspondiente
                    print(f"Habilidad Especial: {personaje.habilidad_especial}")
                else:
                    print("Selección inválida. Por favor, seleccione un número válido.") # Si la opcion es invalida muestra el mensaje
            else:
                print("No hay personajes creados.") # Si no hay personajes creados imprime el mensaje11
        elif opcion == 4: # Opción para realizar un ataque entre personajes
            if cls.personajes_creados:
                print("Personajes Disponibles para Atacar:")
                for i, personaje in enumerate(cls.personajes_creados, 1):
                    print(f"{i}. {personaje.nombre} - {personaje.raza}")
                seleccion_atacante = input("Seleccione el número correspondiente al personaje que quiere atacar: ")
                if seleccion_atacante.isdigit() and 1 <= int(seleccion_atacante) <= len(cls.personajes_creados): #verificamos si la entrada del usuario es un dígito y si está dentro del rango válido de índices de la lista
                    indice_atacante = int(seleccion_atacante) - 1 # Convierte la entrada del usuario a un entero y luego resta 1 a ese valor.
                    atacante = cls.personajes_creados[indice_atacante]
                    print("Personajes disponibles para ser atacados:")
                    for i, objetivo in enumerate(cls.personajes_creados, 1):
                        if i != indice_atacante + 1:
                            print(f"{i}. {objetivo.nombre}")
                    seleccion_objetivo = input("Seleccione el número correspondiente al personaje al que quiere atacar: ")
                    if seleccion_objetivo.isdigit() and 1 <= int(seleccion_objetivo) <= len(cls.personajes_creados):
                        indice_objetivo = int(seleccion_objetivo) - 1
                        objetivo = cls.personajes_creados[indice_objetivo]
                        while True:
                            usar_poder_especial = input("¿Desea usar el poder especial en el ataque? (s/n): ")
                            if usar_poder_especial.lower() == 's':
                                print(f"{atacante.nombre} ataca con su poderosisimo ataque especial a {objetivo.nombre}!")
                                break
                            elif usar_poder_especial.lower() == 'n':
                                print(f"{atacante.nombre} ataca a {objetivo.nombre} con su arma {atacante.arma}!")
                                break
                            else:
                                print("Por favor, ingrese 's' para sí o 'n' para no.")
                                continue
                    else:
                        print("Selección inválida para el objetivo. Intente de nuevo.")
                else:
                    print("Selección inválida para el atacante. Intente de nuevo.")
            else:
                print("No hay personajes creados para realizar un ataque.")
        elif opcion == 5: # Opción para salir del programa
            print("***SALIENDO DEL PROGRAMA****")
            print("****Realizado por:*****")
            print("Sebastian Orrego Urrea")
            print("Mateo Gallelo Gonzalez")
            print("Valentina Osorio Buitrago")
            exit()

    @classmethod
    def iniciar(cls):
        while True:
            print(f"""{color_amarillo}
            Menú :{color_reset}
            1. {color_verde}Crear personaje{color_reset}
            2. {color_verde}Ver personajes creados{color_reset}
            3. {color_verde}Ver detalles de un personaje{color_reset}
            4. {color_verde}Activar Habilidad o atacar{color_reset}
            5. {color_rojo}Salir{color_reset}""")
            opcion_usuario = input("Seleccione una opción: ")
            opcion_validada = cls.validar_opcion(opcion_usuario)
            if opcion_validada is not None:
                cls.ejecutar_opcion(opcion_validada)
                cls.pausar_para_continuar()
            else:
                print('Oops! Opción no válida. Intente de nuevo.')
                cls.pausar_para_continuar()

if __name__ == '__main__':
    Programa.iniciar()
    """Aquí, se llama al método iniciar() de la clase Programa cuando este script es ejecutado como el programa 
    principal. Esto iniciará el programa y mostrará el menú al usuario para que pueda interactuar con él."""
