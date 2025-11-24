# src/search_fetcher.py
from serpapi import GoogleSearch
from .config import SERPAPI_KEY

def fetch_top_urls(query: str, num: int = 10):
    params = {"engine":"google", "q": query, "num": num, "api_key": SERPAPI_KEY}
    results = GoogleSearch(params).get_dict()
    return [r["link"] for r in results.get("organic_results", [])[:num]]
