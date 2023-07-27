import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from configuration.config import Datatest
from support.CreateDriver import CreateDriver
from web.applications import Application


def before_scenario(context, scenario):
    # Configuración del driver de Selenium
    context.driver = CreateDriver.set_up_config()  # Obteniendo driver con la configuracion de WebdriverFactory
    context.driver.get(Datatest.URL_WEB)
    context.driver.implicitly_wait(Datatest.IMPLICIT_WAIT)
    context.application = Application(context.driver)


def after_scenario(context, scenario):
    # Cierre del driver de Selenium
    if scenario.status == "failed":
        scenario_name = scenario.name
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        screenshot_name = f"{scenario_name}_{current_time}.png"
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)
    context.driver.quit()
