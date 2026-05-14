import pandas as pd

df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

def assign_theme(text):
    text = str(text).lower()

    # LOGIN ISSUES
    if any(word in text for word in ["login", "sign in", "password", "account"]):
        return "Account/Login Issues"

    # OTP / AUTH
    if any(word in text for word in ["otp", "code", "verification"]):
        return "OTP & Verification Issues"

    # TRANSACTION / TRANSFER
    if any(word in text for word in ["transfer", "transaction", "send money", "payment"]):
        return "Transaction Issues"

    # PERFORMANCE
    if any(word in text for word in ["slow", "lag", "delay", "hang"]):
        return "Performance Issues"

    # APP CRASH / BUG
    if any(word in text for word in ["crash", "error", "bug", "stuck"]):
        return "App Stability Issues"

    # UI / UX
    if any(word in text for word in ["ui", "interface", "design", "look"]):
        return "UI/UX Issues"

    # FEATURE REQUEST
    if any(word in text for word in ["feature", "add", "need", "should"]):
        return "Feature Requests"

    return "General Feedback"


df["theme"] = df["review"].apply(assign_theme)

# Save output
df.to_csv("data/raw/reviews_with_sentiment_and_themes.csv", index=False)

print("\n✅ Theme classification completed!\n")
print(df["theme"].value_counts())