/*
 * Salario promedio general y departamento con mayor promedio salarial
 */

USE coordinadora;

SELECT 
    (SELECT AVG(salEmp) FROM Empleado) AS salarioPromedioGeneral,
    d.nombreDpto AS departamento,
    AVG(e.salEmp) AS salarioPromedio
FROM 
    Departamento d
JOIN 
    Empleado e ON d.codDepto = e.codDepto
GROUP BY 
    d.nombreDpto
ORDER BY 
    salarioPromedio DESC
LIMIT 1;
