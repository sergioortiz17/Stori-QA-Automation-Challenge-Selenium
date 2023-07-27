# Stori Challenge Sergio Ortiz version WEB Selenium
# STACK : Behave Python Cucumber-Gherkin POM
# Reporte Allure y xml junit

Link Google Drive Video

https://drive.google.com/file/d/1TaL6V0Zcz8oA02dKfa71RsRBkgR4cwiJ/view?usp=drive_link

# Requerimientos 
1-Python instalado https://www.python.org/
2-Administrador de paquetes pip  (Verificas con pip --version)
3- pip install virtualenv (venv opcional-deseable -nice to have)
4- Instalacion allure report https://www.skill2lead.com/allure-report/allure-report-behave-allure-report-configuration.php

## Uso

Para ejecutar las pruebas, se deben seguir los siguientes pasos:

1. Clonar el repositorio en tu máquina local.
2. Crear un entorno virtual e instala dependencias dentro con `pip install -r requirements.txt` en la raiz del proyecto (opcional deseable nicetohave).
3. Descargar los drivers para el navegador que se va a utilizar y colocarlos en la carpeta `Drivers`. (No aplica porque deje el ultimo en el proyecto pero si se actualiza el navegador hay que colocar el chromedriver que lo soporte)
4. Ejecutar prueba usando los comandos o sus shortcuts `comandos.txt`.
    
    Run sin logs solo viendo la interfaz grafica
	`behave`
    Run test viendo logs en consola
    `make behave_chrome` o `behave --no-capture`  
    Run y genera folder reports con formato de allure para levantar reporte html
    `make behave_report` o `behave -f allure_behave.formatter:AllureFormatter -o reports/` 
    Run y genera file con reporte xml
    `make behave_xml` o `behave --junit --junit-directory ./report`

# REPORTE
Para ver los reportes de Allure en la carpeta reports/ (despues de haberlo ejecutado con `make behave_report` o `behave -f allure_behave.formatter:AllureFormatter -o reports/`)ejecuta el siguiente comando en la carpeta raiz, para que levante el servidor y puedas verlo en un puerto local de tu browser  
    `make allure` o `allure serve reports/`

# Estructura
- Stori-QA-Automation-Challenge-Selenium
    - configuration
    - drivers  (chromedriver)  
    - features
        - Pages_Object
            - __init__.py
            - PracticePage.py   (POM)                                     
        - steps
            - __init__.py
            - AutomationPractice.py
        - test            
            - __init__.py
            - AutomationPractice.feature
        - enviroment.py (Hooks)       
    - support (Actions DriverFactory CreateDriver)
    - web (applications.py init class)
    - requirements.txt (contiene lista de dependencias)  
    - Makefile (rules shorcuts para scripts por consola)                  
    - reports (solo aparece si ejecutas `make behave_report`)

## Ayuda Extra con instalación del archivo requirements

Instala las dependencias necesarias para este proyecto, sigue los siguientes pasos:

1. Después de descargar el repositorio, abre tu IDE y selecciona la carpeta del proyecto para crear un entorno virtual de Python. Asegúrate de tener Python 3.11 o una versión superior instalada.
2. Crea una variable de entorno para el intérprete de Python actualizado. Copia la ruta absoluta de la variable de entorno hasta la carpeta "Scripts".
3. Abre una consola de comando y accede a la ruta copiada.
4. Ejecuta el siguiente comando para activar la variable de entorno:
`activate`
5. Una vez allí, ejecuta el siguiente comando para instalar todas las dependencias del proyecto:
`pip install -r requirements.txt`
6. Recuerda activar tu venv para correr los test
