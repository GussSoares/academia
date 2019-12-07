BEGIN;
--
-- Create model Token
--
CREATE TABLE "api_token" ("token" varchar(40) NOT NULL PRIMARY KEY, "criado" timestamp with time zone NOT NULL, "aplicacao" smallint NOT NULL, "usuario_id" integer NULL);
ALTER TABLE "api_token" ADD CONSTRAINT "api_token_usuario_id_e41633f2_fk_usuario_id" FOREIGN KEY ("usuario_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "api_token_token_1c16448b_like" ON "api_token" ("token" varchar_pattern_ops);
CREATE INDEX "api_token_usuario_id_e41633f2" ON "api_token" ("usuario_id");
COMMIT;

BEGIN;
--
-- Remove field aplicacao from token
--
ALTER TABLE "api_token" DROP COLUMN "aplicacao" CASCADE;
COMMIT;