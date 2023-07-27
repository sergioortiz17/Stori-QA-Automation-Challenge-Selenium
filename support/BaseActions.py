import time

from datetime import datetime
from urllib.parse import urlparse
import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        global act
        act = ActionChains(driver)

    @staticmethod
    def Tiempo(tie):
        time.sleep(tie)

##################### CONFIGURATION OF BROWSER ######################################

    def visit_web(self, URL: str):
        self.driver.get(URL)

######################### ACTION CHAINS #######################################################################
    def clickAction(self, by_tipo: By, selector: str):

        try:
            val = self.driver.find_element(by_tipo, selector)
            act.click(val).perform()
            time.sleep(1)
        except NoSuchElementException as ex:
            assert False, f"No se pudo realizar la accion de click actions\n" \
                          f"debido a que no se encontró el elemento con el selector '{selector}' de tipo:" \
                          f" '{by_tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se pudo realizar la accion de click actions\n" \
                          f"debido a que no se puede interactuar con el elemento '{selector}' de tipo: " \
                          f"'{by_tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se pudo realizar la accion de click actions\n" \
                          f"debido a que el Tiempo de espera fue excedido para encontrar el elemento '{selector}' " \
                          f"de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            assert False, f"Error Desconocido: {ex.args}"

    def key_Up_Key_Down(self, by_tipo: By, selector: str, tecla: Keys):

        try:
            val = self.driver.find_element(by_tipo, selector)
            act.click(val).perform()
            act.key_down(tecla).key_up(tecla).perform()
            val.send_keys(Keys.ENTER)

            time.sleep(1)
        except NoSuchElementException as ex:
            assert False, f"No se pudo hacer la accion de hacer click en un elemento y pulsar una tacla del keyboard\n" \
                          f"debido a que no se encontró el elemento con el selector '{selector}' de tipo: '{by_tipo}'\n" \
                          f" Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se pudo hacer la accion de hacer click en un elemento y pulsar una tacla del keyboard\n" \
                          f"debido a que no se puede interactuar con el elemento '{selector}' de tipo: '{by_tipo}'\n " \
                          f"Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se pudo hacer la accion de hacer click en un elemento y pulsar una tacla del keyboard\n" \
                          f"debido a que el Tiempo de espera fue excedido para encontrar el elemento '{selector}'" \
                          f" de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            assert False, f"Error Desconocido: {ex.args}"

######################### SEARCH AND SEND, INPUTS; ELEMENTS; TEXT AND SELECTORS ################################

    def send_Text_Input(self, by_tipo: By, selector: str, texto: str, tiempo: float):

        try:
            ele = None
            ele = self.driver.find_element(by_tipo, selector)
            # Limpiar campo y enviar texto
            ele.clear()
            ele.send_keys(texto)
            BaseActions.Tiempo(tiempo)
            print(f"Cargado el texto {texto} correctamente")
        except NoSuchElementException as ex:
            assert False, f"No se pudo enviar el texto en el input debido a que\n" \
                          f"no encontró el elemento con el selector '{selector}'  de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se pudo enviar el texto en el input debido a que\n" \
                          f"no se puede interactuar con el elemento '{selector}' de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se pudo enviar el texto en el input debido a que\n" \
                          f"el Tiempo de espera fue excedido para encontrar el elemento '{selector}' de tipo: '{by_tipo}" \
                          f"'\n Error Log: {ex.msg}"
        except Exception as ex:
            assert False, f"Error Desconocido al intentar evniar texto en el input con en el elemento: {selector} de tipo {by_tipo}" \
                          f"\n Error Log : {ex.args}"

    def scrollToElement_visibility(self, tipo, elemento):
        try:
            val = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, elemento)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            print("\n Desplazando al elemento -> {} ".format(elemento))
        except NoSuchElementException as ex:
            assert False, f"No se movio debido a que no se encontró el elemento " \
                          f"con el selector '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se movio debido a que no se puede interactuar con " \
                          f"el elemento '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se movio debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

######################### SWITCHS ################################

    def switchTaB(self, ntab : int):
        try:
            pestañas = self.driver.window_handles

            # Cambiar a la segunda pestaña (el índice 1 corresponde a la segunda pestaña, ya que es una lista basada en 0)
            self.driver.switch_to.window(pestañas[ntab])

            # Realizar acciones en la segunda pestaña (por ejemplo, obtener su URL)
            url_segunda_pestaña = self.driver.current_url
            print("tab URL actual:", url_segunda_pestaña)
    
        except NoSuchElementException as ex:
            assert False, f"No se pudo realizar la accion de click actions\n" \
                          f"debido a que no se encontró el elemento con el selector '{selector}' de tipo:" \
                          f" '{by_tipo}'\n Error Log: {ex.msg}"        
  
    def switchToiFrame(self):
        try:

            iframe = self.driver.find_element(By.ID, "courses-iframe")
            self.driver.switch_to.frame(iframe)



            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            BaseActions.scrollToElement_visibility(self,By.XPATH,"/html/body/div/div[2]/section[4]/div[2]/a")
            BaseActions.screenshot(self, "prueba")
            self.driver.switch_to.default_content()
            
            
        except NoSuchElementException as ex:
            assert False, f"No se pudo realizar la accion de click actions\n" \
                          f"debido a que no se encontró el elemento con el selector '{selector}' de tipo:" \
                          f" '{by_tipo}'\n Error Log: {ex.msg}"        

    def switchToiFrameText(self):
        try:

            iframe = self.driver.find_element(By.ID, "courses-iframe")
            self.driver.switch_to.frame(iframe)



            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            texto_buscado = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div/div/div[2]/ul/li[2]")
            
            with open("texto_iframe.txt", "w") as archivo:
                #archivo.write(str(textos_hermanos_anteriores)+ "\n")
                
                archivo.write("EL parrafo es:\n")
                archivo.write(str(texto_buscado.text)+ "\n")
         
            self.driver.switch_to.default_content()
            
            
        except NoSuchElementException as ex:
            assert False, f"No se pudo realizar la accion de click actions\n" \
                          f"debido a que no se encontró el elemento con el selector '{selector}' de tipo:" \
                          f" '{by_tipo}'\n Error Log: {ex.msg}"        

        #self.driver.quit()
        
    def switchWindow(self, nWindow : int):
        try:
            #define ventanas abiertas
            ventanas_abiertas = self.driver.window_handles
            #switch a la recien que abrio
            self.driver.switch_to.window(ventanas_abiertas[nWindow])
            #acciones sobre esta ventana
            url_nueva_ventana = self.driver.current_url
            print("URL de la nueva ventana:", url_nueva_ventana)
         
        except NoSuchElementException as ex:
            assert False, f"No se pudo realizar la accion de click actions\n" \
                          f"debido a que no se encontró el elemento con el selector '{selector}' de tipo:" \
                          f" '{by_tipo}'\n Error Log: {ex.msg}"        

