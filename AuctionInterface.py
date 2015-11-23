__author__ = 'David Sweetman'
from ItemList import *
from Bidder import *

itemlist = ItemList()
bidDict = {}
status = True                                                 # True while we want programme to keep running


while status is True:
    while True:
        try:
            userinput = int(input("""Do you want to?
                         Place a Bid (1)
                         Get Highest Bid for item(2)
                         See all bids for item(3)
                         See all items bid on by user(4)
                         Exit(5)
                         Enter selection: """))                     # Ask user for number corresponding to task req.
        except ValueError:                                          # Not a valid selection
            print("Error, invalid selection")
        else:                                                       # Set number as task
            task = userinput
            break

    if task == 1:
        while True:
            try:
                itemtobid = input("Enter Item name to bid on: ").upper()
                iteminfo = itemlist.getItem(itemtobid)
                biddername = input("Enter Bidder name: ").upper()
                if biddername in bidDict:                                # Check if bidder has made bids yet
                    bidder = bidDict[biddername]                         # Set already made bidder as bidder

                else:
                    bidder = Bidder(biddername)                          # Create new bidder
                    bidDict[biddername] = bidder                         # Add them to the Dictionary of bidders
                bid = float(input("Enter bid amount: "))
            except (KeyError, ValueError):                               # If bid not a floatable number, exit
                print("Error, invalid selection. Start Bid again")
            else:
                Item.addBid(iteminfo, bid, bidder)                       # add bid to item
                if iteminfo.bidstatus is True:                           # check that bid has been made
                    print("Bid that you entered", biddername, ":", bid, "gbp")
                else:
                    print("Bid not entered")                             # if not print error
                break

    elif task == 2:
        while True:
            try:
                itemCheck = input("Enter item name to check: ").upper()
                iteminfo = itemlist.getItem(itemCheck)                   # get item corresponding to item name
                currentbid = Item.getCurrentBid(iteminfo)                    # get the current bid for it
            except KeyError:
                print("Error, item not found. Retry.")                   # if item not in list, print error
            else:
                if Item.soldStatus(iteminfo) is True:                    # check if its current bid or winning bid
                    print("Winning bid is", currentbid)
                else:
                    print("Current highest bid is", currentbid)
                break

    elif task == 3:
        try:
            itemBids = input("Enter item you wish to see bids for: ").upper()
            iteminfo = itemlist.getItem(itemBids)                         # Get item corresponding to item name entered
            answer = Item.getBidList(iteminfo)                            # Get list of all bids made for item
            print(answer)
        except KeyError:
            print("Error, item not found. Retry.")


    elif task == 4:
        bidhist = input("Enter user name that you would like to see the items bid for: ").upper()
        if bidhist in bidDict:                             # Check if bidder name has made bids
            bidderreq = bidDict[bidhist]
            for key in bidderreq.itemsBidForDict:
                print(key)                                  # Print all the keys, i.e the items bid for
        else:
            print("Error, no history for that username.")
    elif task == 5:
        status = False                                     # So that programme stops running and exits

    else:
        print("Invalid option")                             # If user does not pick one of the options available
