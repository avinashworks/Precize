# Precize
This Python script prompts the user to enter the name of a city, then retrieves the top 10 restaurants in that city (based on ratings and reviews) through a Google search using the SerpApi service. The collected restaurant data is saved in a JSON file, with restaurant names as keys and relevant details (ratings, reviews, etc.) as values.

Features
Prompts for a city name via command line

Fetches top 10 restaurants for food quality and popularity

Collects ratings, number of reviews, address, phone, and website (if available)

Stores results in a JSON file named after the city

Getting Started
Prerequisites
Python 3.x

pip (for installing dependencies)

SerpApi API key (free tier available)

Installation
Clone the repository or download the script.

Install required Python package:

bash
pip install google-search-results
Get your SerpApi API key and place it in the script where indicated (API_KEY = 'YOUR_SERPAPI_KEY').

Usage
bash
python top_restaurants.py
Enter the city name when prompted.

The results will be saved to a file named <city>_restaurants.json in the current directory.

Approach
The script uses the SerpApi "google_food" engine to fetch structured restaurant data.

Results are parsed and organized into a dictionary, then saved to a JSON file with restaurant names as keys.

The script includes comments for clarity and basic error handling for robustness.

Limitations & Notes
Usage of SerpApi is subject to their free tier limitations. Heavy use may require a paid account.

Data is as accurate as Google’s local search and depends on SerpApi coverage for the specified city.

If you need to customize the fields saved, adjust the dictionary construction in the script.
