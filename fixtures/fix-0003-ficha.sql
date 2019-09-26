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

BEGIN;
--
-- Remove field created_at from ficha
--
ALTER TABLE "ficha" DROP COLUMN "created_at" CASCADE;
--
-- Remove field updated_at from ficha
--
ALTER TABLE "ficha" DROP COLUMN "updated_at" CASCADE;
--
-- Add field criado to ficha
--
ALTER TABLE "ficha" ADD COLUMN "criado" timestamp with time zone DEFAULT '2019-09-24T14:06:58.952291+00:00'::timestamptz NULL;
ALTER TABLE "ficha" ALTER COLUMN "criado" DROP DEFAULT;
--
-- Add field modificado to ficha
--
ALTER TABLE "ficha" ADD COLUMN "modificado" timestamp with time zone DEFAULT '2019-09-24T14:06:58.959813+00:00'::timestamptz NULL;
ALTER TABLE "ficha" ALTER COLUMN "modificado" DROP DEFAULT;
COMMIT;

BEGIN;
--
-- Remove field exercicio from ficha
--
SET CONSTRAINTS "ficha_exercicio_id_30620590_fk_exercicio_id" IMMEDIATE; ALTER TABLE "ficha" DROP CONSTRAINT "ficha_exercicio_id_30620590_fk_exercicio_id";
ALTER TABLE "ficha" DROP COLUMN "exercicio_id" CASCADE;
COMMIT;

BEGIN;
--
-- Create model FichaExercicio
--
CREATE TABLE "ficha_exercicio" ("id" serial NOT NULL PRIMARY KEY, "criado" timestamp with time zone NULL, "modificado" timestamp with time zone NULL, "exercicio_id" integer NULL, "ficha_id" integer NULL);
ALTER TABLE "ficha_exercicio" ADD CONSTRAINT "ficha_exercicio_exercicio_id_a21fdde4_fk_exercicio_id" FOREIGN KEY ("exercicio_id") REFERENCES "exercicio" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "ficha_exercicio" ADD CONSTRAINT "ficha_exercicio_ficha_id_c5112f54_fk_ficha_id" FOREIGN KEY ("ficha_id") REFERENCES "ficha" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "ficha_exercicio_exercicio_id_a21fdde4" ON "ficha_exercicio" ("exercicio_id");
CREATE INDEX "ficha_exercicio_ficha_id_c5112f54" ON "ficha_exercicio" ("ficha_id");
COMMIT;