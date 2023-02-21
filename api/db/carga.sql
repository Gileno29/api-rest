SELECT 'CREATE DATABASE estoque'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mydb');
CREATE ROLE api WITH LOGIN PASSWORD 'api@docker';
CREATE ROLE leitura WITH LOGIN PASSWORD 'leitura@docker';


GRANT CONNECT ON DATABASE "estoque" TO "leitura";
GRANT USAGE ON SCHEMA public TO "leitura"; 
REVOKE CREATE ON SCHEMA public FROM PUBLIC; 
GRANT SELECT ON ALL TABLES IN SCHEMA public TO "leitura"; 
GRANT EXECUTE ON ALL PROCEDURES IN SCHEMA public TO "leitura"; 
GRANT ALL PRIVILEGES ON DATABASE "docker" TO "leitura"; 
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO "leitura"; 
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO "leitura"; 
REVOKE GRANT OPTION FOR CREATE ON DATABASE estoque FROM leitura; 
REVOKE INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA PUBLIC FROM leitura;