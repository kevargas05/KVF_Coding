from random import choice
from art import logo, vs
from game_data import data
#from replit import clear
#
def random_item():
    item_info = choice(data)
    return item_info
#
def followers_comparison(a,b):
    if a>b:
        return "a"
    else:
        return "b"
#
#
def game_display(user_score, option_a_info, option_b_info):
    '''
    Returns user choice
    '''
    print(logo)
    if user_score != 0:
        print(f"You're right! Current score: {user_score}")
    print(f"Compare A: {option_a_info['name']}, {option_a_info['description']}, {option_a_info['country']}")
    print(vs)
    print(f"Against B: {option_b_info['name']}, {option_b_info['description']}, {option_b_info['country']}")
    choice = input("Who has more followers? Type 'A' or 'B':\n").lower()
    return choice
#
def game():
    option_a_info = random_item()
    option_a_followers = option_a_info ['follower_count']
    #
    option_b_info = random_item()
    option_b_followers = option_b_info ['follower_count']
    while option_a_followers == option_b_followers:
            option_b_info = random_item()
            option_b_followers = option_b_info ['follower_count']
    #
    answer = followers_comparison(option_a_followers,option_b_followers)
    user_score = 0
    #
    user_choice = game_display(user_score, option_a_info, option_b_info)
    #
    while user_choice == answer:
        #clear()
        user_score += 1 
        if "a" == user_choice:
            option_a_info = random_item()
            option_a_followers = option_a_info ['follower_count']
            #
            option_b_info = random_item()
            option_b_followers = option_b_info ['follower_count']
            #
            while option_a_followers == option_b_followers:
                option_b_info = random_item()
                option_b_followers = option_b_info ['follower_count']
            #
            user_choice = game_display(user_score, option_a_info, option_b_info)
        else:
            option_a_info = option_b_info
            option_a_followers = option_b_followers
            #
            option_b_info = random_item()
            option_b_followers = option_b_info ['follower_count']
            while option_a_followers == option_b_followers:
                option_b_info = random_item()
                option_b_followers = option_b_info ['follower_count']
            #
            user_choice = game_display(user_score, option_a_info, option_b_info)
            
    #
    print(f"Game Over. Final Score: {user_score}")
    return

game()
