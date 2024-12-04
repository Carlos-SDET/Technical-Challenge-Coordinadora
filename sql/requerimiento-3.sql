-- 3. Empleados sin departamento valido

use coordinadora;

select 
	nomEmp as nombre, 
	codDepto as codigo_departamento
from 
	Empleado
where 
	codDepto not in (
	select
		codDepto
	from
		Departamento);