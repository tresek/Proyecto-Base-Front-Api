Feature: Test API: Consulta de información de una mascota por su ID

  @api
  Scenario: Consultar una mascota existente por ID
    Given que la API del Petstore está disponible
    When consulto la mascota con ID 1
    Then la respuesta debe ser exitosa con código 200