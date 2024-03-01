from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnterTheSite:
    def enter_the_site(self, webdriver, url):
        webdriver.get(url)
        print(f"Visited the site using the URL {url}")
        webdriver.maximize_window()
        

class ReturnPath:
    def get_path_wait(self, webdriver, path):
        return WebDriverWait(webdriver, 20).until(EC.element_to_be_clickable((By.XPATH, path)))
    
    def get_path(self, webdriver, path):
        return webdriver.find_element(By.XPATH, path)

