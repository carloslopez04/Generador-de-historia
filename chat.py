import requests
import json

url = "http://127.0.0.1:5000/v1/completions"
headers = {"Content-Type": "application/json"}

def creatividad():
    """
    Función para seleccionar el nivel de creatividad.
    """
    print("Selecciona el nivel de creatividad:")
    print("a) Creatividad alta")
    print("b) Creatividad media")
    print("c) Creatividad baja")

    option = input("Elige una opción (a/b/c): ").lower()
    creativity_levels = {"a": 0.9, "b": 0.7, "c": 0.3}
    return creativity_levels.get(option, 0.7)  # Creatividad por defecto en caso de que no se escoja

def historia():
    """
    Genera una historia basándose en los datos proporcionados por el usuario.
    """
    # Solicitar datos al usuario
    personaje1 = input("Introduce el nombre del personaje principal: ")
    personaje2 = input("Introduce el nombre del personaje secundario: ")
    lugar = input("¿Dónde transcurre la historia? ")
    trama = input("¿Qué acción importante sucede en la historia? ")

    # Configuración de creatividad
    temperature = creatividad()

    # Crear el prompt para la historia
    prompt = (f"Escribe una historia emocionante. "
              f"El personaje principal es {personaje1}, "
              f"acompañado por {personaje2}. "
              f"La historia transcurre en {lugar}, "
              f"donde ocurre lo siguiente: {trama}.")

    # Configurar el cuerpo de la solicitud
    body = {
        "prompt": prompt,
        "max_tokens": 500,  # Longitud máxima de la historia
        "temperature": temperature
    }

    try:
        # Realizar la solicitud a la API
        response = requests.post(url=url, headers=headers, json=body)
        response.raise_for_status()  # Levantar excepción si hay errores HTTP
        message_response = json.loads(response.content.decode("utf-8"))

        # Extraer y mostrar la historia generada
        generar_historia = message_response["choices"][0]["text"]
        print("\n--- Historia Generada ---\n")
        print(generar_historia)
        print("\n--- Fin de la Historia ---\n")
    except KeyError: 
        print("Error en la generación de la historia. Asegurate de que todo este bien.")

# Ejecutar el programa
if __name__ == "__main__":
    print("Generador de Historias con AI\n")
    historia()