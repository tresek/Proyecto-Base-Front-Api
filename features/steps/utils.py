from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_locators import HomeLocators as LOCATORS
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

def esperar(context, locator, visible=True, timeout=15):
    wait = WebDriverWait(context.driver, timeout)
    if visible:
        return wait.until(EC.visibility_of_element_located(locator))
    else:
        return wait.until(EC.invisibility_of_element_located(locator))

def obtener_estilo(context, tipo):
    if tipo == "diario":
        return context.driver.find_element(*LOCATORS.TAB_EVOLUTIVO_DIARIO_ACTIVO)
    elif tipo == "mensual":
        return context.driver.find_element(*LOCATORS.TAB_EVOLUTIVO_MENSUAL_ACTIVO)