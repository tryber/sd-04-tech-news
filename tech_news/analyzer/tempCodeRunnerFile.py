from pymongo import MongoClient
from tech_news.database import db

lista = db.news.find({"timestamp": "2020-11-11"})

for i in lista:
    print(lista)
