import sqlite3
import logging
import schedule
import time
from datetime import datetime
import os


class IndonesianDataPipeline:
    def __init__(self, db_name="indonesia_data.db", log_file="pipeline.log"):
        self.db_name = db_name
        self.log_file = log_file
        self.setup_database()
        self.setup_logging()

    def setup_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS weather (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            city TEXT, temp REAL, condition TEXT, humidity INTEGER, date TEXT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS economic (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            province TEXT, gdp REAL, inflation REAL, exchange_rate REAL, date TEXT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS news (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT, summary TEXT, sentiment_keywords TEXT, category TEXT, date TEXT)""")
        conn.commit()
        conn.close()

    def setup_logging(self):
        logging.basicConfig(filename=self.log_file,
                            level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")

    def collect_all_data(self):
        logging.info("Collecting weather, economic, and news data...")
        # Simulated dummy entries (replace with real scraping or API calls)
        weather_data = {"city": "Jakarta", "temp": 31.5, "condition": "Sunny", "humidity": 70, "date": datetime.now().isoformat()}
        economic_data = {"province": "Jakarta", "gdp": 120.3, "inflation": 2.8, "exchange_rate": 15200, "date": datetime.now().isoformat()}
        news_data = {"title": "Ekonomi Naik", "summary": "Pertumbuhan ekonomi positif", "sentiment_keywords": "positif,maju",
                     "category": "ekonomi", "date": datetime.now().isoformat()}

        self.store_data("weather", weather_data)
        self.store_data("economic", economic_data)
        self.store_data("news", news_data)

    def store_data(self, table, data):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            keys = ','.join(data.keys())
            placeholders = ','.join(['?'] * len(data))
            values = tuple(data.values())
            cursor.execute(f"INSERT INTO {table} ({keys}) VALUES ({placeholders})", values)
            conn.commit()
            conn.close()
            logging.info(f"Stored data into '{table}': {data}")
        except Exception as e:
            logging.error(f"Failed to store data into '{table}': {e}")

    def validate_data_quality(self, data, data_type):
        logging.info(f"Validating {data_type} data...")
        issues = []

        # Basic checks
        if not data:
            issues.append("Empty data")
        if data_type == "weather" and ("temp" not in data or data["humidity"] > 100):
            issues.append("Weather data out of range or missing")

        if issues:
            logging.warning(f"Quality issues found in {data_type} data: {issues}")
        return issues

    def generate_daily_report(self):
        logging.info("Generating daily report...")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM weather")
        weather_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM economic")
        econ_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM news")
        news_count = cursor.fetchone()[0]
        conn.close()

        html_report = f"""
        <html><body>
        <h2>Daily Data Report</h2>
        <p>Weather Records: {weather_count}</p>
        <p>Economic Records: {econ_count}</p>
        <p>News Records: {news_count}</p>
        <p>Generated on: {datetime.now().isoformat()}</p>
        </body></html>
        """
        with open("daily_report.html", "w", encoding="utf-8") as f:
            f.write(html_report)
        logging.info("Daily report saved to 'daily_report.html'.")

    def run_pipeline(self):
        try:
            self.collect_all_data()
            self.generate_daily_report()
        except Exception as e:
            logging.error(f"Pipeline failed: {e}")


# Optional Scheduler
if __name__ == "__main__":
    pipeline = IndonesianDataPipeline()
    schedule.every().day.at("07:00").do(pipeline.run_pipeline)

    print("[INFO] Running daily scheduled pipeline...")
    while True:
        schedule.run_pending()
        time.sleep(60)
