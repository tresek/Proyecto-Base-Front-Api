from selenium.webdriver.common.by import By

class HomeLocators:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "(//button)[2]")
    OVERLAY = (By.CLASS_NAME, "overlay")
    TAB_EVOLUTIVO_DIARIO = (By.XPATH,"//a[contains(., 'Evolutivo diario')]")