Ejecutar todos los escenarios
* behave

Ejecutar solo una feature específica
* behave features/estilos_evolutivo.feature

 Ejecutar solo un escenario específico (por nombre)
 * behave -n "Verificar color, fuente y tamaño del texto en Evolutivo diario"

Ejecutar usando un tag
* @regresion
Scenario: Validar algo importante

También puedes usar combinaciones:
* behave -t @regresion -t ~@skip

Ejecutar y generar reportes Allure
* behave -f allure_behave.formatter:AllureFormatter -o reportes features/
* allure serve reportes

Ejecutar y ver solo fallos
* behave --no-capture --no-skipped --stop

Ejecutar con logs visibles (útil para debug)
* behave --no-capture

#### Ehecucion de API 
* pytest api/tests/ --alluredir=reports/allure-results
* allure serve reports/