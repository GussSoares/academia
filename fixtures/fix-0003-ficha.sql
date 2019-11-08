BEGIN;
--
-- Create model Ficha
--
CREATE TABLE "ficha" ("id" serial NOT NULL PRIMARY KEY, "criado" timestamp with time zone NULL, "modificado" timestamp with time zone NULL, "usuario_id" integer NULL);
--
-- Create model FichaExercicio
--
CREATE TABLE "ficha_exercicio" ("id" serial NOT NULL PRIMARY KEY, "criado" timestamp with time zone NULL, "modificado" timestamp with time zone NULL, "exercicio_id" integer NULL, "ficha_id" integer NULL);
ALTER TABLE "ficha" ADD CONSTRAINT "ficha_usuario_id_31c7f839_fk_usuario_id" FOREIGN KEY ("usuario_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "ficha_usuario_id_31c7f839" ON "ficha" ("usuario_id");
ALTER TABLE "ficha_exercicio" ADD CONSTRAINT "ficha_exercicio_exercicio_id_a21fdde4_fk_exercicio_id" FOREIGN KEY ("exercicio_id") REFERENCES "exercicio" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "ficha_exercicio" ADD CONSTRAINT "ficha_exercicio_ficha_id_c5112f54_fk_ficha_id" FOREIGN KEY ("ficha_id") REFERENCES "ficha" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "ficha_exercicio_exercicio_id_a21fdde4" ON "ficha_exercicio" ("exercicio_id");
CREATE INDEX "ficha_exercicio_ficha_id_c5112f54" ON "ficha_exercicio" ("ficha_id");
COMMIT;

BEGIN;
--
-- Create model Treino
--
CREATE TABLE "treino" ("id" serial NOT NULL PRIMARY KEY, "criado" timestamp with time zone NULL, "modificado" timestamp with time zone NULL, "titulo" varchar(3) NOT NULL);
--
-- Alter field ficha on fichaexercicio
--
SET CONSTRAINTS "ficha_exercicio_ficha_id_c5112f54_fk_ficha_id" IMMEDIATE; ALTER TABLE "ficha_exercicio" DROP CONSTRAINT "ficha_exercicio_ficha_id_c5112f54_fk_ficha_id";
ALTER TABLE "ficha_exercicio" ADD CONSTRAINT "ficha_exercicio_ficha_id_c5112f54_fk_ficha_id" FOREIGN KEY ("ficha_id") REFERENCES "ficha" ("id") DEFERRABLE INITIALLY DEFERRED;
--
-- Create model FichaAtual
--
CREATE TABLE "ficha_atual" ("id" serial NOT NULL PRIMARY KEY, "criado" timestamp with time zone NULL, "modificado" timestamp with time zone NULL, "ficha_id" integer NOT NULL, "usuario_id" integer NOT NULL);
ALTER TABLE "ficha_atual" ADD CONSTRAINT "ficha_atual_ficha_id_8f9a25b8_fk_ficha_id" FOREIGN KEY ("ficha_id") REFERENCES "ficha" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "ficha_atual" ADD CONSTRAINT "ficha_atual_usuario_id_1edf817a_fk_usuario_id" FOREIGN KEY ("usuario_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "ficha_atual_ficha_id_8f9a25b8" ON "ficha_atual" ("ficha_id");
CREATE INDEX "ficha_atual_usuario_id_1edf817a" ON "ficha_atual" ("usuario_id");
COMMIT;

BEGIN;
--
-- Add field treino to fichaexercicio
--
ALTER TABLE "ficha_exercicio" ADD COLUMN "treino_id" integer NULL;
CREATE INDEX "ficha_exercicio_treino_id_31a66ba0" ON "ficha_exercicio" ("treino_id");
ALTER TABLE "ficha_exercicio" ADD CONSTRAINT "ficha_exercicio_treino_id_31a66ba0_fk_treino_id" FOREIGN KEY ("treino_id") REFERENCES "treino" ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;

BEGIN;
--
-- Add field instrutor to ficha
--
ALTER TABLE "ficha" ADD COLUMN "instrutor_id" integer NULL;
--
-- Add field obs to ficha
--
ALTER TABLE "ficha" ADD COLUMN "obs" text NULL;
--
-- Alter field usuario on ficha
--
SET CONSTRAINTS "ficha_usuario_id_31c7f839_fk_usuario_id" IMMEDIATE; ALTER TABLE "ficha" DROP CONSTRAINT "ficha_usuario_id_31c7f839_fk_usuario_id";
ALTER TABLE "ficha" ADD CONSTRAINT "ficha_usuario_id_31c7f839_fk_usuario_id" FOREIGN KEY ("usuario_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "ficha_instrutor_id_cf8cb842" ON "ficha" ("instrutor_id");
ALTER TABLE "ficha" ADD CONSTRAINT "ficha_instrutor_id_cf8cb842_fk_usuario_id" FOREIGN KEY ("instrutor_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;

BEGIN;
--
-- Add field repeticoes to fichaexercicio
--
ALTER TABLE "ficha_exercicio" ADD COLUMN "repeticoes" varchar(2) NULL;
--
-- Add field series to fichaexercicio
--
ALTER TABLE "ficha_exercicio" ADD COLUMN "series" varchar(1) NULL;
COMMIT;
