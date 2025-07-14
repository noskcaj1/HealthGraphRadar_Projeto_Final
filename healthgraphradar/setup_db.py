from sqlalchemy import create_engine, text
import os

engine = create_engine(os.getenv("DB_URL"))

with engine.begin() as conn:
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        usuario TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        perfil TEXT CHECK (perfil IN ('admin', 'profissional', 'consulta')) NOT NULL DEFAULT 'profissional',
        ativo BOOLEAN DEFAULT TRUE
    );

    CREATE TABLE IF NOT EXISTS prontuarios (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        sexo TEXT CHECK (sexo IN ('Masculino', 'Feminino', 'Outro')) NOT NULL,
        sintomas TEXT,
        diagnostico TEXT,
        profissional_id INTEGER REFERENCES usuarios(id),
        data_insercao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS log_acesso (
        id SERIAL PRIMARY KEY,
        usuario_id INTEGER REFERENCES usuarios(id),
        acao TEXT NOT NULL,
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    INSERT INTO usuarios (nome, email, usuario, senha, perfil)
    VALUES ('Admin', 'admin@healthgraph.com', 'admin', 'admin123', 'admin')
    ON CONFLICT (usuario) DO NOTHING;
    """))