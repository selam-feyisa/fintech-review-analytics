from google_play_scraper import reviews, Sort
import pandas as pd
import time

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_data = []

for bank, app_id in apps.items():
    print(f"Scraping {bank}...")

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=500
    )

    for r in result:
        all_data.append({
            "review": r.get("content"),
            "rating": r.get("score"),
            "date": r.get("at").strftime("%Y-%m-%d") if r.get("at") else None,
            "bank": bank,
            "source": "Google Play"
        })

    time.sleep(2)  # avoid blocking

df = pd.DataFrame(all_data)

print("Total reviews:", len(df))

df.to_csv("data/raw/bank_reviews_raw.csv", index=False)
