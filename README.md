# Redfin Property Data Scraper

## Introduction

This script is designed to scrape property data from Redfin, a popular real estate listing platform. It uses the Selenium library in Python to automate the process of navigating through multiple pages and extracting the required information.

## Requirements

Before running the script, make sure you have the following requirements installed:

- Python 3.x
- Selenium library
- Pandas library
- undetected_chromedriver library

## Installation

To install the required libraries, you can use pip:

```bash
pip install selenium pandas undetected_chromedriver
```

## Usage

To use the script, follow these steps:

1. Download the script and save it as a `.py` file.
2. Create an Excel file named `input.xlsx` with the following columns:
   - Link: The URL of the Redfin page to scrape.
   - Location: The location of the property.
   - Keyword: A keyword related to the property.
   - Link Type: The type of link (e.g., "For Sale" or "For Rent").

3. Run the script using Python:

```bash
python redfin_scraper.py
```

The script will read the input data from the `input.xlsx` file, navigate to each Redfin page, scrape the property data, and save it to an Excel file named `Property_data.xlsx`.

## Script Overview

The script starts by importing necessary libraries and initializing a WebDriver instance using the `undetected_chromedriver` library to bypass detection.

It then reads the input data from the `input.xlsx` file and stores the data in separate lists for links, locations, keywords, and link types.

The script iterates over each link in the input data and opens the corresponding Redfin page in the WebDriver. For each property listing on the page, it scrapes various details such as the property status, agent information, address, price, estimated monthly payment, beds, baths, square footage, images, link, time on Redfin, MLS number, lot size, property type, and description.

The scraped data is stored in a dictionary called `headings`. After scraping data for all property listings on a page, the script converts the dictionary into a Pandas DataFrame and prints it.

The script handles exceptions and checks for missing or empty data. It also handles cases where there are multiple tabs open, such as when clicking on multiple property listings.

Finally, the script appends the scraped data to an existing Excel file named `Property_data.xlsx` or creates a new file if it does not exist.

The script quits the WebDriver and prints a completion message when all data has been scraped against all links available in the input file.

## Note

Please note that this script is just an example and may require modifications to fit your specific requirements. Make sure to customize the script according to your needs before running it.
