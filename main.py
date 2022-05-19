import random
from termcolor import colored, cprint


suits = ["D", "H", "S", "C"]
values = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
decks = 1
card = []
player_hand = []
dealer_hand = []
current_bet = 0
player_money = 500
index = 0

class Dealer():
    def dealer_print_cards(self):
        print("Dealer cards are:")
        for i in range(5): # Den här checkar varje index i min hand och lägger till den korrekta färgen för det kortet
            if 'H' in dealer_hand[i]:
                cprint(f"{dealer_hand[i][0]} {dealer_hand[i][1]}", 'red', end=' ')   # ett bättre sätt att formatera om strings. Enklare att läsa/förstå än str.format()
            elif 'D' in dealer_hand[i]:
                cprint(f"{dealer_hand[i][0]} {dealer_hand[i][1]}", 'cyan', end=' ')
            elif 'S' in dealer_hand[i]:
                cprint(f"{dealer_hand[i][0]} {dealer_hand[i][1]}", 'magenta' , end=' ')
            elif 'C' in dealer_hand[i]:
                cprint(f"{dealer_hand[i][0]} {dealer_hand[i][1]}", 'grey', end=' ')
            if i != 4:  # När den hamnar på index 4 kommer den inte längre printa "|"
                print("|", end = " ")
        print("\n")

    def dealer_round(self): # En enkelt dealer bot. Om jag hade mer tid hade jag kunnat göra den smartare, men det här gör så att den iaf fungerar.
        dealer_index = 0
        chance = random.randint(1,100)
        if 0 <= chance < 20:
            dealer_index = 0
        elif 20 <= chance < 40:
            dealer_index = 1
        elif 40 <= chance < 60:
            dealer_index = 2
        elif 60 <= chance < 80:
            dealer_index = 3
        elif 80 <= chance <= 100:
            dealer_index = 4
        dealer_hand.remove(dealer_hand[dealer_index])
        dealer_hand.append(card.pop(0))
 

class Playergame():
    def player_print_cards(self):
        print("Your cards are:")
        for i in range(5): # Precis som funktion för när dealern printar korten men för playern. Det går ej att undvika denna koduppreptning eftersom det är två olika listor den hanterar
            if 'H' in player_hand[i]:
                cprint(f"{player_hand[i][0]} {player_hand[i][1]}", 'red', end=' ')
            elif 'D' in player_hand[i]:
                cprint(f"{player_hand[i][0]} {player_hand[i][1]}", 'cyan', end=' ')
            elif 'S' in player_hand[i]:
                cprint(f"{player_hand[i][0]} {player_hand[i][1]}", 'magenta' , end=' ')
            elif 'C' in player_hand[i]:
                cprint(f"{player_hand[i][0]} {player_hand[i][1]}", 'grey', end=' ')
            if i != 4:
                print("|", end = " ")
        print("\n")
    
    def player_round(self): 
        global index
        while index < 2: # under en hel match ska du bara kunna kasta bort två kort totalt
            try:
                answer1 = input("Do you want to toss a card?\n yes/no\n").lower()
                if answer1 == "yes":
                    while True:
                        print("Type the card you want to remove?")
                        try:
                            toss = input()
                            toss = toss.split(" ") # Separerar stringen till två individuella stringen till en lista så man kan ta bort den från "player_hand"
                            toss[0] = toss[0].capitalize() # eftersom stringen nu är i två delar behöver vi felhantera båda delarna och se till så vi kan skriva med små bokstäver
                            toss[1] = toss[1].capitalize()
                            player_hand.remove(toss)
                            player_hand.append(card.pop(0))
                            index+= 1
                            break
                        except:
                            print("You don't have that card in your hand")
                elif answer1 == 'no':
                    break
            except:
                continue
            
        if player_money > 0: # Du ska inte kunna betta om du inte har några pengar kvar
            print("Do you want to increase your current bet?\nyes/no")
            while True:
                try:
                    answer2 = input().lower()
                    if answer2 =="yes":
                        print("You have betted", current_bet,end="$\n")
                        playergame.player_bet()
                        break
                    elif answer2 == 'no':
                        print("Well, thats okay")
                        break
                except:
                    continue

    def player_bet(self): # ett betting system som körs i början av spelet och kan köras varje runda om man vill
        global player_money # Globala variabler så att dom inte återställs varje gång vi kallar på funktionen
        global current_bet
        print("You have",player_money,end="$. How much do you want to bet?\n")
        while True:
            try:
                place_bet= int(input())
                if player_money >= place_bet:
                    current_bet+=place_bet
                    player_money-=place_bet
                    print("You have now betted", current_bet, end="$\n")
                    break
                else:
                    print("You don't have that much money on you.")
            except ValueError: # När du skriver bokstäver istället för ett nummer
                print("Please enter a number.")
                continue


