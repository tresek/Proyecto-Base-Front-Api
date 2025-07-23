
Feature: Validación visual en pantalla Home

  @test_diseño
  Scenario: Verificar color, fuente de grilla SCP
    Given el usuario ingresa a la URL "https://dev-scp-programador.copec.cl/home"
    And ingresa a la pantalla de la grilla SCP
    Then el dropdown "Planta de Origen" tiene:
      | propiedad         | valor esperado |
      | color_texto       | #49454F        | 
      | tamaño_fuente     | 16px           | 
      | fuente            | TT Norms       | 
      | banner background | #F4F9FF      | 
    Then el campo "Día" debe tener:
      | propiedad       | valor esperado         |
      | placeholder     | dd/mm/yyyy             | 
      | tamaño_fuente   | 16px                   | 
      | color_texto     | #7C97AB              |  
	    | fuente          | "TT Norms"             |
    Then el mensaje "Seleccione una planta y fecha para iniciar" debe tener
      | propiedad       | valor esperado         |
      | tamaño_fuente   | 16px                   | 
      | color_texto     | #052B57             | 
      | alineacion      | centrado             | 
	    | fuente          | TT Norms             | 
	    | background popup| #F4F9FF            | 
	    |Background Overlay | #001D37          | 
    Then el ícono azul de información debe tener
      | propiedad       | valor esperado         |
      | color           | #1B91EC                |
	    | borde verde     | #E2F9FF                | 
    Then el botón de acción a la derecha debe estar visible y tener color de fondo azul
	    | color_fondo     | #0E69AF     
    

 
    
   