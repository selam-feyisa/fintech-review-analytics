import pandas as pd

df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Original shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna(subset=["review", "rating"])

# Normalize date
df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d")

df = df.dropna(subset=["date"])

print("Cleaned shape:", df.shape)

df.to_csv("data/raw/bank_reviews_clean.csv", index=False)

print("Preprocessing done!")