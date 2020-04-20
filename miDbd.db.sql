CREATE TABLE IF NOT EXISTS "Usuarios" (
	"idusuario"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"email"	text NOT NULL UNIQUE,
	"contraseña_encriptada"	text NOT NULL
);
CREATE TABLE IF NOT EXISTS "Contactos" (
	"id"	INTEGER NOT NULL,
	"id_contacto"	INTEGER NOT NULL,
	"perfil"	TEXT,
	PRIMARY KEY("id","id_contacto")
);
CREATE TABLE IF NOT EXISTS "Datos_activos" (
	"id"	INTEGER NOT NULL UNIQUE,
	"fecha_nacimiento"	TEXT,
	"celular"	TEXT,
	"telefono"	TEXT,
	"pais"	TEXT,
	"ciudad"	TEXT,
	"direccion"	TEXT,
	"profesion"	TEXT,
	"puesto"	TEXT,
	"empresa"	TEXT,
	"entidad_financiera"	TEXT,
	"cuenta"	TEXT,
	"red_social"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Perfiles_integrales" (
	"id"	INTEGER NOT NULL UNIQUE,
	"fecha_nacimiento"	TEXT,
	"pais"	TEXT,
	"ciudad"	TEXT,
	"direccion"	TEXT,
	"entidad_financiera"	TEXT,
	"cuenta"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Perfiles_basicos" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT,
	"apellido"	TEXT,
	"email"	TEXT NOT NULL UNIQUE,
	"celular"	TEXT,
	"telefono"	TEXT,
	"profesion"	TEXT,
	"empresa"	TEXT,
	"puesto"	TEXT,
	"red_social"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Perfiles" (
	"id"	INTEGER NOT NULL UNIQUE,
	"basico"	TEXT NOT NULL UNIQUE,
	"integral"	TEXT NOT NULL UNIQUE,
	"financiero"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Contraseñas" (
	"id"	INTEGER NOT NULL UNIQUE,
	"contraseña encriptada"	TEXT NOT NULL,
	"contraseña"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
COMMIT;
