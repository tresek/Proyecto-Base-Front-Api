from behave import when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.steps.utils import esperar
from locators.home_locators import HomeLocators as LOCATORS
import allure


# ---------- EVOLUTIVO DIARIO ----------

def obtener_elemento_diario(context):
    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located(LOCATORS.TAB_EVOLUTIVO_DIARIO)
    )
    return context.driver.find_element(*LOCATORS.TAB_EVOLUTIVO_DIARIO)

@then('el usuario debería ver la pestaña "Evolutivo diario"')
def step_wait_tab_diario(context):
    esperar(context, LOCATORS.OVERLAY, visible=False)

    try:
        print("🔍 Esperando la pestaña 'Evolutivo diario'...")
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(LOCATORS.TAB_EVOLUTIVO_DIARIO)
        )
        print("Pestaña encontrada.")
    except Exception as e:
        print("No se encontró la pestaña:", e)
        raise

@when('hace clic en la pestaña "Evolutivo diario"')
def step_click_tab_diario(context):
    esperar(context, LOCATORS.OVERLAY, visible=False)
    esperar(context, LOCATORS.TAB_EVOLUTIVO_DIARIO).click()

@then('el texto "Evolutivo diario" debe tener el color "{color}"')
def step_color_diario(context, color):
    elem = obtener_elemento_diario(context)
    actual = elem.value_of_css_property("color")
    allure.attach(actual, name="Color", attachment_type=allure.attachment_type.TEXT)
    assert actual == color, f"Esperado: {color}, encontrado: {actual}"

@then('el texto debe tener la fuente "{fuente}"')
def step_valida_fuente(context, fuente):
    elem = obtener_elemento_diario(context)
    actual = elem.value_of_css_property("font-family")
    allure.attach(actual, name="Fuente", attachment_type=allure.attachment_type.TEXT)
    assert fuente in actual, f"Fuente esperada: {fuente}, pero se encontró: {actual}"

@then('el texto debe tener un tamaño de "{tamano}"')
def step_valida_tamano(context, tamano):
    elem = obtener_elemento_diario(context)
    actual = elem.value_of_css_property("font-size")
    allure.attach(actual, name="Tamaño fuente", attachment_type=allure.attachment_type.TEXT)
    assert actual == tamano, f"Tamaño esperado: {tamano}, pero se encontró: {actual}"