######################### ALERTS ################################

    def verifyAlert(self, texto_esperado):
        
        
        try:
            # Esperar a que aparezca el alert
            alert = Alert(self.driver)
            alert_text = alert.text

            # Comparar el texto del alert con el valor esperado
            
            assert texto_esperado in alert_text, f"El texto del alert no coincide con el esperado. Esperado: '{texto_esperado}'. Actual: '{alert_text}'"
            
            if texto_esperado in alert_text:
                print("¡El texto del alert coincide correctamente con el esperado!")
            else:
                print("El texto del alert NO coincide con el esperado. Esperado:", texto_esperado)
            alert.accept()
            
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir
            print("Error:", e)
            
######################### CHILDS TO PARENTS ################################

    def if_match_get_previous_siblings(self, toCompare, css_siblings_elements, semantic_siblings):
        
        try:
            #conjunto de elementos con este css_selector
            siblings_elements = self.driver.find_elements(By.CSS_SELECTOR, css_siblings_elements)

            # Inicializar una variable 
            equal_elements_text = 0
            all_text_siblings = []
            # Recorrer los elementos y verificar si su texto es igual a "25"
            for elemento in siblings_elements:
                if elemento.text == toCompare:
                    #aumenta el contador en uno
                    equal_elements_text += 1
                    #busca el hermano anterior OJO funciona para price y position porque course_name y name son sus anteriores sino hay que cambiar este ./preceding-sibling::td[1]
                    get_sibling = elemento.find_element(By.XPATH, "./preceding-sibling::td[1]")
                    # guarda el texto del hermano en un array
                    all_text_siblings.append(get_sibling.text)

            # Imprimir la cantidad de elementos iguales
            print(f"Elementos iguales a {toCompare}: {equal_elements_text}")
            #print("Cantidad de elementos con texto igual a {price}:", cantidad_elementos_igual_25)
            nombre_archivo = "elementos_con.txt"
            nombre_completo_archivo = f"{nombre_archivo.replace('.txt', '')}_{toCompare}.txt"

            with open(nombre_completo_archivo, "w") as archivo:
                archivo.write(f"{semantic_siblings}:\n")
                for texto in all_text_siblings:
                 archivo.write(texto + "\n")
                archivo.write("")
                archivo.write("")

        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir
            print("Error:", e)          

    def imprimir_archivo_en_consola(nombre_archivo):
        try:
            # Lee el contenido del archivo
            with open(nombre_archivo, "r") as file:
                contenido = file.read()

            # Imprime el contenido en la consola
            print(contenido)

        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no fue encontrado.")

    def verifyRegraan(self):


        try:
            result = False
            time.sleep(1)
            elements = None
           # BaseActions.elementIsVisibleByText()
            elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                 "div.container")  # Crear listado de elementos con la clase Checkbox
            for ele in elements:  # Se itera elemento por elemento hasta encontrar el que coincide con el texto del capchat
                if ele.text == "30 DAY":
                    print(f"Se encontro Msj de Rembolso")
                    elements[elements.index(ele)].click()  # Sí detecta el elemento esperado hara click sobre el
                    result = True
                    break
            if result is False:
                print("No se encontro Msj de Rembolso")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se" \
                          f"buscaba algun Msj de Rembolso en pantalla\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró ningun Msj de Rembolso en pantalla\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No hay Msj de Rembolso en pantalla para interactuar\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido al buscar algun Msj de Rembolso en pantalla: {ex}"

#################################### ALLURE SCREENSHOT ##############################################

    def screenshot(self, nombre: str):

        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)

    def subirArchivo(self, by_tipo: By, selector: str, ruta: str):
        try:
            val = self.driver.find_element(by_tipo, selector)
            val.send_keys(ruta)
            print("\n Elemento Cargado -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"No se pudo subir el archivo debido\n" \
                          f"a que no se encontró el elemento con el selector '{selector}" \
                          f" de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se pudo subir el archivo debido\n" \
                          f"a que no se puede interactuar con el elemento '{selector}'" \
                          f" de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se pudo subir el archivo debido\n" \
                          f"a que el Tiempo de espera fue excedido para encontrar el elemento '{selector}'" \
                          f" de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            assert False, f"Error Desconocido: {ex}"


