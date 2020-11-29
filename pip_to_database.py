from pymongo import MongoClient
from Scraper import scraper
import time

#connect to mongo and create connection to PIP database
client = MongoClient('mongodb+srv://cowen:compproject@cluster0.1qgln.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.PIPdata

file_Name = '../PIPtagCode/ReceiverCode/data.txt'
scraper = scraper.FileScraper(file_Name)
while True:
    scraper.extract_line()
    scraper.print_last_line()
    scraper.extract_sensor_data()
    time.sleep(2)