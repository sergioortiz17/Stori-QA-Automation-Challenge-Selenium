from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.BaseActions import BaseActions

t = 0.1


##################### Locators ######################################
inputCountry = (By.XPATH, "//*[@id='autocomplete']")
btonCountry = (By.XPATH,"//*[@id='ui-id-7']")
inputDropdownOptionN = (By.XPATH,"//*[@id='dropdown-class-example']")
downArrow = "\ue015"
btonNewWindow = (By.XPATH,"//*[@id='openwindow']")
finalPageAcademy = (By.XPATH,"//*[@id='footer-part']/div[1]/div/div/div[2]/div/ul/li[5]/a")
btonNewTab = (By.XPATH,"//*[@id='opentab']")
textFirstTitle = (By.XPATH,"/html/body/h1")
inputAlert = (By.XPATH,"//*[@id='name']")
btonAlert = (By.XPATH,"//*[@id='alertbtn']")
btonConfirmAlert = (By.XPATH,"//*[@id='confirmbtn']")
tableCourses = (By.XPATH,"//*[@id='product']")


texto_esperado_Alert = "Hello Stori Card, share this practice page and share your knowledge"
texto_esperado_Alert_Confirm = "Hello Stori Card, Are you sure you want to confirm?"

path_css_siblings_elements_price = "#product > tbody > tr > td:nth-child(3)"
path_css_siblings_elements_position = "#product > tbody > tr > td:nth-child(2)"

class PracticePage(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    #Punto 2
    def insertCountry(self , country):
        BaseActions.send_Text_Input(self, inputCountry[0], inputCountry[1], country[:2], t) 
        BaseActions.clickAction(self, btonCountry[0],btonCountry[1])

    #Punto 3
    def selectOptionsDropDown(self):
        
        BaseActions.key_Up_Key_Down(self, inputDropdownOptionN[0],inputDropdownOptionN[1], downArrow)
        BaseActions.Tiempo(2)
        BaseActions.key_Up_Key_Down(self, inputDropdownOptionN[0],inputDropdownOptionN[1],downArrow)
    
    #Punto 4
    def verifyMoneyBackGuaranteeinQaclickacademy(self):
        #Click en Boton que abre nueva ventana
        BaseActions.clickAction(self, btonNewWindow[0],btonNewWindow[1])
        #switch Window driver 
        BaseActions.switchWindow(self, 1)
        BaseActions.verifyRegraan(self)
            #Scroll despacio para busqueda (no es necesario en realidad)
        BaseActions.scrollToElement_visibility(self,finalPageAcademy[0],finalPageAcademy[1])
            #Verifica de nuevo texto de rembolso en modal o en la pagina que se ve 
        BaseActions.verifyRegraan(self)
            #cierra esa ventana 
        self.driver.close()
        BaseActions.switchWindow(self, 0)

    #Punto 5
    def openTabAndScreenshot(self):
        #Click en Boton que OPEN TAB que abre la pestaña
        BaseActions.clickAction(self, btonNewTab[0],btonNewTab[1])
        #switch Window driver 
        BaseActions.switchTaB(self, 1)
        #scroll y foto del elemento        
        #aca no esta el elemento pero igual buscarlo?
        #volver a la pestaña
        BaseActions.switchTaB(self, 0)
        BaseActions.switchToiFrame(self)
        BaseActions.screenshot(self,"Boton-ViewAll")
        BaseActions.Tiempo(10)
   
    #Punto 6
    def verify_name_in_Alert_expected(self, name):
        #scroll hasta el input del Alert
        BaseActions.scrollToElement_visibility(self,inputAlert[0],inputAlert[1])
        #Envia texto al alert
        BaseActions.send_Text_Input(self,inputAlert[0],inputAlert[1],name,t)
        #Click en Boton Alert
        BaseActions.clickAction(self, btonAlert[0],btonAlert[1])
        #Verificar que el texto en el alert este bien
        BaseActions.verifyAlert(self, texto_esperado_Alert)
        #Enviar texto al input de alert de nuevo para esta vez es click a confirm
        BaseActions.send_Text_Input(self,inputAlert[0],inputAlert[1],name,t)
        #Click en Boton Confirm
        BaseActions.clickAction(self, btonConfirmAlert[0],btonConfirmAlert[1])
        #solo le da ok al boton aceptar del alert 
        BaseActions.verifyAlert(self,texto_esperado_Alert_Confirm)

    #Punto 7
    def count_and_get_courses_for_this_price(self, price): 
        #scroll buscando table of courses
        BaseActions.scrollToElement_visibility(self,tableCourses[0], tableCourses[1])  
        BaseActions.if_match_get_previous_siblings(self, price, path_css_siblings_elements_price, "Names of courses that cost")
        BaseActions.imprimir_archivo_en_consola(f"elementos_con_{price}.txt")
        
    #Punto 8
    def count_and_get_people_whit_this_position(self, position): 
        BaseActions.if_match_get_previous_siblings(self, position, path_css_siblings_elements_position, "People with this profession")
        #BaseActions.imprimir_archivo_en_consola(f"{file_name}")
        BaseActions.imprimir_archivo_en_consola(f"elementos_con_{position}.txt")

    #Punto 9
    def getTextInsideiFrame(self):     
        BaseActions.switchToiFrameText(self)
        BaseActions.Tiempo(2)
        BaseActions.imprimir_archivo_en_consola("texto_iframe.txt")
        
