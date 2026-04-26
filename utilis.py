import pandas as pd

def clean_data(df):
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("N\A")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"],errors = "coerce")
    return df