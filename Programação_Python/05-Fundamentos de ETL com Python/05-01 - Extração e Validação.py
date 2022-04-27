import pandas as pd
import pandera as pa

# Extração dos Dados:

df = pd.read_csv("ocorrencia.csv", sep=",", parse_dates=['ocorrencia_dia'], dayfirst=True)

# Esquema de Validação dos Tipos de Dados:

schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia": pa.Column(pa.Int),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classificacao": pa.Column(pa.String),
        "ocorrencia_cidade": pa.Column(pa.String, nullable=True),
        "ocorrencia_uf": pa.Column(pa.String, nullable=True),
        "ocorrencia_aerodromo": pa.Column(pa.String, nullable=True),
        "ocorrencia_dia": pa.Column(pa.DateTime, nullable=True),
        "ocorrencia_hora": pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])?$'), nullable=True),
        "total_recomendacoes": pa.Column(pa.Float, nullable=True)
    }
)

# Validação dos Tipos de Dados:

schema.validate(df)