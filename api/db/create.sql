CREATE DATABASE evergreen;
USE evergreen;
CREATE TABLE Canal (
	idCanal INT(11) PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    tipoDestinatario VARCHAR(20) NOT NULL,
    fecha DATETIME
)
INSERT INTO canal(nombre, tipo, tipoDestinatario,fecha) VALUES ('Mensaje individual', 'SMS', 'Simple', '2020/07/15');
INSERT INTO canal(nombre, tipo, tipoDestinatario,fecha) VALUES ('Correo', 'Email', 'Grupo', '2020/06/22');
INSERT INTO canal(nombre, tipo, tipoDestinatario,fecha) VALUES ('Llamada', 'Central Telefonica', 'Simple', '2020/08/21');