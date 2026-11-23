from pathlib import Path

import pandas as pd

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

# Mantém os mesmos nomes de colunas do seu wdbc.xlsx atual (radius1...radius3)
features = [
    "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave_points", "symmetry", "fractal_dimension"
]
colunas = (
    ["ID", "Diagnosis"]
    + [f"{f}1" for f in features]
    + [f"{f}2" for f in features]
    + [f"{f}3" for f in features]
)

df = pd.read_csv(data_dir / "wdbc.data", header=None, names=colunas)
df.to_excel(data_dir / "wdbc.xlsx", index=False)
print(df.dtypes.value_counts())  # Deve mostrar: float64: 30, int64: 1, object: 1
