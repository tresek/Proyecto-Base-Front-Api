Feature: Login y validación de estilos "Evolutivo Diario"

  @test_diario
  Scenario: Verificar color, fuente y tamaño del texto en Evolutivo diario
    Given el usuario navega a la URL "https://d2cv8h37i5axx3.cloudfront.net/ingreso"
    When ingresa el usuario "solyner28@yopmail.com"
    And ingresa la contraseña "gust2909"
    And hace clic en el botón "Ingresar"
    Then el texto "Evolutivo diario" debe tener el color "rgba(0, 123, 255, 1)"
    And el texto debe tener la fuente "TT Norms"
    And el texto debe tener un tamaño de "14px"