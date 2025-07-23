from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # si quieres modo invisible
    context.driver = webdriver.Chrome(options=options)

def after_all(context):
    context.driver.quit()
