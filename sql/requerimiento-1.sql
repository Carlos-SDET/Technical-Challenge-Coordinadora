/*
Calcular el valor total del próximo pago para empleados del departamento 3000
Incluir un reconocimiento adicional de $500,000
El pago regular incluye salario y comisión
Ordenar la información alfabéticamente por empleado
*/


USE coordinadora;

SELECT 
    nomEmp AS empleado,
    salEmp as salarioBase,
    comisionE  as comision,
    500000 as bonoUnico,
    (salEmp + comisionE + 500000) AS pagoTotal
FROM 
    Empleado
WHERE 
    codDepto = 3000
ORDER BY 
    nomEmp ASC;
