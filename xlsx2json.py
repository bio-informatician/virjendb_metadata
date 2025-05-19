import pandas as pd
import json

df = pd.read_excel("metadata.xlsx", sheet_name=0, skiprows=3)
for col in df.columns:
    if df[col].dtype == object:  
        df[col] = df[col].apply(lambda x: x.replace('"', "'") if isinstance(x, str) else x)
        df[col] = df[col].apply(lambda x: x.replace('‘', "") if isinstance(x, str) else x)
        df[col] = df[col].apply(lambda x: x.replace('’', "") if isinstance(x, str) else x)

data = df.to_dict(orient="records")
json_str = json.dumps(data, ensure_ascii=False, indent=2)
with open("metadata.json", "w", encoding="utf-8") as f:
    f.write(json_str)
