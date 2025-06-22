import threading
import time
from collections import deque
from datetime import datetime
import json
import random


class RealTimeIndonesianDataCollector:
    def __init__(self):
        self.data_buffer = {
            'weather': deque(maxlen=100),
            'news': deque(maxlen=50)
        }
        self.update_intervals = {
            'weather': 300,  # 5 minutes
            'news': 600      # 10 minutes
        }

    def _collect_weather_data(self):
        while True:
            simulated_data = {
                "timestamp": datetime.now().isoformat(),
                "city": "Jakarta",
                "temperature": round(random.uniform(28, 34), 1),
                "condition": random.choice(["Sunny", "Cloudy", "Rainy"]),
                "humidity": random.randint(60, 90)
            }
            self.data_buffer["weather"].append(simulated_data)
            print("[Weather] Updated buffer with:", simulated_data)
            time.sleep(self.update_intervals["weather"])

    def _collect_news_data(self):
        while True:
            simulated_data = {
                "timestamp": datetime.now().isoformat(),
                "title": "Industri Teknologi Tumbuh",
                "category": "teknologi",
                "summary": "Berita teknologi terbaru menunjukkan pertumbuhan.",
                "sentiment_keywords": ["maju", "positif"]
            }
            self.data_buffer["news"].append(simulated_data)
            print("[News] Updated buffer with:", simulated_data)
            time.sleep(self.update_intervals["news"])

    def start_data_collection(self):
        weather_thread = threading.Thread(target=self._collect_weather_data, daemon=True)
        news_thread = threading.Thread(target=self._collect_news_data, daemon=True)
        weather_thread.start()
        news_thread.start()

    def get_current_snapshot(self):
        return {
            "weather": list(self.data_buffer["weather"]),
            "news": list(self.data_buffer["news"])
        }

    def export_dashboard_data(self, filename="realtime_dashboard.json"):
        snapshot = self.get_current_snapshot()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(snapshot, f, indent=2, ensure_ascii=False)
        print(f"[INFO] Exported real-time snapshot to {filename}")


# Run Example
if __name__ == "__main__":
    collector = RealTimeIndonesianDataCollector()
    collector.start_data_collection()

    # Simulate periodic export
    while True:
        collector.export_dashboard_data()
        time.sleep(60)  # export every minute
