import scraper as _scraper
import json as _json 

if __name__ == "__main__":
    quotes = _scraper.scrape_quote()
    with open("quotes.json",mode="w", encoding="utf-8") as quotes_file:
        _json.dump(quotes, quotes_file, ensure_ascii=False)