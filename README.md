# Proyecto de transcripción de audio con Deepgram API
Este es un proyecto de transcripción de audio que utiliza la API de Deepgram para realizar la transcripción. La aplicación permite subir archivos de audio y devuelve la transcripción del mismo en formato de texto.

## Requisitos
* Python 3.7 o superior
* pip
* Un API key de Deepgram

## Instalación
1. Clonar el repositorio:

```https://github.com/MartinAAcebeyL/apiAudioText.git```

2. Crear y activar un entorno virtual:

```python3 -m venv venv```

```source venv/bin/activate```

3. Instalar las dependencias:

```pip install -r requirements.txt```

4. Crear un archivo .env con la variable de entorno DEEPGRAM_API_KEY que contenga tu API key de Deepgram.
5. Iniciar la aplicación:

```python manage.py runserver```

## Pruebas y coverage
* Puedes ejecutar los tests con el siguiente comando:

```python manage.py test```

* También se puede generar un reporte de coverage con:

```coverage run --source='.' manage.py test```

```coverage report```

## Documentación
La documentación de la API se encuentra en la carpeta [docs](./DeepgramAudioTranscription/docs/). Incluye una descripción de las rutas disponibles y los parámetros que aceptan. La documentación fue generada con Postman.

## Pruebas con archivos de audio

[Video de referencia](https://www.youtube.com/watch?v=Sm56AE9yOuA)

En la carpeta [files](./files/) se encuentran varios archivos de audio que se pueden utilizar para probar la API de transcripción. Para realizar pruebas con alguno de estos archivos, se debe hacer lo siguiente:
1. Realizar una petición POST a la URL http://localhost:8000/api/transcription/ con el archivo de audio como parámetro. En Postman, esto se puede hacer a través de la sección "Body" y seleccionando "form-data" como tipo de dato. Luego, agregar una nueva entrada con la clave "audio" y seleccionar el archivo deseado como valor.
2. Enviar la petición y esperar la respuesta.



O tambien puede usar curl, para hacer las peticiones. A continuación se muestra un ejemplo de cómo realizar una prueba utilizando el archivo audio.wav

```curl -X POST -F "audio=@/path/to/audio.wav" http://localhost:8000/api/transcription/```

Donde /path/to/audio.wav es la ubicación del archivo audio.wav en el sistema de archivos local y http://localhost:8000/api/transcription/ es la URL de la API de transcripción. La respuesta de la API será un objeto JSON con la transcripción del archivo de audio.
