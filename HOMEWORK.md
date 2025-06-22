# 📝 HOMEWORK: Web Scraping and API for Indonesian Data

## 🎯 Assignment Overview

Test your web scraping and API skills through practical Indonesian data projects.

**Structure**: 3 Levels (Basic → Intermediate → Advanced) + Bonus Challenges  
**Focus**: Indonesian data sources and real-world applications  
**Timeline**: 3 weeks total

## ⚠️ Rules
- Ethical scraping (check robots.txt, respect rate limits)
- Include data sources and proper error handling
- Document code with comments
- Use Indonesian data sources

---

## 📚 LEVEL 1: BASIC (Week 1)

### Task 1: HTTP Requests (10%)
**Goal**: Get Indonesian provinces data via API

```python
# File: task1_http_basic.py
import requests

def get_indonesian_provinces():
    """Get provinces from: https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json"""
    # TODO: Implement HTTP GET request
    # TODO: Display total provinces and first 5 provinces
    pass

# Expected: 34 provinces total, display first 5 names
```

**Deliverable**: Script showing total provinces and first 5 province names

### Task 2: API Parameters (15%)
**Goal**: Search cities by province with proper headers

```python
# File: task2_api_parameters.py
import requests

class IndonesianCityAPI:
    def __init__(self):
        self.base_url = "https://www.emsifa.com/api-wilayah-indonesia/api"
        # TODO: Add proper headers
    
    def get_cities_by_province_id(self, province_id):
        """Get cities from specific province"""
        # TODO: Implement city search
        pass
    
    def search_city_by_name(self, city_name):
        """Search city by name across Indonesia"""
        # TODO: Implement case-insensitive search
        pass

# TODO: Get cities from West Java (ID: 32) and search for "Bandung"
```

**Deliverable**: Script that searches cities and displays statistics

### Task 3: Basic Web Scraping (15%)
**Goal**: Parse HTML weather data and save to CSV

```python
# File: task3_scraping_basic.py
from bs4 import BeautifulSoup
import csv

def scrape_weather_data(html_content):
    """Extract city, temperature, condition from sample HTML"""
    # TODO: Parse HTML and extract weather data for 5 Indonesian cities
    # TODO: Save to CSV with headers: city, temperature, condition, humidity
    pass

# Sample HTML provided with Jakarta, Surabaya, Bandung, Medan, Yogyakarta data
```

**Deliverable**: CSV file with weather data + analysis (highest/lowest temp, average)

---

## 📚 LEVEL 2: INTERMEDIATE (Week 2)

### Task 4: Advanced API Integration (20%)
**Goal**: Multi-source data collection with retry mechanism

```python
# File: task4_advanced_api.py
import requests
import time

class IndonesianDataCollector:
    def safe_api_call(self, url, max_retries=3):
        """API call with exponential backoff"""
        # TODO: Implement retry logic with delays
        pass
    
    def get_regional_data(self):
        """Collect provinces and cities data"""
        pass
    
    def get_economic_indicators(self):
        """Simulated economic data (GDP, inflation, exchange rate)"""
        pass
    
    def integrate_all_data(self):
        """Combine data from multiple sources"""
        pass

# TODO: Collect from 3+ sources, generate JSON/CSV reports
```

**Deliverable**: Integrated data report from multiple APIs with error handling

### Task 5: E-commerce Scraping (20%)
**Goal**: Scrape Indonesian product data with pagination

```python
# File: task5_ecommerce_scraping.py
from bs4 import BeautifulSoup
import pandas as pd

class IndonesianEcommerceScraper:
    def scrape_products(self, category, max_pages=3):
        """Scrape products: name, price, rating, seller, location"""
        # TODO: Scrape 4 categories (elektronik, fashion, makanan, rumah-tangga)
        # TODO: Handle pagination, extract 50+ products
        pass
    
    def analyze_products(self):
        """Price analysis by category, top sellers, rating distribution"""
        pass

# Sample product structure: name, price, rating, reviews_count, category, seller_location
```

**Deliverable**: Products CSV + analysis report + price comparison visualization

### Task 6: News Data Collection (20%)
**Goal**: Scrape Indonesian news for sentiment analysis prep

```python
# File: task6_news_scraping.py
from bs4 import BeautifulSoup
import re

class IndonesianNewsScraper:
    def scrape_news_category(self, category):
        """Scrape from: politik, ekonomi, teknologi, olahraga, hiburan"""
        # TODO: Extract title, summary, date, source, category
        # TODO: Collect 100+ articles across 5 categories
        pass
    
    def clean_news_text(self, text):
        """Clean and preprocess text"""
        pass
    
    def identify_sentiment_keywords(self):
        """Find positive/negative keywords for preliminary sentiment"""
        pass

# Structure: title, summary, category, source, date, sentiment_keywords
```

