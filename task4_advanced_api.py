import requests
import time
import json
import csv


class IndonesianDataCollector:
    def __init__(self):
        self.base_url = "https://www.emsifa.com/api-wilayah-indonesia/api"
        self.headers = {
            "User-Agent": "IndoDataCollector/1.0"
        }

    def safe_api_call(self, url, max_retries=3):
        """
        Perform an HTTP GET request with exponential backoff retry strategy.
        """
        delay = 1
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"[WARN] Attempt {attempt + 1} failed with status {response.status_code}")
            except requests.RequestException as e:
                print(f"[ERROR] Request failed: {e}")
            time.sleep(delay)
            delay *= 2  # exponential backoff
        print("[FAIL] Max retries reached. Skipping request.")
        return []

    def get_regional_data(self):
        """
        Get all provinces and their respective cities.
        """
        print("[INFO] Fetching provinces...")
        provinces = self.safe_api_call(f"{self.base_url}/provinces.json")
        regional_data = []

        for prov in provinces[:5]:  # limit to 5 provinces for demo
            prov_id = prov["id"]
            prov_name = prov["name"]
            print(f"[INFO] Fetching cities for {prov_name}...")
            cities = self.safe_api_call(f"{self.base_url}/regencies/{prov_id}.json")
            for city in cities:
                regional_data.append({
                    "province_id": prov_id,
                    "province_name": prov_name,
                    "city_id": city["id"],
                    "city_name": city["name"]
                })

        return regional_data

    def get_economic_indicators(self):
        """
        Simulate fetching economic indicators for each province.
        """
        print("[INFO] Simulating economic indicators...")
        # Simulated data (static mapping)
        economic_data = {
            "11": {"GDP": 102.5, "inflation": 3.1, "exchange_rate": 15200},
            "12": {"GDP": 89.3, "inflation": 2.9, "exchange_rate": 15200},
            "13": {"GDP": 76.0, "inflation": 3.4, "exchange_rate": 15200},
            "14": {"GDP": 98.7, "inflation": 2.7, "exchange_rate": 15200},
            "15": {"GDP": 120.4, "inflation": 3.2, "exchange_rate": 15200},
        }
        return economic_data

    def integrate_all_data(self):
        """
        Combine regional and economic data into a unified report.
        """
        print("[INFO] Integrating all data...")
        regional_data = self.get_regional_data()
        economic_data = self.get_economic_indicators()

        final_data = []
        for row in regional_data:
            econ = economic_data.get(row["province_id"], {})
            integrated = {
                **row,
                "GDP": econ.get("GDP", None),
                "inflation": econ.get("inflation", None),
                "exchange_rate": econ.get("exchange_rate", None)
            }
            final_data.append(integrated)

        return final_data

    def export_to_csv(self, data, filename="integrated_data.csv"):
        print(f"[INFO] Exporting to {filename}...")
        if not data:
            print("[WARN] No data to export.")
            return

        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def export_to_json(self, data, filename="integrated_data.json"):
        print(f"[INFO] Exporting to {filename}...")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    collector = IndonesianDataCollector()
    integrated_data = collector.integrate_all_data()

    collector.export_to_csv(integrated_data)
    collector.export_to_json(integrated_data)
