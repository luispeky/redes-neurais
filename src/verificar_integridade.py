from pathlib import Path

import pandas as pd

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

df = pd.read_excel(data_dir / "wdbc.xlsx")

# 1. Conferir dimensões (esperado: 569 linhas, 32 colunas)
print("Shape:", df.shape)

# 2. Verificar valores ausentes e linhas duplicadas
print("Nulos por coluna:\n", df.isnull().sum()[df.isnull().sum() > 0])
print("IDs duplicados:", df.iloc[:, 0].duplicated().sum())

# 3. Conferir tipos (colunas numéricas lidas como 'object'/texto indicam erro de decimal)
print("\nTipos das colunas:\n", df.dtypes.value_counts())
print("\nAmostra de valores e escalas (min e max):")
print(df.describe().T[["min", "mean", "max"]].head(12))