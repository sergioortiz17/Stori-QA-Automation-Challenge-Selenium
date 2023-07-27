from selenium import webdriver

from configuration.config import Datatest
from support.WebdriverFactory import WebDriverFactory


class CreateDriver(WebDriverFactory):

    @staticmethod
    def set_up_config():

        print("################")
        print("[ POM CONFIGURACION  ] - Lee la configuracion de propiedades basicas del archivo config.py")
        print("################")
        browser = Datatest.BROWSER
        os = Datatest.OS
        print("[ POM CONFIGURACION ] - OS: " + os + " | Browser: " + browser + " |")
        print("#################")

        driver = WebDriverFactory.createNewWebDriver(browser, os)

        return driver
