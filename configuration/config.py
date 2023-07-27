import os


class Datatest:

    # Tiempo de espera implicito de forma global
    IMPLICIT_WAIT = 10

    # Navegador: Este parametro selecciona donde ejecutar la prueba (Firefox, Chrome o Internet Explorer)
    BROWSER = "chrome"

    # Prueba del sistema operativo (linux, mac, windows)
    OS = "windows"

    # Ruta de la carpeta de recursos de drivers
    # (OJO ESTA RUTA NO DEBE SER MODIFICADA), en caso de faltar algun driver anexarlo a
    # la carpeta drivers dentro de resources en el proyecto
    resourcerFolder = os.path.join("driver")

    URL_WEB = "https://rahulshettyacademy.com/AutomationPractice/"
    
