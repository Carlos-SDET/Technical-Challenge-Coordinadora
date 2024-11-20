/*
 * Dpto con la nomina mas alta (salario+comision)
 */

USE coordinadora;

SELECT 
    d.nombreDpto AS departamento, 
    SUM(e.salEmp + e.comisionE) AS nominaTotal
FROM 
    Departamento d
JOIN 
    Empleado e ON d.codDepto = e.codDepto
GROUP BY 
    d.nombreDpto
ORDER BY 
    nominaTotal desc
LIMIT 1;
