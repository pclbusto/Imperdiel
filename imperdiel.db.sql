BEGIN TRANSACTION;
CREATE TABLE "Rubros" (
	`NombreRubro`	TEXT UNIQUE,
	`IdRubro`	INTEGER UNIQUE,
	PRIMARY KEY(`IdRubro`)
);
CREATE TABLE "Productos" (
	`NombreProducto`	TEXT,
	`IdProducto`	INTEGER UNIQUE,
	`IdMarca`	INTEGER,
	`IdRubro`	INTEGER,
	PRIMARY KEY(`IdProducto`)
);
CREATE TABLE "Marcas" (
	`NombreMarca`	TEXT,
	`IdMarca`	INTEGER UNIQUE,
	PRIMARY KEY(`NombreMarca`,`IdMarca`)
);
CREATE TABLE "Importaciones" (
	`marca`	TEXT,
	`productoNombre`	TEXT,
	`codigo`	INTEGER,
	`codigoOrigen`	TEXT,
	`precioSinIva`	NUMERIC,
	`rubro`	INTEGER
);
COMMIT;
