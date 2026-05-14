import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load cleaned data
df = pd.read_csv("data/raw/bank_reviews_clean.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

labels = []
scores = []

for text in df["review"].astype(str):
    # Get sentiment score
    score = analyzer.polarity_scores(text)["compound"]
    scores.append(score)

    # Convert score to label
    if score >= 0.05:
        labels.append("POSITIVE")
    elif score <= -0.05:
        labels.append("NEGATIVE")
    else:
        labels.append("NEUTRAL")

# Add results to dataframe
df["sentiment_label"] = labels
df["sentiment_score"] = scores

# Save output
df.to_csv("data/raw/reviews_with_sentiment.csv", index=False)

print("✅ Sentiment analysis completed successfully")
print(df.head())