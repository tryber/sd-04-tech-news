from pymongo import MongoClient
from tech_news.database import db
import re


lista = db.news.find({"timestamp": re.compile("2020-11-11", re.IGNORECASE)})

for i in lista:
    print(lista)
