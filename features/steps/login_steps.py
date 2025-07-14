from behave import given, when, then
from selenium import webdriver
from pages.home_locators import HomeLocators as LOCATORS
from features.steps.utils import esperar
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

@given('el usuario navega a la URL "{url}"')
def step_open_url(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    context.driver.maximize_window()

@when('ingresa el usuario "{usuario}"')
def step_ingresa_usuario(context, usuario):
    esperar(context, LOCATORS.EMAIL_INPUT).send_keys(usuario)

@when('ingresa la contraseña "{password}"')
def step_ingresa_password(context, password):
    esperar(context, LOCATORS.PASSWORD_INPUT).send_keys(password)

@when('hace clic en el botón "Ingresar"')
def step_click_login(context):
    esperar(context, LOCATORS.LOGIN_BUTTON).click()