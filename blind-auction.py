from blind-auction_art import logo
print(logo)
#
bid_time = True
bid_dictionary = {}
#
while bid_time == True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $ "))
  #
  bid_dictionary [name] = bid
  #
  others_check = input("Are there any other bidders? Type 'yes or 'no'.")
  if others_check == "no":
    bid_time = False
    winner = ""
    highest_bid = 0
    #
    print(bid_dictionary)
    for key in bid_dictionary:
      if bid_dictionary[key] > highest_bid:
        winner = key
        highest_bid = bid_dictionary[key]
        print(highest_bid)
print(f"The winner is {winner} with a bid of ${highest_bid}")
