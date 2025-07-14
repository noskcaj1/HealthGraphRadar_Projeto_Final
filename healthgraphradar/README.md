# HealthGraph Radar

Aplicação de mapeamento de dados clínicos com Streamlit + PostgreSQL (via Supabase).

## Funcionalidades

- Cadastro de prontuários clínicos
- Painel interativo com análise de dados
- Login seguro por perfil
- Integração com Supabase

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura de banco recomendada

Utilize o script SQL fornecido no setup para criar as tabelas: `usuarios`, `prontuarios`, `log_acesso`.

---