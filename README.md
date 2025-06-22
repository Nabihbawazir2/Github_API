# 🇮🇩 Gathering Data for AI Projects: Web Scraping and APIs

## 📋 Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Core Concepts](#core-concepts)
- [Tools and Libraries](#tools-and-libraries)
- [Learning Structure](#learning-structure)
- [Indonesian Use Cases](#indonesian-use-cases)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## 🎯 Introduction

Welcome to the **"How to Gather Data for Your AI Projects: Web Scraping and APIs"** learning module designed specifically for Indonesian students! 

In this digital era, data is the most valuable asset for AI projects. This module will teach you how to collect data from various online sources using web scraping and API techniques, with a focus on Indonesian data sources.

### Why is this Important?
- 🔍 **80% of data scientist time** is spent collecting and cleaning data
- 📊 **Quality data** is the key to successful AI projects
- 🌐 **The internet** provides trillions of data points that can be utilized
- 🇮🇩 **Indonesian data** is very valuable for understanding local context

## 🎯 Learning Objectives

After completing this module, you will be able to:

### 🔧 Technical Skills
- ✅ Understand HTTP protocols and how the web works
- ✅ Use the `requests` library for API calls
- ✅ Perform web scraping with `BeautifulSoup`
- ✅ Handle various data formats (JSON, HTML, CSV)
- ✅ Implement error handling and retry mechanisms
- ✅ Combine data from multiple sources

### 📊 Analytical Skills
- ✅ Clean and validate data
- ✅ Analyze website and API structures
- ✅ Identify useful data patterns
- ✅ Optimize data collection processes

### 🌏 Indonesian Context
- ✅ Access Indonesian government data
- ✅ Scrape Indonesian news websites
- ✅ Use local e-commerce APIs
- ✅ Collect Indonesian economic and social data

## 📚 Core Concepts

### 1. HTTP Protocol
HTTP (HyperText Transfer Protocol) is the foundation of web communication.

#### HTTP Methods
- **GET**: Retrieve data from server
- **POST**: Send data to server
- **PUT**: Update data on server
- **DELETE**: Delete data from server

#### HTTP Status Codes
```
200 - OK (Success)
404 - Not Found (Page not found)
429 - Too Many Requests (Rate limited)
500 - Internal Server Error (Server error)
```

#### Headers
Headers provide additional information about request/response:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Indonesian Student Bot)',
    'Accept': 'application/json',
    'Accept-Language': 'id-ID,id;q=0.9'
}
```

### 2. APIs (Application Programming Interfaces)

API is an interface that allows applications to communicate with other systems.

#### REST API
- **Representational State Transfer**
- Uses standard HTTP methods
- Data is usually in JSON format
- Stateless (does not store state)

#### API Authentication
1. **API Key**: Simple token for identification
2. **OAuth**: Standard for authorization
3. **Bearer Token**: Token carried in header

### 3. Web Scraping

Web scraping is the process of automatically extracting data from websites.

#### HTML Structure
```html
<html>
  <head>
    <title>Judul Halaman</title>
  </head>
  <body>
    <div class="container">
      <h1 id="main-title">Judul Utama</h1>
      <p class="content">Konten paragraf</p>
    </div>
  </body>
</html>
```

#### CSS Selectors
- **Tag**: `div`, `p`, `h1`
- **Class**: `.container`, `.content`
- **ID**: `#main-title`
- **Attribute**: `[href="link"]`

## 🛠️ Tools and Libraries

### Python Libraries Used

#### 1. Requests
```python
import requests

# Basic GET request
response = requests.get('https://api.example.com/data')
print(response.json())

# POST request with data
data = {'name': 'Jakarta', 'country': 'Indonesia'}
response = requests.post('https://api.example.com/cities', json=data)
```

#### 2. BeautifulSoup
```python
from bs4 import BeautifulSoup

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find elements
title = soup.find('title').text
articles = soup.find_all('article', class_='news-item')
```

#### 3. Pandas
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame(data)

# Save to different formats
df.to_csv('data.csv', index=False)
df.to_json('data.json', orient='records')
```

#### 4. JSON
```python
import json

# Parse JSON string
data = json.loads(json_string)

# Save to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

### Development Tools

#### 1. Browser Developer Tools
- **Inspect Element**: Melihat struktur HTML
- **Network Tab**: Monitor HTTP requests
- **Console**: Debug JavaScript

#### 2. Postman
- Test API endpoints
- Manage API collections
- Generate code snippets

#### 3. Jupyter Notebook
- Interactive development
- Data visualization
- Documentation

## 📖 Learning Structure

### Step 1: Basic HTTP Requests
**Duration**: 30 minutes
- Understanding HTTP protocol
- Using `requests` library
- Handling response and errors

**Practice**:
```python
import requests

# Simple GET request
response = requests.get('https://httpbin.org/get')
print(f"Status: {response.status_code}")
print(f"Data: {response.json()}")
```

### Step 2: Working with APIs
**Duration**: 45 minutes
- REST API concepts
- Authentication methods
- Rate limiting and best practices

**Practice**:
```python
# Indonesian Region API
response = requests.get('https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json')
provinces = response.json()
print(f"Indonesia has {len(provinces)} provinces")
```

### Step 3: Web Scraping Basics
**Duration**: 60 minutes
- HTML parsing with BeautifulSoup
- CSS selectors
- Extracting data from elements

**Practice**:
```python
from bs4 import BeautifulSoup

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract news headlines
headlines = soup.find_all('h2', class_='news-title')
for headline in headlines:
    print(headline.text.strip())
```

### Step 4: Advanced Scraping
**Duration**: 60 minutes
- Sessions and cookies
- Handling JavaScript content
- Rate limiting implementation

### Step 5: Data Processing
**Duration**: 45 minutes
- Data cleaning techniques
- Using pandas for analysis
- Saving in multiple formats

### Step 6: Error Handling
**Duration**: 30 minutes
- Exception handling
- Retry mechanisms
- Logging and debugging

### Step 7: Integration
**Duration**: 45 minutes
- Combining API and scraping data
- Data enrichment
- Creating final datasets

## 🇮🇩 Indonesian Use Cases

### 1. Jakarta Weather Data
```python
# Using OpenWeatherMap API
api_key = "YOUR_API_KEY"
city = "Jakarta"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
weather_data = response.json()

print(f"Jakarta Weather: {weather_data['main']['temp']}°C")
print(f"Condition: {weather_data['weather'][0]['description']}")
```

### 2. Scraping Indonesian News
```python
from bs4 import BeautifulSoup
import requests

# Scraping headlines (example structure)
url = "https://example-news-site.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

headlines = soup.find_all('h2', class_='headline')
for headline in headlines:
    print(f"📰 {headline.text.strip()}")
```

### 3. Indonesian Stock Data
```python
# Accessing IHSG (Indonesia Stock Exchange) data
# Example using Yahoo Finance API
import yfinance as yf

# Download BBCA (Bank Central Asia) stock data
bbca = yf.download('BBCA.JK', start='2024-01-01', end='2024-12-31')
print(f"BBCA closing price: {bbca['Close'].iloc[-1]}")
```

### 4. Indonesian E-commerce Data
```python
# Scraping product data (with rate limiting)
import time

def scrape_products(base_url, max_pages=5):
    products = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract product info
            items = soup.find_all('div', class_='product-item')
            for item in items:
                product = {
                    'name': item.find('h3').text.strip(),
                    'price': item.find('span', class_='price').text.strip(),
                    'rating': item.find('div', class_='rating')['data-rating']
                }
                products.append(product)
        
        # Polite delay
        time.sleep(2)
    
    return products
```

### 5. Indonesian Government Data
```python
# Accessing government open data
# Example: BPS (Statistics Indonesia) data

def get_population_data():
    # BPS API simulation
    url = "https://webapi.bps.go.id/v1/api/list/model/data/domain/0000/var/xxx"
    
    headers = {
        'User-Agent': 'Indonesian-Student-Research/1.0'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
```

## ✅ Best Practices

### 1. Ethical Scraping
- 🤖 **robots.txt**: Always check and respect robots.txt
- ⏱️ **Rate Limiting**: Don't overload servers with requests
- 👤 **User-Agent**: Use clear and informative User-Agent
- 📧 **Contact Info**: Include contact info in User-Agent

```python
headers = {
    'User-Agent': 'Indonesian-Student-Bot/1.0 (Educational Purpose; Contact: student@university.ac.id)'
}
```

### 2. Error Handling
```python
def safe_request(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response
            elif response.status_code == 429:
                # Rate limited, wait longer
                time.sleep(60)
                continue
        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
        except requests.exceptions.ConnectionError:
            print(f"Connection error on attempt {attempt + 1}")
        
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)  # Exponential backoff
    
    return None
```

### 3. Data Validation
```python
def validate_indonesian_city_data(data):
    required_fields = ['city', 'population', 'province']
    valid_provinces = ['DKI Jakarta', 'Jawa Barat', 'Jawa Timur', ...]  # Complete list
    
    errors = []
    
    for i, record in enumerate(data):
        # Check required fields
        for field in required_fields:
            if field not in record or not record[field]:
                errors.append(f"Row {i}: Missing {field}")
        
        # Validate province
        if record.get('province') not in valid_provinces:
            errors.append(f"Row {i}: Invalid province")
        
        # Validate population
        if not isinstance(record.get('population'), int) or record['population'] < 0:
            errors.append(f"Row {i}: Invalid population")
    
    return errors
```

### 4. Data Storage
```python
def save_data_multiple_formats(data, base_filename):
    """Save data in multiple formats for flexibility"""
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save as CSV (good for Excel, analysis)
    df.to_csv(f'{base_filename}.csv', index=False, encoding='utf-8')
    
    # Save as JSON (good for web apps, APIs)
    df.to_json(f'{base_filename}.json', orient='records', indent=2)
    
    # Save as Excel (good for business users)
    try:
        df.to_excel(f'{base_filename}.xlsx', index=False, engine='openpyxl')
    except ImportError:
        print("Excel export requires openpyxl: pip install openpyxl")
    
    # Save summary statistics
    with open(f'{base_filename}_summary.txt', 'w') as f:
        f.write(f"Dataset Summary\n")
        f.write(f"===============\n")
        f.write(f"Total records: {len(df)}\n")
        f.write(f"Columns: {', '.join(df.columns)}\n")
        f.write(f"Date created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
```

## 🚨 Troubleshooting

### Common Issues and Solutions

#### 1. HTTP 403 Forbidden
**Problem**: Website blocks your requests
**Solution**:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}
```

#### 2. HTTP 429 Too Many Requests
**Problem**: Rate limiting
**Solution**:
```python
import time
import random