**Deliverable**: News dataset JSON + keyword analysis + summary report

---

## 📚 LEVEL 3: ADVANCED (Week 3)

### Task 7: Data Pipeline (25%)
**Goal**: Automated data collection and storage system

```python
# File: task7_data_pipeline.py
import sqlite3
import logging
import schedule

class IndonesianDataPipeline:
    def __init__(self):
        self.setup_database()  # SQLite tables for weather, news, economic data
        self.setup_logging()   # Comprehensive logging
    
    def collect_all_data(self):
        """Collect weather, economic, news data"""
        pass
    
    def validate_data_quality(self, data, data_type):
        """Check completeness, format, duplicates"""
        pass
    
    def generate_daily_report(self):
        """HTML report with data summary and quality metrics"""
        pass
    
    def run_pipeline(self):
        """Execute full pipeline with error handling"""
        pass

# TODO: Schedule daily runs, store in database, generate reports
```

**Deliverable**: SQLite database + daily HTML reports + quality metrics

### Task 8: Real-time Dashboard Data (25%)
**Goal**: Real-time data collection for dashboard

```python
# File: task8_realtime_dashboard.py
import threading
from collections import deque

class RealTimeIndonesianDataCollector:
    def __init__(self):
        self.data_buffer = {'weather': deque(maxlen=100), 'news': deque(maxlen=50)}
        self.update_intervals = {'weather': 300, 'news': 600}  # seconds
    
    def start_data_collection(self):
        """Start multi-threaded real-time collection"""
        pass
    
    def get_current_snapshot(self):
        """Current data state for dashboard"""
        pass
    
    def export_dashboard_data(self):
        """JSON format for dashboard consumption"""
        pass

# Structure: real-time weather, news, economic data with timestamps
```

**Deliverable**: Real-time JSON data + metrics + dashboard-ready format

---

## 🏆 BONUS CHALLENGES (+30% Extra Credit)

1. **Social Media Sentiment** (+10%): Analyze Indonesian social media posts sentiment
2. **Tourism Integration** (+10%): Combine weather, events, hotels data for tourism insights  
3. **Automated PDF Reports** (+10%): Generate PDF reports with visualizations

---

## 📊 Grading Rubric

| Aspect | Weight | Criteria |
|--------|--------|----------|
| Code Quality | 20% | Clean code, proper naming, comments |
| Functionality | 30% | All requirements met |
| Error Handling | 15% | Robust error handling |
| Data Quality | 15% | Validation and cleaning |
| Documentation | 10% | README and comments |
| Indonesian Context | 10% | Relevant local data sources |

## 📁 Submission Format

```
homework_submission/
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
├── level1/                      # Basic tasks (3 files)
├── level2/                      # Intermediate tasks (3 files)  
├── level3/                      # Advanced tasks (2 files)
├── data/                        # Generated CSV/JSON/DB files
├── reports/                     # HTML reports and metrics
└── bonus/                       # Bonus challenges (optional)
```

### README Template:
```markdown
# Indonesian Data Collection - Homework Submission

**Student**: [Name] | **ID**: [Student ID] | **Date**: [YYYY-MM-DD]

## Summary
Brief description of completed tasks...

## How to Run
1. `pip install -r requirements.txt`
2. `python level1/task1_http_basic.py`
3. Continue with other levels...

## Challenges & Learnings
Key challenges faced and lessons learned...

## Data Sources
- Indonesian Region API
- Simulated weather/news/ecommerce data
```

## ⏰ Timeline

- **Week 1**: Level 1 (Tasks 1-3) - Basic concepts
- **Week 2**: Level 2 (Tasks 4-6) - Practical applications  
- **Week 3**: Level 3 (Tasks 7-8) - Advanced integration
- **Week 4**: Bonus challenges (optional)

## 💡 Success Tips

1. Start with basic tasks, build incrementally
2. Test each function before moving forward
3. Implement proper error handling
4. Focus on Indonesian data sources
5. Document your code clearly
6. Respect rate limits and robots.txt

## 📚 Resources

- [Requests Documentation](https://requests.readthedocs.io/)
- [BeautifulSoup Guide](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Indonesian Region API](https://github.com/emsifa/api-wilayah-indonesia)

---

**Good luck! 🚀** Contact instructor for questions via learning platform. 