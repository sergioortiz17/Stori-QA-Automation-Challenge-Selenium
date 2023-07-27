from features.Pages_Object.PracticePage import PracticePage



class Application:
    def __init__(self, driver):
        self.PracticePage = PracticePage(driver)

        
