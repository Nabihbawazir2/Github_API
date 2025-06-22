from bs4 import BeautifulSoup
import csv


class WeatherData:
    def __init__(self, city, temperature, condition, humidity):
        self.city = city
        self.temperature = float(temperature)  # Celsius, e.g., 30.5
        self.condition = condition
        self.humidity = int(humidity.strip('%'))  # percentage

    def to_list(self):
        return [self.city, self.temperature, self.condition, self.humidity]


class WeatherScraper:
    def __init__(self, html_content):
        self.html_content = html_content
        self.weather_data = []

    def parse_html(self):
        soup = BeautifulSoup(self.html_content, "html.parser")
        rows = soup.select("table.weather-table tr")[1:]  # skip header row

        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 4:
                city = cells[0].get_text(strip=True)
                temp = cells[1].get_text(strip=True).replace("°C", "")
                condition = cells[2].get_text(strip=True)
                humidity = cells[3].get_text(strip=True)
                self.weather_data.append(WeatherData(city, temp, condition, humidity))

    def save_to_csv(self, filename="weather_data.csv"):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["city", "temperature", "condition", "humidity"])
            for entry in self.weather_data:
                writer.writerow(entry.to_list())


class WeatherAnalyzer:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def get_summary(self):
        if not self.weather_data:
            print("No data to analyze.")
            return

        temps = [entry.temperature for entry in self.weather_data]
        highest = max(self.weather_data, key=lambda x: x.temperature)
        lowest = min(self.weather_data, key=lambda x: x.temperature)
        avg = sum(temps) / len(temps)

        print("\n--- Weather Summary ---")
        print(f"Hottest city: {highest.city} ({highest.temperature}°C)")
        print(f"Coldest city: {lowest.city} ({lowest.temperature}°C)")
        print(f"Average temperature: {avg:.2f}°C")


# --- Sample Execution Code ---
if __name__ == "__main__":
    # Sample HTML (should be replaced with real HTML in use)
    sample_html = """
    <html><body>
    <table class="weather-table">
        <tr><th>City</th><th>Temp</th><th>Condition</th><th>Humidity</th></tr>
        <tr><td>Jakarta</td><td>31°C</td><td>Sunny</td><td>70%</td></tr>
        <tr><td>Surabaya</td><td>34°C</td><td>Cloudy</td><td>65%</td></tr>
        <tr><td>Bandung</td><td>27°C</td><td>Rainy</td><td>85%</td></tr>
        <tr><td>Medan</td><td>33°C</td><td>Sunny</td><td>68%</td></tr>
        <tr><td>Yogyakarta</td><td>29°C</td><td>Thunderstorm</td><td>75%</td></tr>
    </table>
    </body></html>
    """

    # Scrape
    scraper = WeatherScraper(sample_html)
    scraper.parse_html()
    scraper.save_to_csv()

    # Analyze
    analyzer = WeatherAnalyzer(scraper.weather_data)
    analyzer.get_summary()
