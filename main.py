#importing random module in order to generate a random choice for the player and the computer from a given list.
import random

#this function (deal_card) will contain the cards variable that will have the cards values and the random module will be used to randomly generate the cards and display them.
#the 11 will represent the ace and the 4 values of 10 will represent: 10 card + queen (10) + king(10) + jack(10).
#this function(deal_card) will be useful for picking a random value from the given list.
def deal_card():
 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#this function (calculate_score) will be used to calculate the score of the given cards.
#this function will be useful for figuring out the blackjack value (0).
#in order to calculate the score, the number 11 (ace) have to be configured according to the score. Added as 11 if the score is below 21, or added as 1 if the score is over 21.
def calculate_score(cards):
  

  
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#this function will be used to compare the scores between the player and the computer. (Game rules)
#according to the game rules, this function will be used to establish these rules, display each possible outcome and compare the scores.
#for example if the player score will be equal to the computer score the result will be a draw.
def compare(user_score, computer_score): 

  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lost!"

  if user_score == computer_score:
    return "It is a Draw!"

  elif computer_score == 0:
    return "You Lost, opponent has Blackjack!"

  elif user_score == 0:
    return "BLACKJACK!!! Congratulations, you win!"

  elif user_score > 21:
    return "You went over. You lost!"

  elif computer_score > 21:
    return "Computer went over. You win!"

  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lost!"

#this function (play_game) will basically contain the game.
#the role of this function is to append 2 random cards to each player, as a list, from the previous function where we have the cards varialble (deal_card function)
# the "_" from the for loop is just a random value that is not declared anywhere else. 
#For the player, we also need to know the score and if they won or not. This function will calculate the player score and display the results.
#if the score number is less than 21 and the player decides to pick another card, this function will allow that using the user_dealing_again input where another card will be randomly picked and added to the total score.
#For the computer point of view, this function will calculate the score and display the results. The difference is that when the score of the random card is not equal to 0 (blackjack) or less than 17, another random card will be added to the score.
#Finally, the scores are compared and the updated results are displayed accordingly.
def play_game():

  
  user_cards = []
  computer_cards = []
  game_over = False


  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  

  while not game_over:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      
      user_dealing_again = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_dealing_again == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Player final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


    

#this is a statement that will call the main function whenever the game reaches the end (game over).
if __name__ == "__main__":
   
  while input("Welcome to BLACKJACK card game, also known as 21. Do you want to play? Type 'y' or 'n': ") == "y":
    play_game()
