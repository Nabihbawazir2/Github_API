# File: task1_http_basic.py
import requests

class IndonesianProvinceFetcher:
    def __init__(self, url="https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json"):
        self.url = url
        self.provinces = []

    def fetch_provinces(self):
        """Fetch province data from the API and store it."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.provinces = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data: {e}")
            self.provinces = []

    def display_summary(self, count=5):
        """Display total provinces and the first 'count' province names."""
        if not self.provinces:
            print("No province data available.")
            return

        print(f"Total provinces: {len(self.provinces)}")
        print(f"First {count} provinces:")
        for province in self.provinces[:count]:
            print(f"- {province['name']}")

if __name__ == "__main__":
    fetcher = IndonesianProvinceFetcher()
    fetcher.fetch_provinces()
    fetcher.display_summary()