class Poker():
    def card_combinations(self): #Då jag skulle kunna lägga allt i en print. Så är det här det bättre valet ifall någon skulle felhantera koden, det går heller inte att skriva flera färger samtidigt med "colored" så jag måste skriva om kommandot flera gånger i varje print.
        spade = colored("Spade", 'magenta')
        hearts = colored("Hearts", 'red')
        diamonds = colored("Diamonds", 'cyan')
        clubs = colored("Clubs", 'grey')
        print("There is 4 colours that indicates type of cards. Theese are:\n",spade, hearts, diamonds, clubs,"\nThere is also 7 combinations you can have with your cards. Theese are:")  
        royalflush=colored("One  King  Queen  Jack  Ten", 'red')
        straight_flush=colored("Five  Six  Seven  Eight  Nine", 'grey')
        flush = colored("Two  Four  Five  Six  Nine", 'red')
        print("Royalflush\n",royalflush,"\nStraight Flush\n",straight_flush,"\nFlush\n", flush)
        print("Four of a kind\n",colored("King", 'red'), colored("King", 'cyan'), colored("King", 'magenta'), colored("King", 'grey'))
        print("Full house\n",colored("King", 'red'), colored("King", 'cyan'), colored("Nine", 'magenta'), colored("Nine", 'cyan'), colored("Nine", 'grey'))
        print("Straight\n",colored("Five", 'red'), colored("Six", 'cyan'), colored("Seven", 'magenta'), colored("Eight", 'grey'), colored("Nine", 'cyan'))
        print("Three of a kind\n",colored("King", 'red'), colored("King", 'magenta'), colored("King", 'cyan'))
        print("Two pair\n", colored("King", 'red'), colored("King", 'cyan'), colored("Nine", 'magenta'), colored("Nine", 'grey'))
        print("Pair\n", colored("King", 'red'), colored("King", 'cyan'))
        print("There are a total of two rounds and each round you can choose whether or not you want to toss a card or keep your current hand.\nHowever, you can only toss a maxium of two cards each game")

    def shuffle_cards(self):
        global decks
        global suits
        global values
        for deck in range(decks): # shufflar mina kort med möjlighet att lägga till flera kortlekar ifall man vill
            for suit in suits:
                for value in values:
                    card.append([suit, value])
                    random.shuffle(card)

        for nr in range(5): # lägger till korten i min spelare samt motståndaren. Den ger ett kort till mig ett kort till dealern.
            player_hand.append(card.pop(0))
            dealer_hand.append(card.pop(0))

    def start_game(self):
        while True:
            print("1. Play Poker.         2. Check out Rules.")
            player = input()
            if player == "1":
                poker.play_game()
            elif player =="2":
                poker.card_combinations()
                continue

    def play_game(self):
        poker.shuffle_cards()
        playergame.player_bet()
        for nr in range(2):
            playergame.player_print_cards()
            playergame.player_round()
            dealer.dealer_round()
        print("\033[H\033[J")
        dealer.dealer_print_cards()
        playergame.player_print_cards()
        poker.end_game()

    def end_game(self):
        global current_bet
        global player_money
        global index
        global player_hand
        global dealer_hand
        global card
        # Hade inte tid att programmera en funktion för att räkna ut ifall man vann så den här är temporär.
        print("The winning part of the game is not yet implemented.\nHowever, you can still calculate yourself if you won the game or not.\nDid you win?\n yes/no")
        while True:
            endgame = input().lower()
            if endgame =="yes":
                for i in range(random.randint(1,6)): # Lite roligt eftersom spelaren antagligen kommer ljuga.
                    print("Really?")
                    truth = input().lower()
                    if "no" in truth:
                        print("We know...")
                        quit() # Ett straff för att spelaren ljög
                current_bet *= 1.5
                player_money+=current_bet
                print("You won",current_bet,"$You now have a total of",player_money,end="$\n")
            elif endgame =="no":
                current_bet = 0
                print("Loser")

            if player_money <= 0:
                print("You can't play because you don't have any money left")
                quit() # Självklart kan du ju inte köra om du har pengar så den här stänger ner programmet när du har fått slut på pengar.
            else:
                print("Wanna play again?\nyes/no")    
                restart = input().lower()
                if restart == "yes":
                    print("\033[H\033[J")   # Rensar typ terminalen. Det gör så att det blir enklare att se saker och ting
                    index = 0 # återställer alla variabler så du kan köra igen. Försökte hitta ett bättre sätt men allt jag kunde hitta på google var hur man raderar dom fullständigt
                    current_bet = 0
                    player_hand = []
                    dealer_hand = []
                    card = []
                    poker.start_game()
                elif restart == "no":
                    quit()

# Gör så att vi kan kalla på våra funktioner inom klassen genom att göra dom till variabler
playergame = Playergame()
poker = Poker()
dealer = Dealer()


poker.start_game()
