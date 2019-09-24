BEGIN;
--
-- Create model Usuario
--
CREATE TABLE "usuario" ("id" serial NOT NULL PRIMARY KEY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "date_joined" timestamp with time zone NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL, "matricula" varchar(7) NOT NULL UNIQUE, "first_name" varchar(30) NULL, "last_name" varchar(30) NULL, "email" varchar(254) NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL);
CREATE TABLE "usuario_groups" ("id" serial NOT NULL PRIMARY KEY, "usuario_id" integer NOT NULL, "group_id" integer NOT NULL);
CREATE TABLE "usuario_user_permissions" ("id" serial NOT NULL PRIMARY KEY, "usuario_id" integer NOT NULL, "permission_id" integer NOT NULL);
CREATE INDEX "usuario_username_7e1fc9dc_like" ON "usuario" ("username" varchar_pattern_ops);
CREATE INDEX "usuario_matricula_4af4d2b0_like" ON "usuario" ("matricula" varchar_pattern_ops);
ALTER TABLE "usuario_groups" ADD CONSTRAINT "usuario_groups_usuario_id_161fc80c_fk_usuario_id" FOREIGN KEY ("usuario_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "usuario_groups" ADD CONSTRAINT "usuario_groups_group_id_c67c8651_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "usuario_groups" ADD CONSTRAINT "usuario_groups_usuario_id_group_id_2e3cd638_uniq" UNIQUE ("usuario_id", "group_id");
CREATE INDEX "usuario_groups_usuario_id_161fc80c" ON "usuario_groups" ("usuario_id");
CREATE INDEX "usuario_groups_group_id_c67c8651" ON "usuario_groups" ("group_id");
ALTER TABLE "usuario_user_permissions" ADD CONSTRAINT "usuario_user_permissions_usuario_id_693d9c50_fk_usuario_id" FOREIGN KEY ("usuario_id") REFERENCES "usuario" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "usuario_user_permissions" ADD CONSTRAINT "usuario_user_permiss_permission_id_a8893ce7_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "usuario_user_permissions" ADD CONSTRAINT "usuario_user_permissions_usuario_id_permission_id_3db58b8c_uniq" UNIQUE ("usuario_id", "permission_id");
CREATE INDEX "usuario_user_permissions_usuario_id_693d9c50" ON "usuario_user_permissions" ("usuario_id");
CREATE INDEX "usuario_user_permissions_permission_id_a8893ce7" ON "usuario_user_permissions" ("permission_id");
COMMIT;

BEGIN;
--
-- Remove field created_at from usuario
--
ALTER TABLE "usuario" DROP COLUMN "created_at" CASCADE;
--
-- Remove field updated_at from usuario
--
ALTER TABLE "usuario" DROP COLUMN "updated_at" CASCADE;
--
-- Add field criado to usuario
--
ALTER TABLE "usuario" ADD COLUMN "criado" timestamp with time zone DEFAULT '2019-09-24T14:05:46.261940+00:00'::timestamptz NULL;
ALTER TABLE "usuario" ALTER COLUMN "criado" DROP DEFAULT;
--
-- Add field modificado to usuario
--
ALTER TABLE "usuario" ADD COLUMN "modificado" timestamp with time zone DEFAULT '2019-09-24T14:05:46.266737+00:00'::timestamptz NULL;
ALTER TABLE "usuario" ALTER COLUMN "modificado" DROP DEFAULT;
COMMIT;