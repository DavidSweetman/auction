__author__ = 'David Sweetman'
import unittest
from Item import *
from Bidder import *


# Unit test to test the functionality set out in the exercise description in the email
# Tests the ability to: record a bid, get the winning bid, get all the bids for an item, and all the bids for user
# as well as other functionality of the code.
class TestAuction(unittest.TestCase):

    def setUp(self):
        self.testitem1 = Item("Car", 1000)
        self.testitem2 = Item("Boat", 10000)
        self.testitem3 = Item("Game", 100)
        self.testbidder1 = Bidder("John Doe")
        self.testbidder2 = Bidder("Jane Doe")

    # Test to check if when we add a bid, the bid stored in the item matches the added bid
    def test_add_bid_and_check_bid_methods(self):
        self.testitem1.addBid(1001, self.testbidder1)                    # Add bid by John to Car
        self.assertEqual(self.testitem1.getCurrentBid(), 1001)           # Check if the bid added matches amount stored

    # Test if adding a bidder with an argument creates that bidder object and we can access the bidder name
    def test_add_bidder(self):
        testbidder = Bidder("John Doe")                                   # Create bidder object
        self.assertEqual(testbidder.bidderName, "JOHN DOE")               # Check if there is a bidder with name

    # Check if the getItemsBidOn method retrieves the dictionary of items bid for
    def test_check_user_bid_hist_call(self):
        self.testitem1.addBid(1001, self.testbidder2)                     # Add bid by Jane to Car
        self.testitem2.addBid(10001, self.testbidder2)                    # Add bid by Jane to Boat
        bidhistdict = self.testbidder2.getItemsBidOn()                    # Make a dictionary using the method
        self.assertEqual(bidhistdict,self.testbidder2.itemsBidForDict)    # Check if it is the same as the items bid on

    # Check if we can get all the items for which a user has bid on
    def test_check_user_bid_hist(self):
        bidhistdict = self.testbidder1.getItemsBidOn()
        self.testitem2.addBid(10001, self.testbidder1)                     # Add a bid by John for Boat
        self.assertTrue("CAR" in bidhistdict and "BOAT" in self.testbidder1.getItemsBidOn())

    # Check if a bid is correctly stored in a the items bid history list
    def test_check_item_bid_hist(self):
        self.testitem1.addBid(1001.50, self.testbidder2)
        self.assertIn(('JANE DOE',1001.50),self.testitem1.bidList)

    # Check if item can be set as sold and we can check that status
    def test_check_item_set_as_sold(self):
        self.testitem1.changeStatus()                                       # Set as sold
        self.assertTrue(self.testitem1.soldStatus)                          # Check status

    # Test that if a string is added as a bid, the bid will not be registered
    def test_bid_error(self):
        self.testitem2.addBid("100000gbp",self.testbidder1)                 # Add bid with string as bid amount
        self.assertFalse(self.testitem2.bidstatus)                          # Check if bid has been made

    # Test that we can retrieve the winning bid of an item marked as sold
    def test_get_winning_bid(self):
        self.testitem2.addBid(99999, self.testbidder1)                      # Add a bid by John for Boat
        self.testitem2.changeStatus()                                       # Set it as sold
        self.assertEqual(self.testitem2.getwinningbid(),99999)              # Check if winning bid is equal to Johns bid

    # Test that we can retrieve the winning bidder of an item marked as sold
    def test_get_winning_bidder(self):
        self.testitem3.addBid(99999, self.testbidder1)
        self.testitem3.changeStatus()                                       # Set as sold
        self.assertEqual(self.testitem3.winner,"JOHN DOE")                  # Check if winner stored in item is right


suite = unittest.TestLoader().loadTestsFromTestCase(TestAuction)
unittest.TextTestRunner(verbosity=2).run(suite)
