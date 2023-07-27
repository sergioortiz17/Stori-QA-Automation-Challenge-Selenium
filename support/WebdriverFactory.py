from selenium import webdriver
import os

from configuration.config import Datatest


class WebDriverFactory:

    @staticmethod
    def createNewWebDriver(browser_value, os_value):

        resourceFolder = Datatest.resourcerFolder  # Obtener la ruta de la carpeta Drivers
        if browser_value.upper() == "FIREFOX":
            if os_value.upper() == "WINDOWS":

                driver_path = os.path.join(resourceFolder, "/geckodriver.exe")
            else:
                driver_path = os.path.join(resourceFolder, "/geckodriver")
            driver = webdriver.Firefox(executable_path=driver_path)
        elif browser_value.upper() == "CHROME":
            if os_value.upper() == "WINDOWS":
                driver_path = os.path.join(resourceFolder, "/chromedriver.exe")
            else:
                driver_path = os.path.join(resourceFolder, "/chromedriver")
            driver = webdriver.Chrome(executable_path=driver_path)
        elif browser_value.upper() == "INTERNET EXPLORER":
            driver_path = os.path.join(resourceFolder, "/IEDriverServer.exe")
            driver = webdriver.Ie(executable_path=driver_path)
        else:
            print(
                "El driver no esta seleccionado en las propiedades, nombre invalido: " + browser_value + ", " + os_value)
            return None
        driver.maximize_window()
        return driver


