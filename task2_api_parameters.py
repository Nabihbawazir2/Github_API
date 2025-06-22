import requests

class IndonesianCityAPI:
    def __init__(self):
        self.base_url = "https://www.emsifa.com/api-wilayah-indonesia/api"
        self.headers = {
            "User-Agent": "CitySearchApp/1.0 (+https://yourdomain.com)"
        }

    def get_cities_by_province_id(self, province_id):
        """
        Get all cities in a specific province by its ID.
        Returns a list of city dictionaries.
        """
        url = f"{self.base_url}/regencies/{province_id}.json"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            cities = response.json()
            print(f"Total cities in province {province_id}: {len(cities)}")
            return cities
        else:
            print(f"Failed to fetch cities for province ID {province_id}. Status code: {response.status_code}")
            return []

    def search_city_by_name(self, city_name):
        """
        Search for a city by name across all provinces.
        Performs a case-insensitive match.
        """
        matches = []
        for prov_id in range(11, 95):  # ID range from Aceh (11) to Papua (94)
            cities = self.get_cities_by_province_id(str(prov_id))
            for city in cities:
                if city_name.lower() in city['name'].lower():
                    matches.append({
                        'province_id': prov_id,
                        'city_id': city['id'],
                        'city_name': city['name']
                    })
        print(f"\nFound {len(matches)} city(ies) matching '{city_name}':")
        for match in matches:
            print(f"- {match['city_name']} (Province ID: {match['province_id']}, City ID: {match['city_id']})")
        return matches


if __name__ == "__main__":
    api = IndonesianCityAPI()

    # Get all cities in West Java (province ID: 32)
    print("Fetching cities in West Java (ID: 32)...")
    west_java_cities = api.get_cities_by_province_id("32")

    # Search for "Bandung"
    print("\nSearching for cities with name containing 'Bandung'...")
    bandung_matches = api.search_city_by_name("Bandung")
