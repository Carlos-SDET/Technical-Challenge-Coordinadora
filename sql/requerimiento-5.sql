/*
 * Directores con mas empleados a cargo
 */
use coordinadora;

select
	e.jefeID as directorID,
	count(e.nDIEmp) as empleados
from
	Empleado e
join 
    Departamento d on
	e.jefeID = d.director
group by 
	e.jefeID
order by 
	empleados desc
limit 3;
