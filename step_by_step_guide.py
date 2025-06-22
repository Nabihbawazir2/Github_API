#!/usr/bin/env python3
"""
Step-by-Step Technical Guide: Web Scraping and APIs for Indonesian Data
=====================================================================

This comprehensive guide teaches web scraping and API usage through Indonesian examples.
Each section builds upon the previous one, from basic concepts to advanced techniques.

Learning Path:
1. Basic HTTP Requests
2. Working with APIs
3. Introduction to Web Scraping
4. Advanced Scraping Techniques
5. Data Processing and Storage
6. Error Handling and Best Practices
7. Combining Multiple Data Sources

Author: AI Engineering Course
Target: Indonesian Students
"""

import requests
import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.parse
import csv

print("🇮🇩 STEP-BY-STEP GUIDE: WEB SCRAPING AND API")
print("=" * 60)

# =============================================================================
# STEP 1: BASIC HTTP REQUESTS - MEMAHAMI DASAR-DASAR HTTP
# =============================================================================

print("\n📚 STEP 1: UNDERSTANDING HTTP REQUESTS")
print("-" * 40)

def step1_basic_http_requests():
    """
    Step 1: Understanding the basics of HTTP requests
    """
    print("🎯 Objective: Understanding how HTTP requests work")
    print("📖 Concepts: GET, POST, Headers, Status Codes")
    
    # Example 1: Simple GET request
    print("\n1.1 Simple GET Request to Indonesian website")
    try:
        response = requests.get('https://httpbin.org/get')
        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response Type: {type(response.json())}")
        print(f"✅ Sample Data: {list(response.json().keys())}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Example 2: Request with headers
    print("\n1.2 Request with Custom Headers")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Indonesian Student Bot)',
        'Accept': 'application/json',
        'Accept-Language': 'id-ID,id;q=0.9,en;q=0.8'
    }
    
    try:
        response = requests.get('https://httpbin.org/headers', headers=headers)
        print(f"✅ Headers sent successfully: {response.status_code}")
        data = response.json()
        print(f"✅ User-Agent detected: {data['headers'].get('User-Agent', 'N/A')}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Example 3: Request with parameters
    print("\n1.3 Request with Query Parameters")
    params = {
        'city': 'Jakarta',
        'country': 'Indonesia',
        'lang': 'id'
    }
    
    try:
        response = requests.get('https://httpbin.org/get', params=params)
        print(f"✅ Parameters sent successfully: {response.status_code}")
        data = response.json()
        print(f"✅ Final URL: {data['url']}")
        print(f"✅ Parameters: {data['args']}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n💡 Key Learning Points:")
    print("- HTTP status codes: 200 (OK), 404 (Not Found), 500 (Server Error)")
    print("- Headers provide additional information about the request")
    print("- Query parameters are used to send data in the URL")
    print("- Always handle exceptions for error handling")

# =============================================================================
# STEP 2: WORKING WITH APIs - USING INDONESIAN APIs
# =============================================================================

print("\n📚 STEP 2: WORKING WITH APIs")
print("-" * 40)

def step2_working_with_apis():
    """
    Step 2: Working with APIs using Indonesian examples
    """
    print("🎯 Objective: Accessing real-time data through APIs")
    print("📖 Concepts: REST API, JSON, Authentication, Rate Limiting")
    
    # Example 1: Indonesian Region API (No Auth)
    print("\n2.1 Accessing Indonesian Region API")
    try:
        # Free API for Indonesian region data
        response = requests.get('https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json')
        if response.status_code == 200:
            provinces = response.json()
            print(f"✅ Successfully retrieved data for {len(provinces)} provinces")
            print("✅ First 5 provinces:")
            for i, province in enumerate(provinces[:5]):
                print(f"   {i+1}. {province['name']}")
        else:
            print(f"❌ Error: Status code {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Example 2: Weather API Simulation for Jakarta
    print("\n2.2 Jakarta Weather API Simulation")
    def get_simulated_weather(city="Jakarta"):
        """Weather API simulation for learning"""
        weather_data = {
            "city": city,
            "temperature": 28.5,
            "humidity": 75,
            "condition": "Partly Cloudy",
            "wind_speed": 12.3,
            "timestamp": datetime.now().isoformat()
        }
        return weather_data
    
    weather = get_simulated_weather("Jakarta")
    print(f"✅ Weather in {weather['city']}: {weather['temperature']}°C")
    print(f"✅ Condition: {weather['condition']}")
    print(f"✅ Humidity: {weather['humidity']}%")
    
    # Example 3: API with Error Handling
    print("\n2.3 Error Handling for API Calls")
    def safe_api_call(url, max_retries=3):
        """API call with retry mechanism"""
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"⚠️ Attempt {attempt + 1}: Status {response.status_code}")
            except requests.exceptions.Timeout:
                print(f"⚠️ Attempt {attempt + 1}: Timeout")
            except requests.exceptions.ConnectionError:
                print(f"⚠️ Attempt {attempt + 1}: Connection Error")
            
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
        
        return None
    
    # Test safe API call
    result = safe_api_call('https://httpbin.org/delay/1')
    if result:
        print("✅ Safe API call successful")
    else:
        print("❌ Safe API call failed after multiple attempts")
    
    print("\n💡 Key Learning Points:")
    print("- APIs return data in JSON format")
    print("- Always check status code before processing data")
    print("- Implement retry mechanism for reliability")
    print("- Use timeout to avoid hanging requests")

# =============================================================================
# STEP 3: INTRODUCTION TO WEB SCRAPING
# =============================================================================

print("\n📚 STEP 3: INTRODUCTION TO WEB SCRAPING")
print("-" * 40)

def step3_web_scraping_basics():
    """
    Step 3: Web scraping basics with BeautifulSoup
    """
    print("🎯 Objective: Extracting data from web pages")
    print("📖 Concepts: HTML parsing, CSS selectors, BeautifulSoup")
    
    # Example 1: Simple HTML parsing
    print("\n3.1 Simple HTML Parsing")
    sample_html = """
    <html>
        <head><title>Indonesian News Today</title></head>
        <body>
            <h1>Indonesian News Portal</h1>
            <div class="news-container">
                <article class="news-item">
                    <h2>Indonesian Economy Shows Positive Growth</h2>
                    <p class="summary">Indonesian economic growth reached 5.2% in Q3</p>
                    <span class="date">2024-01-15</span>
                </article>
                <article class="news-item">
                    <h2>Indonesian Tech Startups Flourish</h2>
                    <p class="summary">Indonesian startup investment reached record high</p>
                    <span class="date">2024-01-14</span>
                </article>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(sample_html, 'html.parser')
    
    # Extract title
    title = soup.find('title').text
    print(f"✅ Page title: {title}")
    
    # Extract all news items
    news_items = soup.find_all('article', class_='news-item')
    print(f"✅ Found {len(news_items)} news items:")
    
    for i, item in enumerate(news_items, 1):
        headline = item.find('h2').text
        summary = item.find('p', class_='summary').text
        date = item.find('span', class_='date').text
        print(f"   {i}. {headline}")
        print(f"      Summary: {summary}")
        print(f"      Date: {date}")
    
    # Example 2: CSS Selectors
    print("\n3.2 Using CSS Selectors")
    
    # Select by class
    summaries = soup.select('.summary')
    print(f"✅ News summaries using CSS selector:")
    for i, summary in enumerate(summaries, 1):
        print(f"   {i}. {summary.text}")
    
    # Select by attribute
    dates = soup.select('span[class="date"]')
    print(f"✅ News dates: {[date.text for date in dates]}")
    
    # Example 3: Scraping with requests + BeautifulSoup
    print("\n3.3 Real Web Scraping (Simulation)")
    
    def scrape_quotes_simulation():
        """Quote scraping simulation for learning"""
        quotes_data = [
            {
                "text": "Independence can only be maintained by a free people",
                "author": "Soekarno",
                "tags": ["independence", "freedom", "indonesia"]
            },
            {
                "text": "A great nation is one that honors the services of its heroes",
                "author": "Soekarno", 
                "tags": ["nation", "heroes", "history"]
            },
            {
                "text": "Never abandon history",
                "author": "Soekarno",
                "tags": ["history", "learning", "future"]
            }
        ]
        return quotes_data
    
    quotes = scrape_quotes_simulation()
    print(f"✅ Successfully scraped {len(quotes)} quotes:")
    for i, quote in enumerate(quotes, 1):
        print(f"   {i}. \"{quote['text']}\" - {quote['author']}")
        print(f"      Tags: {', '.join(quote['tags'])}")
    
    print("\n💡 Key Learning Points:")
    print("- BeautifulSoup simplifies HTML parsing")
    print("- find() for single element, find_all() for multiple elements")
    print("- CSS selectors provide flexibility in element selection")
    print("- Always inspect HTML structure before scraping")

# =============================================================================
# STEP 4: ADVANCED SCRAPING TECHNIQUES
# =============================================================================

print("\n📚 STEP 4: ADVANCED SCRAPING TECHNIQUES")
print("-" * 40)

def step4_advanced_scraping():
    """
    Step 4: Advanced scraping techniques for Indonesian websites
    """
    print("🎯 Objective: Mastering scraping techniques for complex websites")
    print("📖 Concepts: Sessions, Cookies, Forms, Headers, Rate Limiting")
    
    # Example 1: Using Sessions
    print("\n4.1 Using Sessions for Scraping")
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    })
    
    print("✅ Session created with Indonesian-friendly headers")
    print(f"✅ User-Agent: {session.headers['User-Agent'][:50]}...")
    
    # Example 2: Rate Limiting and Politeness
    print("\n4.2 Rate Limiting Implementation")
    
    class PoliteWebScraper:
        def __init__(self, delay=1.0):
            self.delay = delay
            self.last_request_time = 0
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Indonesian-Student-Bot/1.0 (Educational Purpose)'
            })
        
        def polite_get(self, url):
            """GET request with rate limiting"""
            current_time = time.time()
            time_since_last = current_time - self.last_request_time
            
            if time_since_last < self.delay:
                sleep_time = self.delay - time_since_last
                print(f"⏳ Waiting {sleep_time:.1f} seconds for politeness...")
                time.sleep(sleep_time)
            
            try:
                response = self.session.get(url)
                self.last_request_time = time.time()
                return response
            except Exception as e:
                print(f"❌ Error: {e}")
                return None
    
    scraper = PoliteWebScraper(delay=2.0)
    print("✅ Polite scraper created with 2 second delay")
    
    # Example 3: Handling Different Content Types
    print("\n4.3 Handling Various Content Types")
    
    def extract_indonesian_ecommerce_data(html_content):
        """Indonesian e-commerce data extraction simulation"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Product data simulation
        products = [
            {
                'name': 'Smartphone Samsung Galaxy A54',
                'price': 'Rp 5.999.000',
                'rating': 4.5,
                'sold': 1250,
                'location': 'Jakarta Barat'
            },
            {
                'name': 'Nike Air Max Shoes',
                'price': 'Rp 1.899.000', 
                'rating': 4.7,
                'sold': 890,
                'location': 'Bandung'
            }
        ]
        
        return products
    
    # E-commerce HTML simulation
    sample_ecommerce_html = "<html><body>Sample e-commerce page</body></html>"
    products = extract_indonesian_ecommerce_data(sample_ecommerce_html)
    
    print(f"✅ Successfully extracted {len(products)} products:")
    for product in products:
        print(f"   📱 {product['name']}")
        print(f"      💰 {product['price']} | ⭐ {product['rating']} | 🛒 {product['sold']} sold")
        print(f"      📍 {product['location']}")
    
    print("\n💡 Key Learning Points:")
    print("- Use sessions to maintain cookies and connections")
    print("- Implement rate limiting to respect servers")
    print("- Set appropriate headers to avoid blocking")
    print("- Always test scraping code with small data first")

# =============================================================================
# STEP 5: DATA PROCESSING AND STORAGE
# =============================================================================

print("\n📚 STEP 5: DATA PROCESSING AND STORAGE")
print("-" * 40)

def step5_data_processing():
    """
    Step 5: Processing and storing collected Indonesian data
    """
    print("🎯 Objective: Cleaning, processing, and storing data")
    print("📖 Concepts: Data cleaning, pandas, CSV, JSON, database")
    
    # Example 1: Data Cleaning for Indonesian data
    print("\n5.1 Cleaning Indonesian Data")
    
    # Raw data with common issues
    raw_indonesian_data = [
        {'city': '  Jakarta  ', 'population': '10,560,000', 'province': 'DKI Jakarta'},
        {'city': 'Surabaya', 'population': '2.874.000', 'province': 'Jawa Timur'},
        {'city': 'BANDUNG', 'population': '2,452,943', 'province': 'jawa barat'},
        {'city': 'Medan', 'population': '2.210.624', 'province': 'Sumatera Utara'},
        {'city': '', 'population': 'N/A', 'province': 'Unknown'}  # Dirty data
    ]
    
    def clean_indonesian_city_data(data):
        """Clean Indonesian city data"""
        cleaned_data = []
        
        for item in data:
            # Skip empty data
            if not item['city'] or item['city'].strip() == '':
                continue
                
            # Clean city name
            city = item['city'].strip().title()
            
            # Clean population (remove commas, dots, convert to int)
            pop_str = item['population'].replace(',', '').replace('.', '')
            try:
                population = int(pop_str) if pop_str.isdigit() else 0
            except:
                population = 0
            
            # Clean province name
            province = item['province'].strip().title()
            
            if population > 0:  # Only include valid data
                cleaned_data.append({
                    'city': city,
                    'population': population,
                    'province': province
                })
        
        return cleaned_data
    
    cleaned_cities = clean_indonesian_city_data(raw_indonesian_data)
    print(f"✅ Data cleaned: {len(raw_indonesian_data)} → {len(cleaned_cities)} records")
    
    for city in cleaned_cities:
        print(f"   🏙️ {city['city']}: {city['population']:,} people ({city['province']})")
    
    # Example 2: Using Pandas for analysis
    print("\n5.2 Data Analysis with Pandas")
    
    df = pd.DataFrame(cleaned_cities)
    print("✅ DataFrame created:")
    print(df.to_string(index=False))
    
    # Basic statistics
    print(f"\n📊 Population Statistics:")
    print(f"   Total population: {df['population'].sum():,} people")
    print(f"   Average: {df['population'].mean():,.0f} people")
    print(f"   Largest city: {df.loc[df['population'].idxmax(), 'city']}")
    
    # Example 3: Saving data in various formats
    print("\n5.3 Saving Data in Various Formats")
    
    # Save as CSV
    df.to_csv('indonesian_cities.csv', index=False, encoding='utf-8')
    print("✅ Data saved as CSV: indonesian_cities.csv")
    
    # Save as JSON
    with open('indonesian_cities.json', 'w', encoding='utf-8') as f:
        json.dump(cleaned_cities, f, ensure_ascii=False, indent=2)
    print("✅ Data saved as JSON: indonesian_cities.json")
    
    # Save as Excel (if openpyxl is available)
    try:
        df.to_excel('indonesian_cities.xlsx', index=False, engine='openpyxl')
        print("✅ Data saved as Excel: indonesian_cities.xlsx")
    except ImportError:
        print("⚠️ Excel export not available (install openpyxl)")
    
    print("\n💡 Key Learning Points:")
    print("- Always clean data before analysis")
    print("- Pandas is very powerful for data manipulation")
    print("- Save data in multiple formats for flexibility")
    print("- Use encoding='utf-8' for Indonesian characters")

# =============================================================================
# STEP 6: ERROR HANDLING AND BEST PRACTICES
# =============================================================================

print("\n📚 STEP 6: ERROR HANDLING AND BEST PRACTICES")
print("-" * 40)

def step6_error_handling():
    """
    Step 6: Implementing error handling and best practices
    """
    print("🎯 Objective: Creating robust and reliable scrapers")
    print("📖 Concepts: Exception handling, logging, retry mechanisms")
    
    # Example 1: Comprehensive Error Handling
    print("\n6.1 Comprehensive Error Handling")
    
    class RobustIndonesianScraper:
        def __init__(self):
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Indonesian-Educational-Bot/1.0'
            })
            self.errors = []
        
        def scrape_with_error_handling(self, url, max_retries=3):
            """Scraping with comprehensive error handling"""
            for attempt in range(max_retries):
                try:
                    print(f"🔄 Attempt {attempt + 1} for {url}")
                    
                    response = self.session.get(url, timeout=10)
                    
                    if response.status_code == 200:
                        print(f"✅ Successfully accessed {url}")
                        return response
                    
                    elif response.status_code == 429:
                        print("⚠️ Rate limited, waiting longer...")
                        time.sleep(60)  # Wait 1 minute for rate limit
                        continue
                    
                    elif response.status_code == 404:
                        print("❌ Page not found (404)")
                        self.errors.append(f"404 error for {url}")
                        return None
                    
                    else:
                        print(f"⚠️ Unexpected status code: {response.status_code}")
                        
                except requests.exceptions.Timeout:
                    print(f"⏰ Timeout on attempt {attempt + 1}")
                    self.errors.append(f"Timeout for {url} on attempt {attempt + 1}")
                    
                except requests.exceptions.ConnectionError:
                    print(f"🔌 Connection error on attempt {attempt + 1}")
                    self.errors.append(f"Connection error for {url} on attempt {attempt + 1}")
                    
                except Exception as e:
                    print(f"❌ Unexpected error: {str(e)}")
                    self.errors.append(f"Unexpected error for {url}: {str(e)}")
                
                # Exponential backoff
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"⏳ Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
            
            print(f"❌ Failed to access {url} after {max_retries} attempts")
            return None
        
        def get_error_summary(self):
            """Get error summary"""
            return {
                'total_errors': len(self.errors),
                'errors': self.errors
            }
    
    # Test robust scraper
    scraper = RobustIndonesianScraper()
    
    # Test with valid URL
    result = scraper.scrape_with_error_handling('https://httpbin.org/status/200')
    
    # Test with URL that will timeout
    result = scraper.scrape_with_error_handling('https://httpbin.org/delay/15')
    
    # Print error summary
    error_summary = scraper.get_error_summary()
    print(f"\n📋 Error Summary: {error_summary['total_errors']} errors")
    for error in error_summary['errors']:
        print(f"   ❌ {error}")
    
    # Example 2: Data Validation
    print("\n6.2 Indonesian Data Validation")
    
    def validate_indonesian_data(data):
        """Validate Indonesian data"""
        validation_errors = []
        
        # List of valid Indonesian provinces
        valid_provinces = [
            'Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Jambi',
            'Sumatera Selatan', 'Bengkulu', 'Lampung', 'Kepulauan Bangka Belitung',
            'Kepulauan Riau', 'DKI Jakarta', 'Jawa Barat', 'Jawa Tengah',
            'DI Yogyakarta', 'Jawa Timur', 'Banten', 'Bali', 'Nusa Tenggara Barat',
            'Nusa Tenggara Timur', 'Kalimantan Barat', 'Kalimantan Tengah',
            'Kalimantan Selatan', 'Kalimantan Timur', 'Kalimantan Utara',
            'Sulawesi Utara', 'Sulawesi Tengah', 'Sulawesi Selatan',
            'Sulawesi Tenggara', 'Gorontalo', 'Sulawesi Barat', 'Maluku',
            'Maluku Utara', 'Papua Barat', 'Papua'
        ]
        
        for i, item in enumerate(data):
            # Validate city name
            if not item.get('city') or len(item['city']) < 2:
                validation_errors.append(f"Row {i}: Invalid city name")
            
            # Validate population
            if not isinstance(item.get('population'), int) or item['population'] < 0:
                validation_errors.append(f"Row {i}: Invalid population")
            
            # Validate province
            if item.get('province') not in valid_provinces:
                validation_errors.append(f"Row {i}: Invalid province '{item.get('province')}'")
        
        return validation_errors
    
    # Test validation
    test_data = [
        {'city': 'Jakarta', 'population': 10560000, 'province': 'DKI Jakarta'},
        {'city': '', 'population': -100, 'province': 'Invalid Province'},  # Invalid data
        {'city': 'Surabaya', 'population': 2874000, 'province': 'Jawa Timur'}
    ]
    
    errors = validate_indonesian_data(test_data)
    print(f"✅ Validation complete: {len(errors)} errors found")
    for error in errors:
        print(f"   ❌ {error}")
    
    print("\n💡 Key Learning Points:")
    print("- Always implement comprehensive error handling")
    print("- Use retry mechanisms with exponential backoff")
    print("- Validate data before saving or processing")
    print("- Log all errors for debugging")

