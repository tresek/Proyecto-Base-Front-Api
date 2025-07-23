from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def rgba_to_hex(rgba_str):
    """Convierte 'rgba(0, 57, 101, 1)' a '#003965'."""
    import re
    match = re.match(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', rgba_str)
    if match:
        r, g, b = map(int, match.groups())
        return '#{:02X}{:02X}{:02X}'.format(r, g, b)
    return None

@given('el usuario ingresa a la URL "{url}"')
def step_open_url(context, url):
    context.driver.get(url)
    time.sleep(2)

@given('ingresa a la pantalla de la grilla SCP')
def step_ingresa_grilla_scp(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//mat-label[contains(text(), 'Planta de origen')]"))
    )
    print("Grilla SCP visible")

@then('el dropdown "Planta de Origen" tiene')
def step_verificar_dropdown(context):
    for row in context.table:
        propiedad = row['propiedad']
        esperado = row['valor esperado']

        if propiedad == "color_texto":
            element = context.driver.find_element(By.XPATH, "//mat-label[contains(text(), 'Planta de origen')]")
            color_rgba = element.value_of_css_property("color")
            color_hex = rgba_to_hex(color_rgba)
            assert color_hex == esperado.upper(), f"Color esperado: {esperado}, encontrado: {color_hex}"

        elif propiedad == "tamaño_fuente":
            element = context.driver.find_element(By.XPATH, "//mat-label[contains(text(), 'Planta de origen')]")
            font_size = element.value_of_css_property("font-size")
            assert font_size == esperado, f"Tamaño fuente esperado: {esperado}, encontrado: {font_size}"

        elif propiedad == "fuente":
            element = context.driver.find_element(By.XPATH, "//mat-label[contains(text(), 'Planta de origen')]")
            font_family = element.value_of_css_property("font-family")
            assert esperado.lower() in font_family.lower(), f"Fuente esperada: {esperado}, encontrada: {font_family}"

        elif propiedad == "banner background":
            banner = context.driver.find_element(By.CLASS_NAME, "header")
            bg_rgba = banner.value_of_css_property("background-color")
            bg_hex = rgba_to_hex(bg_rgba)
            assert bg_hex == esperado.upper(), f"Background esperado: {esperado}, encontrado: {bg_hex}"

@then('el campo "Día" debe tener')
def step_impl(context):
    dia_input = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='dd/mm/yyyy']"))
    )

    for row in context.table:
        propiedad = row['propiedad'].strip()
        esperado = row['valor esperado'].strip()

        if propiedad == "placeholder":
            valor = dia_input.get_attribute("placeholder")
            assert valor == esperado, f'Placeholder esperado: {esperado}, encontrado: {valor}'

        elif propiedad == "tamaño_fuente":
            font_size = dia_input.value_of_css_property("font-size")
            assert font_size == esperado, f'Tamaño fuente esperado: {esperado}, encontrado: {font_size}'

        elif propiedad == "color_texto":
            color = dia_input.value_of_css_property("color")
            hex_color = rgba_to_hex(color)
            assert hex_color.lower() == esperado.lower(), f'Color texto esperado: {esperado}, encontrado: {hex_color}'

        elif propiedad == "fuente":
            fuente = dia_input.value_of_css_property("font-family")
            assert esperado.lower().replace('"', '') in fuente.lower(), f'Fuente esperada: {esperado}, encontrada: {fuente}'

def rgba_to_hex(rgba):
    import re
    match = re.match(r'rgba?\((\d+), (\d+), (\d+)(?:, [\d\.]+)?\)', rgba)
    if match:
        r, g, b = map(int, match.groups()[:3])
        return '#{:02X}{:02X}{:02X}'.format(r, g, b)
    return rgba

@then('el mensaje "Seleccione una planta y fecha para iniciar" debe tener')
def step_validar_mensaje_bienvenida(context):
    mensaje_element = context.driver.find_element(By.XPATH, "//*[contains(text(),'Seleccione una planta y fecha para iniciar')]")

    # Verificación de estilo
    styles = context.driver.execute_script(
        "var elem = arguments[0];"
        "var styles = window.getComputedStyle(elem);"
        "return {"
        "  fontSize: styles.fontSize,"
        "  color: styles.color,"
        "  textAlign: styles.textAlign,"
        "  fontFamily: styles.fontFamily,"
        "  backgroundColor: styles.backgroundColor"
        "};", 
        mensaje_element
    )

    for row in context.table:
        propiedad = row['propiedad']
        esperado = row['valor esperado']

        if propiedad == "tamaño_fuente":
            assert styles['fontSize'] == esperado, f"Tamaño fuente esperado: {esperado}, encontrado: {styles['fontSize']}"
        elif propiedad == "color_texto":
            actual_hex = rgba_to_hex(styles['color'])
            assert actual_hex.lower() == esperado.lower(), f"Color esperado: {esperado}, encontrado: {actual_hex}"
        elif propiedad == "alineacion":
            assert styles['textAlign'] == "center", f"Alineación esperada: center, encontrada: {styles['textAlign']}"
        elif propiedad == "fuente":
            assert esperado.strip('"').lower() in styles['fontFamily'].lower(), f"Fuente esperada: {esperado}, encontrada: {styles['fontFamily']}"
        elif propiedad == "background popup":
            actual_bg = rgba_to_hex(styles['backgroundColor'])
            assert actual_bg.lower() == esperado.lower(), f"Background popup esperado: {esperado}, encontrado: {actual_bg}"
        elif propiedad == "Background Overlay":
            # Se asume que el overlay tiene una clase conocida o ID
            overlay = context.driver.find_element(By.CSS_SELECTOR, ".overlay-clase")  # Ajusta este selector
            overlay_color = context.driver.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;", overlay)
            overlay_hex = rgba_to_hex(overlay_color)
            assert overlay_hex.lower() == esperado.lower(), f"Overlay esperado: {esperado}, encontrado: {overlay_hex}"

@then('el ícono azul de información debe tener')
def step_validar_icono_info(context):
    icono = context.driver.find_element(By.CLASS_NAME, "info-icon")  # Ajusta el selector
    styles = context.driver.execute_script("return window.getComputedStyle(arguments[0]);", icono)

    for row in context.table:
        propiedad = row['propiedad']
        esperado = row['valor esperado']

        if propiedad == "color":
            actual = rgba_to_hex(styles.color)
            assert actual.lower() == esperado.lower(), f"Color del ícono esperado: {esperado}, encontrado: {actual}"
        elif propiedad == "borde verde":
            actual = rgba_to_hex(styles.borderColor)
            assert actual.lower() == esperado.lower(), f"Color del borde esperado: {esperado}, encontrado: {actual}"

@then('el botón de acción a la derecha debe estar visible y tener color de fondo azul')
def step_validar_boton_accion(context):
    boton = context.driver.find_element(By.ID, "accion-boton")  # Ajusta el selector
    assert boton.is_displayed(), "El botón de acción no está visible"
    styles = context.driver.execute_script("return window.getComputedStyle(arguments[0]);", boton)

    for row in context.table:
        propiedad = row['propiedad']
        esperado = row['valor esperado']

        if propiedad == "color_fondo":
            actual = rgba_to_hex(styles.backgroundColor)
            assert actual.lower() == esperado.lower(), f"Color de fondo esperado: {esperado}, encontrado: {actual}"
