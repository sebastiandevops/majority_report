-- Write a script that creates the database hbtn_0d_usa and the
-- table states (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS majority_report;
USE majority_report;
CREATE TABLE IF NOT EXISTS data_metropolitan (
    id INT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    departamento VARCHAR(256) NOT NULL,
    municipio VARCHAR(256) NOT NULL,
    dia VARCHAR(256) NOT NULL,
    hora VARCHAR(256) NOT NULL,
    barrio VARCHAR(256) NOT NULL,
    zona VARCHAR(256) NOT NULL,
    clase_de_sitio VARCHAR(256) NOT NULL,
    arma VARCHAR(256) NOT NULL,
    movil_agresor VARCHAR(256) NOT NULL,
    movil_victima VARCHAR(256) NOT NULL,
    edad INT NOT NULL,
    sexo VARCHAR(256) NOT NULL,
    estado_civil VARCHAR(256) NOT NULL,
    pais_nacimiento VARCHAR(256) NOT NULL,
    clase_de_empleado VARCHAR(256) NOT NULL,
    escolaridad VARCHAR(256) NOT NULL,
    catidad INT NOT NULL,
    año INT NOT NULL,
    mes INT NOT NULL,
    semana INT NOT NULL,
    franja_horaria VARCHAR(256) NOT NULL,
    hora_24 INT NOT NULL,
    PRIMARY KEY (id));