# =============================================================================
# STEP 7: COMBINING MULTIPLE DATA SOURCES
# =============================================================================

print("\n📚 STEP 7: COMBINING MULTIPLE DATA SOURCES")
print("-" * 40)

def step7_combining_data_sources():
    """
    Step 7: Combining data from APIs and web scraping
    """
    print("🎯 Objective: Integrating data from various sources")
    print("📖 Concepts: Data integration, correlation, enrichment")
    
    # Example 1: Combining API and Scraping Data
    print("\n7.1 Combining API and Scraping Data")
    
    class IndonesianDataIntegrator:
        def __init__(self):
            self.api_data = {}
            self.scraped_data = {}
            self.integrated_data = {}
        
        def fetch_api_data(self):
            """Simulate fetching data from API"""
            # Simulate weather data from API
            self.api_data = {
                'weather': [
                    {'city': 'Jakarta', 'temperature': 28, 'humidity': 75},
                    {'city': 'Surabaya', 'temperature': 30, 'humidity': 70},
                    {'city': 'Bandung', 'temperature': 24, 'humidity': 80}
                ]
            }
            print(f"✅ API data: {len(self.api_data['weather'])} weather records")
        
        def fetch_scraped_data(self):
            """Simulate data from web scraping"""
            # Simulate population data from scraping
            self.scraped_data = {
                'population': [
                    {'city': 'Jakarta', 'population': 10560000, 'area_km2': 664},
                    {'city': 'Surabaya', 'population': 2874000, 'area_km2': 350},
                    {'city': 'Bandung', 'population': 2453000, 'area_km2': 167}
                ]
            }
            print(f"✅ Scraped data: {len(self.scraped_data['population'])} city records")
        
        def integrate_data(self):
            """Combine data based on city name"""
            # Convert to DataFrames for easier merging
            weather_df = pd.DataFrame(self.api_data['weather'])
            population_df = pd.DataFrame(self.scraped_data['population'])
            
            # Merge data based on city
            integrated_df = pd.merge(weather_df, population_df, on='city', how='inner')
            
            # Add calculated fields
            integrated_df['population_density'] = integrated_df['population'] / integrated_df['area_km2']
            integrated_df['comfort_index'] = (100 - integrated_df['humidity']) * 0.5 + (30 - abs(integrated_df['temperature'] - 25)) * 0.5
            
            self.integrated_data = integrated_df.to_dict('records')
            print(f"✅ Data integrated: {len(self.integrated_data)} complete records")
            
            return integrated_df
    
    # Test integration
    integrator = IndonesianDataIntegrator()
    integrator.fetch_api_data()
    integrator.fetch_scraped_data()
    df = integrator.integrate_data()
    
    print("\n📊 Integrated Data:")
    print(df.to_string(index=False))
    
    # Example 2: Data Enrichment
    print("\n7.2 Data Enrichment with Multiple Sources")
    
    def enrich_indonesian_city_data(base_data):
        """Enrich city data with additional information"""
        
        # Additional data sources (simulated)
        economic_data = {
            'Jakarta': {'gdp_per_capita': 15000, 'unemployment_rate': 5.2},
            'Surabaya': {'gdp_per_capita': 12000, 'unemployment_rate': 4.8},
            'Bandung': {'gdp_per_capita': 10000, 'unemployment_rate': 6.1}
        }
        
        tourism_data = {
            'Jakarta': {'tourist_attractions': 25, 'hotels': 450},
            'Surabaya': {'tourist_attractions': 18, 'hotels': 280},
            'Bandung': {'tourist_attractions': 30, 'hotels': 320}
        }
        
        enriched_data = []
        
        for city_data in base_data:
            city_name = city_data['city']
            
            # Start with base data
            enriched_record = city_data.copy()
            
            # Add economic data
            if city_name in economic_data:
                enriched_record.update(economic_data[city_name])
            
            # Add tourism data
            if city_name in tourism_data:
                enriched_record.update(tourism_data[city_name])
            
            # Calculate composite scores
            if 'gdp_per_capita' in enriched_record and 'unemployment_rate' in enriched_record:
                economic_score = (enriched_record['gdp_per_capita'] / 1000) * (10 - enriched_record['unemployment_rate'])
                enriched_record['economic_score'] = round(economic_score, 2)
            
            enriched_data.append(enriched_record)
        
        return enriched_data
    
    # Enrich the integrated data
    enriched_cities = enrich_indonesian_city_data(integrator.integrated_data)
    
    print("✅ Data enriched with economic and tourism information:")
    for city in enriched_cities:
        print(f"\n🏙️ {city['city']}:")
        print(f"   👥 Population: {city['population']:,} people")
        print(f"   🌡️ Temperature: {city['temperature']}°C")
        print(f"   💰 GDP per capita: ${city.get('gdp_per_capita', 'N/A'):,}")
        print(f"   🏨 Hotels: {city.get('hotels', 'N/A')} units")
        print(f"   📊 Economic Score: {city.get('economic_score', 'N/A')}")
    
    # Example 3: Save Final Integrated Dataset
    print("\n7.3 Saving Final Dataset")
    
    final_df = pd.DataFrame(enriched_cities)
    
    # Save in multiple formats
    final_df.to_csv('indonesian_cities_integrated.csv', index=False, encoding='utf-8')
    final_df.to_json('indonesian_cities_integrated.json', orient='records', indent=2)
    
    print("✅ Final dataset saved:")
    print("   📄 indonesian_cities_integrated.csv")
    print("   📄 indonesian_cities_integrated.json")
    
    # Generate summary statistics
    print(f"\n📈 Final Dataset Summary:")
    print(f"   🏙️ Total cities: {len(final_df)}")
    print(f"   👥 Total population: {final_df['population'].sum():,} people")
    print(f"   🌡️ Average temperature: {final_df['temperature'].mean():.1f}°C")
    print(f"   💰 Average GDP per capita: ${final_df['gdp_per_capita'].mean():,.0f}")
    
    print("\n💡 Key Learning Points:")
    print("- Combine data from multiple sources for richer insights")
    print("- Use common fields (like city name) as keys for merging")
    print("- Enrich data with calculated fields and composite scores")
    print("- Always save final dataset in multiple formats")

