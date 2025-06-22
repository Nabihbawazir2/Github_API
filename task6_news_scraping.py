import requests
from bs4 import BeautifulSoup
import re
import json
import time
from collections import Counter


class IndonesianNewsScraper:
    def __init__(self):
        self.base_url = "https://example-news.com/{category}/page/{page}"  # placeholder
        self.categories = ["politik", "ekonomi", "teknologi", "olahraga", "hiburan"]
        self.news_data = []
        self.positive_keywords = {"maju", "sukses", "positif", "menang", "stabil"}
        self.negative_keywords = {"gagal", "turun", "korupsi", "negatif", "kalah"}

    def fetch_html(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
        return None

    def parse_articles(self, html, category):
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.select(".news-card")  # Update this selector

        for card in articles:
            try:
                title = card.select_one(".title").get_text(strip=True)
                summary = card.select_one(".summary").get_text(strip=True)
                date = card.select_one(".date").get_text(strip=True)
                source = "Example News"  # Placeholder

                cleaned_summary = self.clean_news_text(summary)
                sentiment_tags = self.identify_sentiment_keywords(cleaned_summary)

                self.news_data.append({
                    "title": title,
                    "summary": cleaned_summary,
                    "category": category,
                    "source": source,
                    "date": date,
                    "sentiment_keywords": sentiment_tags
                })
            except Exception as e:
                print(f"[WARN] Failed to parse article: {e}")

    def scrape_news_category(self, category, max_pages=5):
        print(f"[INFO] Scraping category: {category}")
        for page in range(1, max_pages + 1):
            url = self.base_url.format(category=category, page=page)
            html = self.fetch_html(url)
            if html:
                self.parse_articles(html, category)
            time.sleep(1.5)  # polite delay

    def clean_news_text(self, text):
        text = re.sub(r"\s+", " ", text)  # remove excessive whitespace
        text = re.sub(r"http\S+", "", text)  # remove URLs
        text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
        return text.lower().strip()

    def identify_sentiment_keywords(self, text):
        found = set()
        for word in self.positive_keywords.union(self.negative_keywords):
            if word in text:
                found.add(word)
        return list(found)

    def export_to_json(self, filename="news_dataset.json"):
        with open(filename, "w", encoding="utf-8") as
