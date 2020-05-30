import random
import time

cards = 0
human = 0
pc = 0
color = ""
card = ""
initial_turn = True
bankroll = 50


def set_default():
    global cards
    cards = [["2","3","4","5","6","7","8","9","10","J","Q","K","A"],["2","3","4","5","6","7","8","9","10","J","Q","K","A"],["2","3","4","5","6","7","8","9","10","J","Q","K","A"],["2","3","4","5","6","7","8","9","10","J","Q","K","A"]]
    global human
    human = 0
    global pc
    pc = 0
    global initial_turn
    initial_turn = True

def draw_card(player):

    card_exists = False

    global color
    global card

    card, color, points = "", "", 0

    while card_exists == False:
        color_number = random.randint(0,3)
        card_number = random.randint(0,12)

        if cards[color_number][card_number] == 0:
            exit
        else:
            card_exists = True

    card = cards[color_number][card_number]

    if color_number == 0:
        color = "♥"
    elif color_number == 1:
        color = "♦"
    elif color_number == 2:
        color = "♣"
    else:
        color = "♠"

    calculate_points(color_number, card_number, player)
    remove_card(color_number, card_number)

    if player == "human":
        points = human
    else:
        time.sleep(2)
        points = pc

    if points < 21:
        if player == "human":
            print("")
            print(f"Your next card: " + "" + str(card) + color + " Value: " + str(human))

            choice = input("Do you want to draw another card? (y/n): ")

            if choice == "y":
                draw_card("human")
            else:
                draw_card("pc")
        elif player == "pc" and points < 21 and points > 16:
            print("")
            print(f"The house got: " + "" + str(card) + color + " Value: " + str(pc))
            time.sleep(1)
            print("")
            print("The house stops at: " + str(points))
            evaluate()
        else:
            print("")
            print(f"The house got: " + "" + str(card) + color + " Value: " + str(pc))
            draw_card("pc")
    elif points == 21:
            if player == "human":
                print("")
                print("Nice you've got a: " + str(card) + color + ", that makes 21. Let's see what the house gets.")
                draw_card("pc")
            if player == "pc":
                print("")
                print("The house got: " + "" + str(card) + color + " Value: " + str(pc))
                evaluate()
    else:
        if player == "human":
            print("")
            print("You got a " + str(card) + color + " and now have " + str(human) + " Points, therefore busting busting 21")
            print("")
            evaluate()
        else:
            print("")
            print("The house got a " + str(card) + color + " and hit above 21")
            print("")
            evaluate()


def remove_card(color, card):
    cards[color][card] = 0

def calculate_points(color, card, player):

    global human
    global pc

    if player == "human":
        if cards[color][card] in ["J","Q","K"]:
            human += 4
        elif cards[color][card] in ["2","3","4","5","6","7","8","9","10"]:
            human += int(cards[color][card])
        else:
            if (human + 11) > 21:
                human += 1
            else:
                human += 11
    else:
        if cards[color][card] in ["J","Q","K"]:
            pc += 4
        elif cards[color][card] in ["2","3","4","5","6","7","8","9","10"]:
            pc += int(cards[color][card])
        else:
            if (pc + 11) > 21:
                pc += 1
            else:
                pc += 11

def evaluate():

    global bankroll

    time.sleep(1)

    if human > 21 and pc <= 21:
        bankroll -= 10
        print("")
        print("You lost this round. Your current Bankroll is: " + str(bankroll))
        print("")
    elif pc > 21:
        bankroll += 20
        print("")
        print("You won this round. Your current Bankroll is: " + str(bankroll))
        print("")
    else:
        if human > pc:
            bankroll += 20
            print("")
            print("You won this round. Your current Bankroll is: " + str(bankroll))
            print("")

        elif human == pc:
            print("")
            print("You both got: " + str(human) + " Points and that's a draw. Your current Bankroll is " + str(bankroll))            
        else:
            bankroll -= 10
            print("")
            print("You lost this round. Your current Bankroll is: " + str(bankroll))

    end_of_round(1)

def end_of_round(integer):
    if integer == 1:
        if bankroll > 0:
            answer = input("Would you like to play another game1? (y/n): ")
            
            if answer == "y":
                welcome_message("another")
            else:
                time.sleep(1)
                end_of_round(0)
        else:
            print("")
            print("")
            print("Sorry but you're broke. The Casino is no place for you!")
            print("")
            print("Come back if you have can afford it")
            print("")
            time.sleep(1)
    else:
        print("")
        if (bankroll - 50) > 0:
            print("Sorry to hear that. You leave the casino with +" + str(bankroll - 50) + " Credits")
            print("")
            print("Congratulation !!") 
            print("")
        elif (bankroll - 50) < 0:
            print("Sorry to hear that. You leave the casino with " + str(bankroll - 50) + " Credits")
            print("")
            print("We are sorry :/")
        elif (bankroll - 50) == 0:
            print("Sorry to hear that. You leave the casino with +" + str(bankroll - 50) + " Credits")
            print("")
            print("We hope you had a good time")
        print("")
    


def welcome_message(round):

    set_default()

    if round == "first":

        names = ["Tom", "Stephanie", "Kim", "Jerry", "Alex", "Michael", "Robin", "Kirsten", "Melanie", "Richard"]

        print("")
        print("######################################################")
        print("###  WELCOME TO THE GRAND CIRCLE BLACKJACK CASINO  ###")
        print("######################################################")
        print("")
        print("Your host tonigh will be " + names[random.randint(0,9)])
        print("")
        answer = input("Your Bankroll is 50 Credits and a Game costs 10. \n \nAre you ready to play? (y/n): ")

        if answer == "y":
            draw_card("human")
        else:
            print("Sorry to hear that. You can always return later for a game")
            print("")
            print("")
            return

    else:
        time.sleep(1)
        print("")
        print("Alright, let's start the next round:")
        print("")
        draw_card("human")

welcome_message("first")