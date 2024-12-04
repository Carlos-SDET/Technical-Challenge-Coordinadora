/*
 * Salario promedio general y departamento con mayor promedio salarial
 */

use coordinadora;

select
	(
	select
		AVG(salEmp)
	from
		Empleado) as salarioPromedioGeneral,
	d.nombreDpto as departamento,
	AVG(e.salEmp) as salarioPromedio
from
	Departamento d
join 
    Empleado e on
	d.codDepto = e.codDepto
group by
	d.nombreDpto
order by
	salarioPromedio desc
limit 1;