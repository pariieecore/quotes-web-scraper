import requests
from bs4 import BeautifulSoup
import json
import time
from collections import Counter

# Website URL
BASE_URL = "https://quotes.toscrape.com/"

# User-Agent header
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; StudentScraper/1.0)"
}


# Fetch webpage
def fetch_page(url):
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return None


# Extract quotes from HTML
def extract_quotes(html):
    soup = BeautifulSoup(html, "html.parser")

    quotes = []

    for item in soup.select("div.quote"):
        quote_text = item.select_one("span.text")
        author = item.select_one("small.author")
        tags = item.select("a.tag")

        # Check if required elements exist
        if quote_text and author:
            quote = {
                "quote": quote_text.get_text(strip=True),
                "author": author.get_text(strip=True),
                "tags": [tag.get_text(strip=True) for tag in tags]
            }

            quotes.append(quote)

    # Find next page
    next_page = soup.select_one("li.next a")

    if next_page:
        return quotes, next_page.get("href")

    return quotes, None


# Save data as JSON
def save_json(quotes):
    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(quotes, file, indent=2, ensure_ascii=False)

    print("Data saved to quotes.json")


# Save data as text
def save_text(quotes):
    with open("quotes.txt", "w", encoding="utf-8") as file:
        for quote in quotes:
            file.write(quote["quote"] + "\n")
            file.write("Author: " + quote["author"] + "\n")
            file.write("Tags: " + ", ".join(quote["tags"]) + "\n")
            file.write("-" * 50 + "\n")

    print("Data saved to quotes.txt")


# Display statistics
def show_statistics(quotes):
    if not quotes:
        print("No quotes found.")
        return

    authors = Counter(q["author"] for q in quotes)

    all_tags = []

    for quote in quotes:
        all_tags.extend(quote["tags"])

    print("\n--- Scraping Statistics ---")
    print("Total quotes:", len(quotes))

    if authors:
        print("Most quoted author:", authors.most_common(1)[0][0])

    if all_tags:
        print("Most common tag:", Counter(all_tags).most_common(1)[0][0])


# Main scraper
def main():
    url = BASE_URL
    all_quotes = []

    while url:
        print("Fetching:", url)

        html = fetch_page(url)

        if html is None:
            break

        quotes, next_page = extract_quotes(html)
        all_quotes.extend(quotes)

        if next_page:
            url = BASE_URL.rstrip("/") + next_page
            time.sleep(1)
        else:
            url = None

    save_json(all_quotes)
    save_text(all_quotes)
    show_statistics(all_quotes)


if __name__ == "__main__":
    main()
