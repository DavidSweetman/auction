__author__ = 'David Sweetman'
import operator

# Class to create Item objects
class Item:

    # Set default values for the attributes of each Item
    currentBid = 0.0
    highestBidHolder = ""
    winner = ""
    soldStatus = False
    bidListDict = {}                                               # Dict of all the highest bids on item by users
    bidList = []                                                   # List of all the bids made on item
    itemName = ""

    # constructor for object
    def __init__(self, itemName, startingPrice = 0.0):
        self.itemName = itemName.upper()
        self.currentBid = startingPrice

    # Method to retrieve item name
    def getName(self):
        return self.itemName

    # Accessor to get current highest bid on the item
    def getCurrentBid(self):
        return self.currentBid

    # Mutator to add a bid to an item
    def addBid(self, newBidRaw, bidder):
        self.bidstatus = False
        try:
            newBid = float(newBidRaw)                                      # Turn bid into float
            if self.soldStatus is False:                                   # If its not sold
                if float(newBid) <= float(self.currentBid):                # If bid is not higher than current bid
                    print("Bid not higher than current bid")
                    self.bidListDict[str(bidder.bidderName)] = newBid      # Add bid to dict of bids made for item
                    self.bidList.append((str(bidder.bidderName),newBid))   # Add bid to list of bids made for item
                    self.bidstatus = True

                else:                                                      # If it is highest bid
                    self.currentBid = newBid                               # Set new bid as highest bid amount
                    self.highestBidHolder = str(bidder.bidderName)         # Set highest bidder as new bidder
                    self.bidListDict[str(bidder.bidderName)] = newBid      # Add bid to dictionary of bids for item
                    bidder.ammendBidDict(newBid,self)                      # Add bid to the bidders dict of bids made
                    self.bidList.append((str(bidder.bidderName),newBid))   # Add bid to list of bids made for item
                    self.bidstatus = True
            else:                                                          # If it is sold already
                print("Item already sold")
        except (KeyError, ValueError):
                output = "Error. Input must be just a number"
                self.bidstatus = False

    # Accessor to get the winning bid of a sold item
    def getwinningbid(self):
        if self.soldStatus == False:
            print("Item still for sale, no winning bid")
        else:
            return self.winningbid

    # Prints out list of bids made by a user
    def getBidList(self):
        print(self.bidList)

    # Print whether Item is sold or not, with the relevant bid
    def printStatus(self):
        if self.soldStatus is True:
            print("Item Sold for ", self.currentBid)
        else:
            print("Item still available. Current highest bid: ", self.currentBid)

    # Set the item as sold
    def changeStatus(self):
        self.soldStatus = True                                       # Sets item as sold
        self.winningbid = self.currentBid                            # Sets the current highest bid as winning bid
        self.winner = max(self.bidListDict.items(), key=operator.itemgetter(1))[0]
        return self.soldStatus

    def __str__(self):
        return self.itemName