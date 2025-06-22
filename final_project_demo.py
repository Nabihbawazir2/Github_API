#!/usr/bin/env python3
"""
Final Project Demo: Indonesian Data Collection Showcase
======================================================

This file demonstrates what students can achieve after completing the lesson on
"How to Gather Data for Your AI Projects: Web Scraping and APIs"

Indonesian Focus Areas:
- Indonesian news headlines
- Jakarta weather data
- Indonesian stock market data
- Indonesian e-commerce product data
- Indonesian government open data

Author: AI Engineering Course
Date: 2024
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Set up Indonesian locale for better display
plt.rcParams['font.family'] = 'DejaVu Sans'

class IndonesianDataCollector:
    """
    A comprehensive data collector for Indonesian sources
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.collected_data = {}
    
    def get_jakarta_weather(self):
        """
        Collect current weather data for Jakarta using OpenWeatherMap API
        """
        print("🌤️  Collecting Jakarta weather data...")
        
        # Note: In real implementation, you would use your own API key
        api_key = "YOUR_API_KEY_HERE"
        city = "Jakarta"
        
        # Simulated weather data for demo purposes
        weather_data = {
            'city': 'Jakarta',
            'temperature': 28.5,
            'humidity': 75,
            'description': 'Partly Cloudy',
            'wind_speed': 12.5,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.collected_data['weather'] = weather_data
        print(f"✅ Jakarta weather data collected successfully: {weather_data['temperature']}°C")
        return weather_data
    
    def scrape_indonesian_news(self):
        """
        Scrape Indonesian news headlines (simulated for demo)
        """
        print("📰 Collecting latest Indonesian news...")
        
        # Simulated news data for demo purposes
        news_data = [
            {
                'title': 'Indonesian Economy Grows 5.2% in Q3 2024',
                'category': 'Economy',
                'timestamp': '2024-01-15 10:30:00',
                'source': 'Kompas'
            },
            {
                'title': 'IKN Nusantara Project Enters Infrastructure Development Phase',
                'category': 'Politics',
                'timestamp': '2024-01-15 09:15:00',
                'source': 'Detik'
            },
            {
                'title': 'Indonesian Startup Raises $50 Million Series A Funding',
                'category': 'Technology',
                'timestamp': '2024-01-15 08:45:00',
                'source': 'Tempo'
            },
            {
                'title': 'Indonesian National Team Advances to Asian Cup Semifinals',
                'category': 'Sports',
                'timestamp': '2024-01-14 22:30:00',
                'source': 'Tribun'
            },
            {
                'title': 'Rice Prices Stable in Jakarta Traditional Markets',
                'category': 'Economy',
                'timestamp': '2024-01-14 16:20:00',
                'source': 'CNN Indonesia'
            }
        ]
        
        self.collected_data['news'] = news_data
        print(f"✅ Successfully collected {len(news_data)} latest news articles")
        return news_data
    
    def get_indonesian_stock_data(self):
        """
        Collect Indonesian stock market data (simulated)
        """
        print("📈 Collecting Indonesian stock market data (IHSG)...")
        
        # Simulated stock data for major Indonesian companies
        stock_data = [
            {'symbol': 'BBCA', 'name': 'Bank Central Asia', 'price': 8500, 'change': '+2.5%'},
            {'symbol': 'BBRI', 'name': 'Bank Rakyat Indonesia', 'price': 4200, 'change': '+1.8%'},
            {'symbol': 'BMRI', 'name': 'Bank Mandiri', 'price': 5800, 'change': '-0.5%'},
            {'symbol': 'TLKM', 'name': 'Telkom Indonesia', 'price': 3150, 'change': '+3.2%'},
            {'symbol': 'ASII', 'name': 'Astra International', 'price': 6200, 'change': '+1.1%'},
            {'symbol': 'UNVR', 'name': 'Unilever Indonesia', 'price': 3800, 'change': '-1.2%'},
            {'symbol': 'ICBP', 'name': 'Indofood CBP', 'price': 9500, 'change': '+0.8%'},
            {'symbol': 'GGRM', 'name': 'Gudang Garam', 'price': 25000, 'change': '+2.1%'}
        ]
        
        self.collected_data['stocks'] = stock_data
        print(f"✅ Successfully collected stock data for {len(stock_data)} Indonesian companies")
        return stock_data
    
    def scrape_ecommerce_products(self):
        """
        Scrape Indonesian e-commerce product data (simulated)
        """
        print("🛒 Collecting Indonesian e-commerce product data...")
        
        # Simulated product data from Indonesian e-commerce
        products_data = [
            {
                'name': 'Smartphone Samsung Galaxy A54 5G',
                'price': 5999000,
                'rating': 4.5,
                'sold': 1250,
                'category': 'Electronics',
                'seller_location': 'Jakarta'
            },
            {
                'name': 'Nike Air Max 270 Shoes',
                'price': 1899000,
                'rating': 4.7,
                'sold': 890,
                'category': 'Fashion',
                'seller_location': 'Bandung'
            },
            {
                'name': 'ASUS VivoBook 14 Laptop',
                'price': 7500000,
                'rating': 4.3,
                'sold': 456,
                'category': 'Computer',
                'seller_location': 'Surabaya'
            },
            {
                'name': 'Eiger 1989 Backpack',
                'price': 350000,
                'rating': 4.6,
                'sold': 2100,
                'category': 'Fashion',
                'seller_location': 'Yogyakarta'
            },
            {
                'name': 'Aceh Gayo Arabica Coffee',
                'price': 85000,
                'rating': 4.8,
                'sold': 3400,
                'category': 'Food',
                'seller_location': 'Aceh'
            }
        ]
        
        self.collected_data['products'] = products_data
        print(f"✅ Successfully collected {len(products_data)} e-commerce product data")
        return products_data
    
    def get_government_open_data(self):
        """
        Access Indonesian government open data (simulated)
        """
        print("🏛️  Accessing Indonesian government open data...")
        
        # Simulated government data
        gov_data = {
            'population_by_province': [
                {'province': 'West Java', 'population': 48037000, 'area_km2': 35378},
                {'province': 'East Java', 'population': 39293000, 'area_km2': 47800},
                {'province': 'Central Java', 'population': 34257000, 'area_km2': 32801},
                {'province': 'North Sumatra', 'population': 14799000, 'area_km2': 72981},
                {'province': 'DKI Jakarta', 'population': 10562000, 'area_km2': 664}
            ],
            'gdp_by_sector': [
                {'sector': 'Manufacturing Industry', 'contribution_percent': 19.7},
                {'sector': 'Trade', 'contribution_percent': 13.2},
                {'sector': 'Agriculture', 'contribution_percent': 12.9},
                {'sector': 'Construction', 'contribution_percent': 10.9},
                {'sector': 'Mining', 'contribution_percent': 8.4}
            ]
        }
        
        self.collected_data['government'] = gov_data
        print("✅ Government open data accessed successfully")
        return gov_data
    
    def create_data_visualizations(self):
        """
        Create visualizations from collected Indonesian data
        """
        print("📊 Creating Indonesian data visualizations...")
        
        # Create a figure with multiple subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Indonesian Data Dashboard', fontsize=16, fontweight='bold')
        
        # 1. News categories pie chart
        if 'news' in self.collected_data:
            news_df = pd.DataFrame(self.collected_data['news'])
            category_counts = news_df['category'].value_counts()
            
            axes[0, 0].pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%')
            axes[0, 0].set_title('News Category Distribution')
        
        # 2. Stock prices bar chart
        if 'stocks' in self.collected_data:
            stocks_df = pd.DataFrame(self.collected_data['stocks'])
            
            axes[0, 1].bar(stocks_df['symbol'], stocks_df['price'])
            axes[0, 1].set_title('Indonesian Company Stock Prices')
            axes[0, 1].set_xlabel('Stock Symbol')
            axes[0, 1].set_ylabel('Price (IDR)')
            axes[0, 1].tick_params(axis='x', rotation=45)
        
        # 3. E-commerce product ratings
        if 'products' in self.collected_data:
            products_df = pd.DataFrame(self.collected_data['products'])
            
            axes[1, 0].scatter(products_df['price'], products_df['rating'], 
                             s=products_df['sold']/10, alpha=0.6)
            axes[1, 0].set_title('E-commerce Product Price vs Rating')
            axes[1, 0].set_xlabel('Price (IDR)')
            axes[1, 0].set_ylabel('Rating')
        
        # 4. Population by province
        if 'government' in self.collected_data:
            pop_data = self.collected_data['government']['population_by_province']
            pop_df = pd.DataFrame(pop_data)
            
            axes[1, 1].barh(pop_df['province'], pop_df['population']/1000000)
            axes[1, 1].set_title('Population by Province (Millions)')
            axes[1, 1].set_xlabel('Population (Millions)')
        
        plt.tight_layout()
        plt.savefig('indonesian_data_dashboard.png', dpi=300, bbox_inches='tight')
        print("✅ Dashboard visualization saved as 'indonesian_data_dashboard.png'")
        
        return fig
    
    def save_collected_data(self):
        """
        Save all collected data to files
        """
        print("💾 Saving all collected data...")
        
        # Save as JSON
        with open('indonesian_data_collection.json', 'w', encoding='utf-8') as f:
            json.dump(self.collected_data, f, ensure_ascii=False, indent=2)
        
        # Save as CSV files
        for data_type, data in self.collected_data.items():
            if isinstance(data, list):
                df = pd.DataFrame(data)
                df.to_csv(f'indonesian_{data_type}_data.csv', index=False, encoding='utf-8')
        
        print("✅ All data saved in JSON and CSV formats")
    
    def generate_summary_report(self):
        """
        Generate a comprehensive summary report
        """
        print("\n" + "="*60)
        print("📋 INDONESIAN DATA COLLECTION SUMMARY REPORT")
        print("="*60)
        
        total_data_points = 0
        
        for data_type, data in self.collected_data.items():
            if isinstance(data, list):
                count = len(data)
                total_data_points += count
                print(f"📊 {data_type.capitalize()}: {count} data points")
            elif isinstance(data, dict):
                if 'population_by_province' in data:
                    count = len(data['population_by_province'])
                    total_data_points += count
                    print(f"📊 {data_type.capitalize()}: {count} data points")
                else:
                    total_data_points += 1
                    print(f"📊 {data_type.capitalize()}: 1 data point")
        
        print(f"\n🎯 Total data points collected: {total_data_points}")
        print(f"📅 Collection time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌏 Geographic focus: Indonesia")
        
        print("\n📈 SKILLS MASTERED:")
        print("✅ Web scraping to collect data from websites")
        print("✅ Using APIs to access real-time data")
        print("✅ Combining multiple data sources")
        print("✅ Cleaning and processing data")
        print("✅ Data visualization with matplotlib")
        print("✅ Saving data in various formats")
        print("✅ Creating automated reports")
        
        return total_data_points


def main():
    """
    Main function to demonstrate the complete Indonesian data collection workflow
    """
    print("🇮🇩 INDONESIAN DATA COLLECTION DEMO FOR AI")
    print("=" * 50)
    print("Welcome to the Indonesian data collection demo!")
    print("This demo shows the final results of today's learning.\n")
    
    # Initialize the data collector
    collector = IndonesianDataCollector()
    
    try:
        # Collect data from various Indonesian sources
        collector.get_jakarta_weather()
        time.sleep(1)  # Simulate API delay
        
        collector.scrape_indonesian_news()
        time.sleep(1)
        
        collector.get_indonesian_stock_data()
        time.sleep(1)
        
        collector.scrape_ecommerce_products()
        time.sleep(1)
        
        collector.get_government_open_data()
        time.sleep(1)
        
        # Create visualizations
        collector.create_data_visualizations()
        
        # Save all data
        collector.save_collected_data()
        
        # Generate summary report
        total_points = collector.generate_summary_report()
        
        print(f"\n🎉 CONGRATULATIONS! You have successfully collected {total_points} data points")
        print("from various Indonesian sources using web scraping and APIs!")
        
        print("\n📁 Generated files:")
        print("- indonesian_data_collection.json")
        print("- indonesian_news_data.csv")
        print("- indonesian_stocks_data.csv") 
        print("- indonesian_products_data.csv")
        print("- indonesian_data_dashboard.png")
        
        print("\n🚀 Next, this data is ready to be used for:")
        print("- Machine Learning models")
        print("- Data analysis and insights")
        print("- Business intelligence")
        print("- Predictive analytics")
        print("- AI applications")
        
    except Exception as e:
        print(f"❌ Error in data collection: {str(e)}")
        print("💡 Tip: Ensure stable internet connection and valid API keys")


if __name__ == "__main__":
    main() 