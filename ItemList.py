__author__ = 'David Sweetman'
import os, csv
from Item import *


# Class to make an item list from a CSV file containing items and their reserve prices
class ItemList:
    # Class to create lists of items and reserve bids from a CSV file name given as parameter
    filename = "items.csv"                  # Default Filename

    def __init__(self, fileCSV = filename):
        self.itemDict = self.buildItemDict(fileCSV)

    # CSV rows are stored as a dictionary of form {item name: item object with parameters(item name, reserve price)
    def buildItemDict(self, fn):
        itemDict = {}
        with open(os.path.join(fn), "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                itemDict[row[0].upper()] = Item(row[0].upper(), row[1])
        return itemDict

    # Method to retrieve item name attribute from item object
    def getItem(self, itemname):
        return self.itemDict[itemname]