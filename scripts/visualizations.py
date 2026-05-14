import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/reviews_with_sentiment_and_themes.csv")

# 1. Theme distribution
df["theme"].value_counts().plot(kind="bar")
plt.title("Theme Distribution Across All Banks")
plt.xlabel("Theme")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Sentiment by bank
df.groupby("bank")["sentiment_score"].mean().plot(kind="bar")
plt.title("Average Sentiment by Bank")
plt.ylabel("Sentiment Score")
plt.show()