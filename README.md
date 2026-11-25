# Python Web Scraper – Quotes Extractor

## About the Project

This project is a simple Python web scraper that extracts quotes from a public practice website using Requests and BeautifulSoup.

It collects quotes, author names, and tags from multiple pages and saves the results in JSON and text files.

## Features

- Fetches web pages using Requests
- Extracts HTML data using BeautifulSoup
- Collects quotes, authors, and tags
- Automatically follows pagination
- Saves data in JSON format
- Saves readable text output
- Displays total quotes and common authors and tags
- Handles HTTP errors and missing HTML elements
- Uses a delay between requests

## Source Website

Quotes to Scrape

https://quotes.toscrape.com/

This website is designed for practicing web scraping.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup
- JSON
- Collections module

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command in the terminal:

```bash
python scraper.py
```

The program will automatically fetch the pages and save the extracted data.

## Output Files

### quotes.json

Contains the extracted quotes, authors, and tags in JSON format.

### quotes.txt

Contains the quotes in a readable text format.

## Example Data

```json
{
  "quote": "Example quote text",
  "author": "Example Author",
  "tags": ["life", "inspiration"]
}
```

## Polite Scraping Practices

- Used a descriptive User-Agent.
- Added a timeout to HTTP requests.
- Handled request errors.
- Waited one second between page requests.
- Used a practice website for educational purposes.

## Learning Outcomes

Through this project, I learned how to send HTTP requests, inspect HTML elements, extract data using CSS selectors, handle pagination, save structured data in JSON, and follow polite web scraping practices.

## Author

Pari Bansal
