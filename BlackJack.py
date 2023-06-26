import random
import time

class Blackjack():
    def __init__(self):
        self.card = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
        self.dealer_card = []
        self.player_card = []
    
    def shuffle(self):
        print("Welcome to the Black Jack game. In this game, you will play with the Dealer, try to win him!\n")
        while True:
            play_choice = input("Are you ready?(Y/N): ").lower()
            if play_choice in ('y','yes'):
                print("The dealer is shuffling the cards...\n")
                time.sleep(2)
                print("-------------------------------------------")
                time.sleep(2)
                dealer_card_1 = random.choice(list(self.card.keys()))
                dealer_card_2 = random.choice(list(self.card.keys()))
                self.dealer_card.append(dealer_card_1)
                self.dealer_card.append(dealer_card_2)
                self.card[dealer_card_1] -= 1
                self.card[dealer_card_2] -= 1
                print(f"Dealer got {self.dealer_card[0]}, the other one is hidden")
                player_card_1 = random.choice(list(self.card.keys()))
                player_card_2 = random.choice(list(self.card.keys()))        
                self.player_card.append(player_card_1)
                self.player_card.append(player_card_2)
                self.card[player_card_1] -= 1
                self.card[player_card_2] -= 1
                print(f"You have {self.player_card}")
                self.playerChoice()
                break
            elif play_choice in ('n','no'):
                wait_choice = input("How many seconds until you're ready? You can enter number of seconds that you need or 'No' to exit: ").lower()
                if wait_choice in ('no','n'):
                    print("See you next time!")
                    break
                elif wait_choice.isdigit() == True:
                    print("-------------------------------------------")
                    time.sleep(int(wait_choice))
                    self.shuffle()
                    break
                else:
                    print("Please enter a number of seconds that you want us to wait or 'No' to exit!")
            else:
                print("You have entered wrong choice. Please try again!")

    def playerChoice(self):    
        if sum(self.player_card) > 21:
            print("Your hand is over 21 points now. You lost!")
            return None
        while True:
            player_choice = input("What would you like to do now ('Hit' to get another card, 'Stand' to stop dealing card and compare hands)?: ").lower()
            if player_choice == "hit":
                if len(self.player_card) == 5:
                    print("You have reached 5 cards, you can't get anymore cards")
                    break
                player_card_x = random.choice(list(self.card.keys()))
                self.player_card.append(player_card_x)
                self.card[player_card_x] -= 1
                print(f"You now have {self.player_card}")
                for card, count in self.card.items():
                    if count == 0:
                        self.card.pop(card)
                if sum(self.player_card) > 21:
                    print("Your hand is over 21 points now. You lost!")
                    break
            elif player_choice == "stand":
                if sum(self.player_card) < 17:
                    print(f"You only have {sum(self.player_card)}. It is not enough points for you to stand.")
                    continue
                    # self.playerChoice
                else:
                    print(f"You have {sum(self.player_card)} points. Let's get to the next stage!")
                    break
            else:
                print("You entered the wrong choice. Please choose again!")
        self.compareHands()

    def compareHands(self):
        if sum(self.player_card) > 21:
            pass
        elif sum(self.dealer_card) > 21:
            print(f"The dealer got {self.dealer_card}.\nThe dealer is busted. You won, congratulation!")
        elif sum(self.dealer_card) > sum(self.player_card):
            print(f"The dealer got {self.dealer_card}.\nYou lost! Wish you luck next time!")
        else:
            print(f"The dealer got {self.dealer_card}.\nYou won, congratulation!")

class Main():
    game = Blackjack()
    game.shuffle()
