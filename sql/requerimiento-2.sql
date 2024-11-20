/*
 * Departamentos con mas de 3 empleados ordenados descendentemente 
 * por la cantidad de empleados
 */

USE coordinadora;

SELECT 
    d.nombreDpto AS departamento,
    COUNT(*) AS numEmpleados
FROM 
	Empleado e
JOIN 
	Departamento d ON e.codDepto = d.codDepto
GROUP BY 
	d.nombreDpto
HAVING 
	COUNT(*) > 3
ORDER BY 
	COUNT(*) DESC;
