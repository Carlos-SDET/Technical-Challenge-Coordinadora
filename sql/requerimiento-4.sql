/*
 * Dpto con la nomina mas alta (salario+comision)
 */

use coordinadora;

select
	d.nombreDpto as departamento,
	SUM(e.salEmp + e.comisionE) as nominaTotal
from
	Departamento d
join 
    Empleado e on
	d.codDepto = e.codDepto
group by
	d.nombreDpto
order by 
	nominaTotal desc
limit 1;