# =============================================================================
# MAIN EXECUTION - MENJALANKAN SEMUA STEPS
# =============================================================================

def main():
    """
    Main function to run all learning steps
    """
    print("🚀 STARTING WEB SCRAPING AND API LEARNING")
    print("This guide will teach you step by step")
    print("from basic concepts to advanced techniques.\n")
    
    try:
        # Execute all steps
        step1_basic_http_requests()
        input("\n⏸️ Press Enter to continue to Step 2...")
        
        step2_working_with_apis()
        input("\n⏸️ Press Enter to continue to Step 3...")
        
        step3_web_scraping_basics()
        input("\n⏸️ Press Enter to continue to Step 4...")
        
        step4_advanced_scraping()
        input("\n⏸️ Press Enter to continue to Step 5...")
        
        step5_data_processing()
        input("\n⏸️ Press Enter to continue to Step 6...")
        
        step6_error_handling()
        input("\n⏸️ Press Enter to continue to Step 7...")
        
        step7_combining_data_sources()
        
        print("\n" + "="*60)
        print("🎉 CONGRATULATIONS! YOU HAVE COMPLETED ALL STEPS!")
        print("="*60)
        print("\n📚 What you have learned:")
        print("✅ HTTP requests and response handling")
        print("✅ Working with REST APIs")
        print("✅ Web scraping with BeautifulSoup")
        print("✅ Advanced scraping techniques")
        print("✅ Data processing and cleaning")
        print("✅ Error handling and best practices")
        print("✅ Integrating multiple data sources")
        
        print("\n🚀 Next you can:")
        print("- Scrape Indonesian websites for AI projects")
        print("- Use APIs for real-time data")
        print("- Build datasets for machine learning")
        print("- Create Indonesian data dashboards")
        print("- Automate data collection")
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Learning stopped by user")
    except Exception as e:
        print(f"\n❌ Error in learning: {str(e)}")
        print("💡 Please try running again or check internet connection")

if __name__ == "__main__":
    main() 