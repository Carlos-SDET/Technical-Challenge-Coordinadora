/*
 * Departamentos con mas de 3 empleados ordenados descendentemente 
 * por la cantidad de empleados
 */

use coordinadora;

select
	d.nombreDpto as departamento,
	COUNT(*) as numEmpleados
from 
	Empleado e
join 
	Departamento d on
	e.codDepto = d.codDepto
group by 
	d.nombreDpto
having 
	COUNT(*) > 3
order by 
	COUNT(*) desc;
