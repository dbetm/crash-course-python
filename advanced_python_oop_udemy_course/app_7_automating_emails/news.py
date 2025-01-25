import os

import requests
from dotenv import load_dotenv


load_dotenv()

# https://newsapi.org/

class NewsFeed:
    base_url = "https://newsapi.org/v2/everything"
    sort_by = "popularity"
    api_key = os.getenv("API_KEY", "")

    def __init__(self, interest_topic: str, from_date: str, to_date: str):
        self.interest_topic = interest_topic
        self.from_date = from_date
        self.to_date = to_date
        self.url = (
            f"{self.base_url}?q={interest_topic}&from={from_date}&to={to_date}&sortBy={self.sort_by}"
            f"&apiKey={self.api_key}"
        )

    def get(self, top_k: int = 5) -> str:
        response = requests.get(self.url)
        content = response.json()

        raw_body = list()

        for article in content["articles"]:
            title = article["title"]
            url = article["url"]

            raw_body.append(f"{title}\n{url}\n")

            if len(raw_body) > top_k:
                break

        return "\n".join(raw_body)


if __name__ == "__main__":
    news_feed = NewsFeed(interest_topic="nasa", from_date="2025-01-22", to_date="2025-01-23")

    body = news_feed.get()

    print(body)