import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
import random


class IndonesianEcommerceScraper:
    def __init__(self):
        self.products = []
        self.base_url = "https://example.com/{category}?page={page}"  # Replace with real e-commerce source

    def fetch_html(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
        except requests.RequestException as e:
            print(f"[ERROR] {e}")
        return None

    def parse_products(self, html, category):
        soup = BeautifulSoup(html, "html.parser")
        product_cards = soup.select(".product-card")  # Adjust selector to actual site

        for card in product_cards:
            try:
                name = card.select_one(".product-title").text.strip()
                price = int(card.select_one(".product-price").text.replace("Rp", "").replace(".", "").strip())
                rating = float(card.select_one(".product-rating").text.strip())
                reviews = int(card.select_one(".product-reviews").text.strip().split()[0])
                seller = card.select_one(".product-seller-location").text.strip()
                
                self.products.append({
                    "name": name,
                    "price": price,
                    "rating": rating,
                    "reviews_count": reviews,
                    "category": category,
                    "seller_location": seller
                })
            except Exception as e:
                print(f"[WARN] Skipping a product due to parsing error: {e}")

    def scrape_products(self, category, max_pages=3):
        print(f"[INFO] Scraping category: {category}")
        for page in range(1, max_pages + 1):
            url = self.base_url.format(category=category, page=page)
            html = self.fetch_html(url)
            if html:
                self.parse_products(html, category)
            time.sleep(random.uniform(1.5, 3.0))  # Polite scraping delay

    def analyze_products(self):
        if not self.products:
            print("[WARN] No product data to analyze.")
            return

        df = pd.DataFrame(self.products)

        # Save to CSV
        df.to_csv("indonesia_products.csv", index=False)
        print("[INFO] Saved products to 'indonesia_products.csv'")

        # Group by category: price statistics
        category_stats = df.groupby("category")["price"].describe()
        print("\n--- Price Statistics by Category ---\n", category_stats)

        # Top sellers
        top_sellers = df["seller_location"].value_counts().head(5)
        print("\n--- Top 5 Seller Locations ---\n", top_sellers)

        # Rating distribution
        rating_dist = df["rating"].value_counts().sort_index()
        print("\n--- Rating Distribution ---\n", rating_dist)

        # Save analysis report
        with open("analysis_report.txt", "w") as f:
            f.write("--- Price Statistics by Category ---\n")
            f.write(str(category_stats))
            f.write("\n\n--- Top 5 Seller Locations ---\n")
            f.write(str(top_sellers))
            f.write("\n\n--- Rating Distribution ---\n")
            f.write(str(rating_dist))
        print("[INFO] Analysis report saved as 'analysis_report.txt'")

        # Visualization
        plt.figure(figsize=(8, 5))
        df.groupby("category")["price"].mean().sort_values().plot(kind="bar", color="skyblue")
        plt.ylabel("Average Price (Rp)")
        plt.title("Average Product Price by Category")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("price_comparison.png")
        print("[INFO] Price comparison chart saved as 'price_comparison.png'")


if __name__ == "__main__":
    scraper = IndonesianEcommerceScraper()

    # Simulated categories; replace with actual categories or URLs
    categories = ["elektronik", "fashion", "makanan", "rumah-tangga"]

    for cat in categories:
        scraper.scrape_products(cat, max_pages=3)

    scraper.analyze_products()
