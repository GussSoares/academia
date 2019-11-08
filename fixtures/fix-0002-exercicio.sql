BEGIN;
--
-- Create model Exercicio
--
CREATE TABLE "exercicio" ("id" serial NOT NULL PRIMARY KEY, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL, "nome" varchar(30) NOT NULL, "descricao" varchar(255) NULL);
COMMIT;

BEGIN;
--
-- Remove field created_at from exercicio
--
ALTER TABLE "exercicio" DROP COLUMN "created_at" CASCADE;
--
-- Remove field updated_at from exercicio
--
ALTER TABLE "exercicio" DROP COLUMN "updated_at" CASCADE;
--
-- Add field criado to exercicio
--
ALTER TABLE "exercicio" ADD COLUMN "criado" timestamp with time zone DEFAULT '2019-09-24T14:06:24.040490+00:00'::timestamptz NULL;
ALTER TABLE "exercicio" ALTER COLUMN "criado" DROP DEFAULT;
--
-- Add field modificado to exercicio
--
ALTER TABLE "exercicio" ADD COLUMN "modificado" timestamp with time zone DEFAULT '2019-09-24T14:06:24.042061+00:00'::timestamptz NULL;
ALTER TABLE "exercicio" ALTER COLUMN "modificado" DROP DEFAULT;
COMMIT;

BEGIN;
--
-- Alter field descricao on exercicio
--
ALTER TABLE "exercicio" ALTER COLUMN "descricao" TYPE text USING "descricao"::text;
--
-- Alter field nome on exercicio
--
ALTER TABLE "exercicio" ADD CONSTRAINT "exercicio_nome_10de4315_uniq" UNIQUE ("nome");
CREATE INDEX "exercicio_nome_10de4315_like" ON "exercicio" ("nome" varchar_pattern_ops);
COMMIT;