import requests
from behave import given, when, then

@given("que la API del Petstore está disponible")
def step_impl(context):
    context.base_url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"

@when("consulto la mascota con ID 1")
def step_impl(context):
    response = requests.get(f"{context.base_url}/10")
    context.response = response

@then("la respuesta debe ser exitosa con código 200")
def step_impl(context):
    assert context.response.status_code == 200, f"Código recibido: {context.response.status_code}"