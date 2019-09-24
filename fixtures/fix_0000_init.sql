BEGIN;
--
-- Create model Usuario
--
CREATE TABLE "usuario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "matricula" varchar(7) NOT NULL UNIQUE, "first_name" varchar(30) NULL, "last_name" varchar(30) NULL, "email" varchar(254) NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL);
COMMIT;

BEGIN;
--
-- Create model Exercicio
--
CREATE TABLE "exercicio" ("id" serial NOT NULL PRIMARY KEY, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL, "nome" varchar(30) NOT NULL, "descricao" varchar(255) NULL);
COMMIT;

BEGIN;
--
-- Create model Ficha
--
CREATE TABLE "ficha" ("id" serial NOT NULL PRIMARY KEY, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL, "exercicio_id" integer NULL, "usuario_id" integer NULL);
ALTER TABLE "ficha" ADD CONSTRAINT "ficha_exercicio_id_30620590_fk_exercicio_id" FOREIGN KEY ("exercicio_id") REFERENCES "exercicio" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "ficha" ADD CONSTRAINT "ficha_usuario_id_31c7f839_fk_usuario_id" FOREIGN KEY ("usuario_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "ficha_exercicio_id_30620590" ON "ficha" ("exercicio_id");
CREATE INDEX "ficha_usuario_id_31c7f839" ON "ficha" ("usuario_id");
COMMIT;