__author__ = 'David Sweetman'


# Class to create Bidder objects
class Bidder:
    # Class to create bidder objects that contains the name, items bid for
    bidderName = ""
    itemsBidForDict = {}                                          # Dictionary of Items that Bidder has bid for.

    # Constructor takes in name as string
    def __init__(self, bidderName):
        self.bidderName = bidderName.upper()                      # Saves bidder name as upper case

    # Adds to dictionary of bid history in form {item name: most recent bid,....}
    def ammendBidDict(self, newBid, item):
        self.itemsBidForDict[item.getName()] = float(newBid)      # Adds to dictionary

    # Returns the dictionary of bids in form {item name: most recent bid,....}
    def getItemsBidOn(self):
        return self.itemsBidForDict
