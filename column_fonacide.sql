UPDATE mecmapi_institucion
SET fonacide = 't' FROM (SELECT DISTINCT
                           cod_establecimiento
                         FROM mecmapi_espacios
                           JOIN mecmapi_institucion ON (codigo_establecimiento = cod_establecimiento)) subquery
WHERE subquery.cod_establecimiento = mecmapi_institucion.codigo_establecimiento;

UPDATE mecmapi_institucion
SET fonacide = 't' FROM (SELECT DISTINCT
                           cod_establecimiento
                         FROM mecmapi_mobiliarios
                           JOIN mecmapi_institucion ON (codigo_establecimiento = cod_establecimiento)) subquery
WHERE subquery.cod_establecimiento = mecmapi_institucion.codigo_establecimiento;

UPDATE mecmapi_institucion
SET fonacide = 't' FROM (SELECT DISTINCT
                           cod_establecimiento
                         FROM mecmapi_sanitarios
                           JOIN mecmapi_institucion ON (codigo_establecimiento = cod_establecimiento)) subquery
WHERE subquery.cod_establecimiento = mecmapi_institucion.codigo_establecimiento;