def polite_request(url):
    # Random delay between 1-3 seconds
    delay = random.uniform(1, 3)
    time.sleep(delay)
    
    response = requests.get(url)
    
    if response.status_code == 429:
        # Wait longer if rate limited
        time.sleep(60)
        return polite_request(url)  # Retry
    
    return response
```

#### 3. Dynamic Content (JavaScript)
**Problem**: Content loaded with JavaScript
**Solution**: Use Selenium
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url)

# Wait for content to load
time.sleep(5)

# Now scrape the content
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

driver.quit()
```

#### 4. Encoding Issues
**Problem**: Indonesian characters not readable
**Solution**:
```python
# Specify encoding explicitly
response = requests.get(url)
response.encoding = 'utf-8'
content = response.text

# When saving to file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

#### 5. Memory Issues with Large Data
**Problem**: Out of memory with large datasets
**Solution**:
```python
def process_large_dataset_chunks(data, chunk_size=1000):
    """Process large dataset in chunks"""
    
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        
        # Process chunk
        processed_chunk = process_data_chunk(chunk)
        
        # Save chunk
        chunk_filename = f'data_chunk_{i//chunk_size + 1}.csv'
        pd.DataFrame(processed_chunk).to_csv(chunk_filename, index=False)
        
        print(f"Processed chunk {i//chunk_size + 1}")
