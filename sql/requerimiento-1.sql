/*
Calcular el valor total del próximo pago para empleados del departamento 3000
Incluir un reconocimiento adicional de $500,000
El pago regular incluye salario y comisión
Ordenar la información alfabéticamente por empleado
*/

use coordinadora;

select
	e.nomEmp as empleado,
	e.salEmp as salarioBase,
	e.comisionE as comision,
	500000 as bonoUnico,
	(e.salEmp + e.comisionE + 500000) as pagoTotal
from
	Empleado e
where
	e.codDepto = 3000
order by
	e.nomEmp asc;
