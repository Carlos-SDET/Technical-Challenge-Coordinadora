Feature: Solicitud de recogidas
	Scenario: Creación exitosa de solicitud de recogida
    	Given tengo los datos válidos para una solicitud
    	When envío la solicitud al sistema
    	Then debería recibir un código 200
    	And debería recibir mensaje "Solicitud recogida programada exitosamente"

  	Scenario: Validación de solicitud duplicada
    	Given existe una solicitud previa
    	When envío la misma solicitud nuevamente
    	Then debería recibir mensaje "Ya existe una recogida programada para hoy"

	Scenario: Validación de fecha fuera de rango
    	Given tengo una solicitud con fecha futura
    	When envío la solicitud
    	Then debería recibir mensaje "no debe ser mayor a la fecha"