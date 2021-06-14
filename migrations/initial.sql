CREATE TABLE "movimientos" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"fecha"	TEXT NOT NULL,
	"concepto"	TEXT,
	"categoria"	TEXT,
	"esGasto"	INTEGER NOT NULL,
	"cantidad"	REAL
)