-- --------------------------------------------------------
-- Host:                         Z:\var\www\html\fullstacksushi\db1.sqlite3
-- Versione server:              3.34.0
-- S.O. server:                  
-- HeidiSQL Versione:            11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dump della struttura del database db1
CREATE DATABASE IF NOT EXISTS "db1";
-- USE "db1" neither supported nor required;

-- Dump della struttura di tabella db1.django_migrations
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);

-- Dump dei dati della tabella db1.django_migrations: -1 rows
/*!40000 ALTER TABLE "django_migrations" DISABLE KEYS */;
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES
	(1, 'contenttypes', '0001_initial', '2022-02-14 05:38:59.014961'),
	(2, 'auth', '0001_initial', '2022-02-14 05:38:59.032978'),
	(3, 'admin', '0001_initial', '2022-02-14 05:38:59.042865'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2022-02-14 05:38:59.052168'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-02-14 05:38:59.063516'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2022-02-14 05:38:59.082865'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2022-02-14 05:38:59.093946'),
	(8, 'auth', '0003_alter_user_email_max_length', '2022-02-14 05:38:59.103366'),
	(9, 'auth', '0004_alter_user_username_opts', '2022-02-14 05:38:59.110428'),
	(10, 'auth', '0005_alter_user_last_login_null', '2022-02-14 05:38:59.119557'),
	(11, 'auth', '0006_require_contenttypes_0002', '2022-02-14 05:38:59.122581'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2022-02-14 05:38:59.130222'),
	(13, 'auth', '0008_alter_user_username_max_length', '2022-02-14 05:38:59.139697'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2022-02-14 05:38:59.150936'),
	(15, 'auth', '0010_alter_group_name_max_length', '2022-02-14 05:38:59.160891'),
	(16, 'auth', '0011_update_proxy_permissions', '2022-02-14 05:38:59.169189'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2022-02-14 05:38:59.178022'),
	(18, 'sessions', '0001_initial', '2022-02-14 05:38:59.184047');
/*!40000 ALTER TABLE "django_migrations" ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