```

## 📋 Learning Checklist

Use this checklist to ensure you have mastered all concepts:

### Basic Concepts
- [ ] Understanding HTTP methods (GET, POST, PUT, DELETE)
- [ ] Understanding HTTP status codes
- [ ] Using headers in requests
- [ ] Understanding query parameters

### API Skills
- [ ] Making API calls with requests
- [ ] Understanding JSON format
- [ ] Implementing authentication (API key, OAuth)
- [ ] Handling rate limits

### Web Scraping Skills
- [ ] Parsing HTML with BeautifulSoup
- [ ] Using CSS selectors
- [ ] Extracting data from various HTML elements
- [ ] Handling forms and sessions

### Advanced Techniques
- [ ] Implementing retry mechanisms
- [ ] Comprehensive error handling
- [ ] Rate limiting for polite scraping
- [ ] Data validation and cleaning

### Indonesian Context
- [ ] Scraping Indonesian websites
- [ ] Using Indonesian government APIs
- [ ] Handling Indonesian language in data
- [ ] Understanding Indonesian data structures

### Data Management
- [ ] Saving data in multiple formats
- [ ] Data cleaning and preprocessing
- [ ] Combining multiple data sources
- [ ] Creating summary reports

## 📚 Referensi

### Official Documentation
- [Requests Documentation](https://requests.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Indonesian Data Sources
- [API Wilayah Indonesia](https://github.com/emsifa/api-wilayah-indonesia)
- [Data Terbuka Indonesia](https://data.go.id/)
- [BPS (Badan Pusat Statistik)](https://www.bps.go.id/)
- [Bank Indonesia API](https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/Default.aspx)

### Learning Resources
- [HTTP Status Codes](https://httpstatuses.com/)
- [CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.asp)
- [JSON Format Guide](https://www.json.org/json-en.html)

### Tools
- [Postman](https://www.postman.com/) - API testing
- [JSONViewer](https://jsonviewer.stack.hu/) - JSON formatting
- [Regex101](https://regex101.com/) - Regular expressions testing

## 🎯 Next Steps

After completing this module, you can continue to:

1. **Data Cleaning and Preparation** - Cleaning data for AI models
2. **Exploratory Data Analysis** - Analyzing collected data
3. **Feature Engineering** - Creating features for machine learning
4. **Database Integration** - Storing data in databases
5. **Real-time Data Processing** - Stream processing for real-time data

## 💡 Success Tips

1. **Practice Regularly**: Practice scraping various Indonesian websites
2. **Stay Updated**: Web scraping techniques are constantly evolving
3. **Be Ethical**: Always respect robots.txt and terms of service
4. **Document Everything**: Record all data sources and methods
5. **Join Communities**: Join Indonesian data science communities

---

**Happy learning and good luck on your AI journey! 🚀**

*Made with ❤️ for Indonesian students* 