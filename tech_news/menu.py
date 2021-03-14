from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)
import sys


def collector_menu():
    entrada = input(
        "Select a option:\n"
        " 1 - Import news from CSV file;\n"
        " 2 - Export News to CSV;\n"
        " 3 - Scrape news;\n 4 - Exit."
    )

    if entrada == "1":
        file_path = input("CSV file name:")
        file_content = csv_importer(file_path)
        create_news(file_content)
    elif entrada == "2":
        file_path = input("Exported CSV file name:")
        csv_exporter(file_path)
    elif entrada == "3":
        pages = input("Number of pages to Scrape:")
        data = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(data)
    elif entrada == "4":
        print("Exit\n")
    else:
        print("Invalid option. Try again.", file=sys.stderr)


def analyzer_menu(): 
    """Seu código deve vir aqui"""
