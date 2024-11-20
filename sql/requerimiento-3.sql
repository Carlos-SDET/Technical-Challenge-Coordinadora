-- 3. Empleados sin departamento valido

USE coordinadora;

SELECT 
	nomEmp as nombre, 
	codDepto as departamento
FROM 
	Empleado 
WHERE 
	codDepto NOT IN (SELECT codDepto FROM Departamento);