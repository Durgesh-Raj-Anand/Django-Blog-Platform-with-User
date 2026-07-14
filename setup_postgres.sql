-- setup_postgres.sql
-- Run once as the postgres superuser to provision the database
-- for the Django blog project.

CREATE ROLE blog_user WITH LOGIN PASSWORD 'uMym3EODpS2So7icIoQ0CKU5dKY1';

CREATE DATABASE blog_db OWNER blog_user;

GRANT ALL PRIVILEGES ON DATABASE blog_db TO blog_user;

GRANT CREATE ON DATABASE blog_db TO blog_user;