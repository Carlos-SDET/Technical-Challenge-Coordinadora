/*
 * Directores con mas empleados a cargo
 */
USE coordinadora;

SELECT 
    e.jefeID AS directorID,
    COUNT(e.nDIEmp) AS empleados
FROM 
    Empleado e
JOIN 
    Departamento d ON e.jefeID = d.director
WHERE 
    e.jefeID IS NOT NULL
GROUP BY 
    e.jefeID
ORDER BY 
    empleados DESC
LIMIT 3;
