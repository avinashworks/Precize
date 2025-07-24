import json
from serpapi import GoogleSearch  # Install with: pip install google-search-results

def get_top_restaurants(city, num_results=10):
    """
    Retrieves the top restaurants in the specified city using SerpApi.

    Args:
        city (str): Name of the city.
        num_results (int): Number of top restaurants to retrieve.

    Returns:
        dict: Dictionary containing restaurant names as keys and their details as values.
    """
    API_KEY = 'YOUR_SERPAPI_KEY'  # Replace with your SerpApi API key

    params = {
        "engine": "google_food",
        "q": f"top restaurants in {city}",
        "api_key": API_KEY,
        "hl": "en",
        "num": num_results
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    restaurants = results.get('local_results', [])[:num_results]

    restaurant_data = {}
    for res in restaurants:
        name = res.get('title', 'Unknown')
        restaurant_data[name] = {
            "rating": res.get('rating'),
            "reviews": res.get('reviews'),
            "address": res.get('address'),
            "phone": res.get('phone'),
            "website": res.get('website')
        }
    return restaurant_data

def main():
    city = input("Enter the name of the city: ")
    print(f"Retrieving top 10 restaurants for {city}...")
    try:
        restaurants = get_top_restaurants(city)
        filename = f"{city.replace(' ', '_').lower()}_restaurants.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(restaurants, f, ensure_ascii=False, indent=4)
        print(f"Restaurant data saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
