import random

print("Let's Play")
print()
print("Instructions")
print("*Please on Caps lock while playing this game")
print("*Order of entering cards eg:-AH=A of Hearts or 7D=7 of Diamonds")
print()
print("Welcome to Omi")
print("-----------------------------------------------------------------")

computer_p = 0  # for the final score
human_p = 0  # for the final score

deck = []  # Unshuffled Deck Seen
deck_b = []  # Unshuffled Deck Unseen
shuffle = []  # Shuffled Deck Seen
shuffle_b = []  # Shuffled Deck Unseen

computer = []  # for the background
computer_seen = []  # to output
computer_for_t = []  # for the shuffling tactics

# Humans cards
human_deck = []
human_deck_unseen = []
# temporary deck fot checking cards with the same suit
human_choice = []

TRUMP_C = ""  # when the computer chooses trumps
TRUMP_H = ""  # when the human chooses trumps

y = 0
count_c = 0  # to check who plays next
count_h = 0  # to check who plays next

round_count = 0

main_number = ["7", "8", "9", "10", "J", "Q", "K", "A"]
background = [1, 2, 3, 4, 5, 6, 7, 8]
suit = ["S", "C", "H", "D"]

another_round = "Y"


def shuffling_algo():
    # Printing 32 cards
    for main in range(len(main_number)):
        for suits in range(len(suit)):
            deck.append(str(main_number[main]) + str(suit[suits]))
    for back in range(len(background)):
        for suits in range(len(suit)):
            deck_b.append(str(background[back]) + str(suit[suits]))

    # Shuffling Algorithm
    for choice in range(len(deck)):
        x = random.randrange(0, len(deck))
        shuffle.append(str(deck[x]))
        shuffle_b.append(str(deck_b[x]))
        deck.remove(str(deck[x]))
        deck_b.remove(str(deck_b[x]))


# Computer gets cards
def computers_cards_computer_trumps():
    for i in range(0, 4):
        computer_seen.append(str(shuffle[i]))
        computer.append(str(shuffle_b[i]))
        computer_for_t.append(str(shuffle_b[i]))  # for the tactics(for the computer to choose trumps)
    # Computer gets the rest of the cards
    for z in range(8, 12):
        computer.append(shuffle_b[z])
        computer_seen.append(str(shuffle[z]))
    # print("Computer:",computer_seen )


# Human gets cards
def human_computer_trumps():
    for x in range(4, 8):
        human_deck.append(shuffle[x])
        human_deck_unseen.append(shuffle_b[x])
    for y in range(12, 16):
        human_deck.append(shuffle[y])
        human_deck_unseen.append(shuffle_b[y])
    print("Your cards are: ", human_deck)


def computer_human_trumps():
    for i in range(4, 8):
        computer_seen.append(str(shuffle[i]))
        computer.append(str(shuffle_b[i]))
    # Computer gets the rest of the cards
    for z in range(12, 16):
        computer.append(shuffle_b[z])
        computer_seen.append(str(shuffle[z]))
    # print("Computers cards are: ", computer_seen)


# Tactics
def tactics():
    import random
    x = random.randrange(0, 4)

    # all 4 suits are equal
    if computer_for_t[0][1] == computer_for_t[1][1] == computer_for_t[2][1] == computer_for_t[3][1]:
        return computer_for_t[0][1]

    # 3 suits are equal
    elif computer_for_t[0][1] == computer_for_t[1][1] == computer_for_t[2][1]:
        return computer_for_t[0][1]

    elif computer_for_t[0][1] == computer_for_t[2][1] == computer_for_t[3][1]:
        return computer_for_t[0][1]

    elif computer_for_t[0][1] == computer_for_t[1][1] == computer_for_t[3][1]:
        return computer_for_t[0][1]

    elif computer_for_t[2][1] == computer_for_t[1][1] == computer_for_t[3][1]:
        return computer_for_t[2][1]

    # 2 suits are equal and other 2 are equal
    elif computer_for_t[0][1] == computer_for_t[1][1] and computer_for_t[2][1] == computer_for_t[3][1]:
        if computer_for_t[0][0] == 8 or computer_for_t[1][0] == 8:
            return computer_for_t[2][1]
        elif computer_for_t[2][0] == 8 or computer_for_t[3][0] == 8:
            return computer_for_t[3][1]
        else:
            return computer_for_t[x][1]

    elif computer_for_t[0][1] == computer_for_t[2][1] and computer_for_t[1][1] == computer_for_t[3][1]:
        if computer_for_t[0][0] == 8 or computer_for_t[2][0] == 8:
            return computer_for_t[1][1]
        elif computer_for_t[1][0] == 8 or computer_for_t[3][0] == 8:
            return computer_for_t[2][1]
        else:
            return computer_for_t[x][1]

    elif computer_for_t[0][1] == computer_for_t[3][1] and computer_for_t[1][1] == computer_for_t[2][1]:
        if computer_for_t[0][0] == 8 or computer_for_t[3][0] == 8:
            return computer[2][1]
        elif computer_for_t[1][0] == 8 or computer_for_t[2][0] == 8:
            return computer_for_t[3][1]
        else:
            return computer_for_t[x][1]



    # only 2 suits are equal
    elif computer_for_t[0][1] == computer_for_t[1][1]:
        return computer_for_t[0][1]

    elif computer_for_t[0][1] == computer_for_t[2][1]:
        return computer_for_t[0][1]

    elif computer_for_t[0][1] == computer_for_t[3][1]:
        return computer_for_t[0][1]

    elif computer_for_t[1][1] == computer_for_t[2][1]:
        return computer_for_t[1][1]

    elif computer_for_t[1][1] == computer_for_t[3][1]:
        return computer_for_t[1][1]

    elif computer_for_t[2][1] == computer_for_t[3][1]:
        return computer_for_t[2][1]

    # If all 4 suits are different
    else:
        return computer_for_t[x][1]


# the final result of the round
def results():
    if computer_p == human_p:
        print()
        print("Your Score: " + str(human_p) + " / Computers score:" + str(computer_p))
        print("Its a tie")
        print()

    elif computer_p > human_p:
        print()
        print("Your Score: " + str(human_p) + " / Computers score:" + str(computer_p))
        print("Computer won")
        print()

    elif computer_p < human_p:
        print()
        print("Your Score: " + str(human_p) + " / Computers score:" + str(computer_p))
        print("You won")
        print()


while another_round == "Y":


    if round_count % 2 == 0:  # even numbers the computer will call trumps
        round_count += 1
        print("Round", round_count)
        print()
        # Computer calls trumps
        count_trump=0
        wheres_trumps=False
        while wheres_trumps==False:
            shuffling_algo()
            computers_cards_computer_trumps()
            TRUMP_C = tactics()
            print("Trump is:",TRUMP_C)
            human_computer_trumps()
            for q in range(0,len(computer_seen)):
                if human_deck[q][-1]==TRUMP_C:
                    count_trump+=1
                    wheres_trumps = True
            if count_trump==0:
                print("You dont have Trumps, would you like to proceed: (Y/N)")
                want_to_play = str(input())
                if want_to_play == "N":
                    print("Ok lets shuffle again")
                    deck.clear()  # Unshuffled Deck Seen
                    deck_b.clear()  # Unshuffled Deck Unseen
                    shuffle.clear()  # Shuffled Deck Seen
                    shuffle_b.clear()  # Shuffled Deck Unseen

                    computer.clear()  # for the background
                    computer_seen.clear()  # to output
                    computer_for_t.clear()  # for the shuffling tactics
                    # Humans cards
                    human_deck.clear()
                    human_deck_unseen.clear()
                    continue
                else:
                    wheres_trumps = True


        # Playing Rules
        # when human plays first
        print("Trick 1")
        # print("Computers hand:", computer_seen)
        print("Trump is:", TRUMP_C)
        x = input("Your call: ")  # human puts the card
        test = True
        while test == True:

            if x in human_deck:

                choice = []  # computers cards with the same suit goes here

                # computer chooses the card with the same suit
                for y in range(0, len(computer_seen)):
                    if computer_seen[y][-1] == x[-1]:
                        choice.append(computer_seen[y])

                if len(choice) != 0:
                    for_choice = random.randrange(0, len(choice))
                    print("Computers card: ", choice[for_choice])
                    # checking who is higher
                    if computer[computer_seen.index(choice[for_choice])][0] > human_deck_unseen[human_deck.index(x)]:
                        count_c += 1
                        print("Computer wins +2")
                        computer_p += 2

                    else:
                        count_h += 1
                        print("You win +2")
                        human_p += 2

                    human_deck_unseen.pop(human_deck.index(x))
                    human_deck.remove(x)
                    computer.pop(computer_seen.index(choice[for_choice]))  # To remove the value in the unseen deck
                    computer_seen.remove(choice[for_choice])
                    # print(computer)
                    choice.clear()

                # if no similar suit, computer chooses a random card
                else:
                    r = random.randrange(0, len(computer_seen))
                    print("Computer choice:", computer_seen[r])
                    # if the random card is a trump
                    if computer[computer_seen.index(computer_seen[r])][1] == TRUMP_C:
                        count_c += 1
                        print("Computer wins +2")
                        computer_p += 2
                    # if random card is not a trump
                    else:
                        count_h += 1
                        print("You win +2")
                        human_p += 2
                    human_deck_unseen.pop(human_deck.index(x))
                    human_deck.remove(x)
                    computer.pop(computer_seen.index(computer_seen[r]))
                    computer_seen.remove(computer_seen[r])
                test = False

            else:
                print("Please enter a card in your deck: ")
                x = input("Your call: ")
        trick_no = 1

        while len(computer_seen) > 0:
            trick_no += 1
            print("------------")
            print("Trick ", trick_no)
            game = False  # to check whether the human deck has the same suit played by the computer
            print("Trump is:", TRUMP_C)

            if count_c > count_h:
                count_c = 0

                print("Your cards are: ", human_deck)
                s = random.randrange(0, len(computer_seen))  # Computers card
                print("Computers card: ", computer_seen[s])
                for t in range(0, len(human_deck)):
                    if computer_seen[s][1] == human_deck[t][-1]:  # Checking the suit(for same suit)
                        game = True
                        human_choice.append(human_deck[t])

                h = input("Your call: ")
                condition = True
                while condition == True:
                    if h in human_deck:
                        condition = False
                        if game == True:
                            eraser = True
                            while eraser == True:
                                if h in human_choice:  # same suit human rule
                                    eraser = False
                                    if human_deck_unseen[human_deck.index(h)][0] > computer[s][0]:

                                        print("You win +2")
                                        count_h += 1
                                        human_p += 2
                                        human_deck_unseen.pop(human_deck.index(h))
                                        human_deck.remove(h)
                                        computer.pop(computer_seen.index(computer_seen[s]))
                                        computer_seen.remove(computer_seen[s])
                                        human_choice.clear()

                                    else:

                                        print("Computer wins +2")
                                        count_c += 1
                                        computer_p += 2
                                        human_deck_unseen.pop(human_deck.index(h))
                                        human_deck.remove(h)
                                        computer.pop(computer_seen.index(computer_seen[s]))
                                        computer_seen.remove(computer_seen[s])
                                        human_choice.clear()

                                else:

                                    print("Enter a card with the same suit", computer_seen[s][-1])
                                    h = input("Your call")
                        # if no same suits in the human_deck
                        else:
                            if h[-1] == TRUMP_C:
                                print("You win +2")
                                count_h += 1
                                human_p += 2
                                human_deck_unseen.pop(human_deck.index(h))
                                human_deck.remove(h)
                                computer.pop(computer_seen.index(computer_seen[s]))
                                computer_seen.remove(computer_seen[s])


                            else:
                                print("Computer wins +2")
                                count_c += 1
                                computer_p += 2
                                human_deck_unseen.pop(human_deck.index(h))
                                human_deck.remove(h)
                                computer.pop(computer_seen.index(computer_seen[s]))
                                computer_seen.remove(computer_seen[s])

                    else:

                        print("Please enter a card in your deck: ")
                        h = input("Your call: ")

            # if human wins first trick
            elif count_h > count_c:
                count_h = 0
                print("Your cards are: ", human_deck)
                h2 = input("Your call: ")
                y = 0
                choice = []  # computers cards with the same suit goes here
                human_test = True
                while human_test == True:
                    if h2 in human_deck:
                        human_test = False
                        # computer chooses the card with the same suit
                        for y in range(0, len(computer_seen)):
                            if computer_seen[y][-1] == h2[-1]:
                                choice.append(computer_seen[y])

                        if len(choice) != 0:
                            for_choice = random.randrange(0, len(choice))
                            print("Computers card: ", choice[for_choice])
                            # checking who is higher
                            if computer[computer_seen.index(choice[for_choice])][0] > \
                                    human_deck_unseen[human_deck.index(h2)][
                                        0]:

                                print("Computer wins +2")
                                count_c += 1
                                computer_p += 2
                                human_deck_unseen.pop(human_deck.index(h2))
                                human_deck.remove(h2)
                                computer.pop(
                                    computer_seen.index(choice[for_choice]))  # To remove the value in the unseen deck
                                computer_seen.remove(choice[for_choice])
                                # print(computer)
                                choice.clear()
                            else:

                                print("You win +2")
                                count_h += 1

                                human_p += 2
                                human_deck_unseen.pop(human_deck.index(h2))
                                human_deck.remove(h2)
                                computer.pop(
                                    computer_seen.index(choice[for_choice]))  # To remove the value in the unseen deck
                                computer_seen.remove(choice[for_choice])
                                # print(computer)
                                choice.clear()



                        # if no similar suit, computer chooses a random card
                        else:
                            r = random.randrange(0, len(computer_seen))
                            print("Computer choice:", computer_seen[r])
                            # if the random card is a trump
                            if computer[computer_seen.index(computer_seen[r])][1] == TRUMP_C:

                                print("Computer wins +2")
                                count_c += 1
                                computer_p += 2

                                human_deck_unseen.pop(human_deck.index(h2))
                                human_deck.remove(h2)
                                computer.pop(computer_seen.index(computer_seen[r]))
                                computer_seen.remove(computer_seen[r])
                            # if random card is not a trump
                            else:

                                print("You win +2")
                                count_h += 1
                                human_p += 2

                                human_deck_unseen.pop(human_deck.index(h2))
                                human_deck.remove(h2)
                                computer.pop(computer_seen.index(computer_seen[r]))
                                computer_seen.remove(computer_seen[r])
                    else:

                        print("Please enter a card in your deck: ")
                        h2 = input("Your call: ")
        results()

        computer_p = 0
        human_p = 0

        # clearing the decks after the round is over
        deck.clear()  # Unshuffled Deck Seen
        deck_b.clear()  # Unshuffled Deck Unseen
        shuffle.clear()  # Shuffled Deck Seen
        shuffle_b.clear()  # Shuffled Deck Unseen

        computer.clear()  # for the background
        computer_seen.clear()  # to output
        computer_for_t.clear()  # for the shuffling tactics

        # Humans cards
        human_deck.clear()
        human_deck_unseen.clear()

        trick_no = 1

        count_c = 0  # to check who plays next
        count_h = 0  # to check who plays next

        print("Do you want to play another round? (Y/N)")
        another_round = str(input())
        # checking for Y and N and whether its only Y and N
        play_again = True
        while play_again == True:
            if another_round == "Y":
                print("OK lets play again")
                play_again = False
            elif another_round == "N":
                print("Thank you for playing")
                break
            else:
                print("Please enter a valid response")
                another_round = str(input())

    # When the human calls trumps
    elif round_count % 2 == 1:  # odd numbers human calls trumps
        round_count += 1
        print("Round", round_count)
        print()
        count_trump = 0
        wheres_trumps = False
        while wheres_trumps == False:
            shuffling_algo()
            # Human Trumps human cards and human calling trumps
            for x in range(0, 4):
                human_deck.append(shuffle[x])
                human_deck_unseen.append(shuffle_b[x])
            print("Your first 4 cards are:", human_deck)
            print("Please select a suit for trumps")
            print()
            speak = True
            while speak == True:
                human_trump = str(input("Choose H for Hearts, S for Spades, C for Clubs and D for Diamonds: "))
                if human_trump in suit:
                    TRUMP_H = human_trump
                    print("Trump is: ", TRUMP_H)
                    speak = False

                else:
                    print("Please choose a valid trump")

            for y in range(8, 12):
                human_deck.append(shuffle[y])
                human_deck_unseen.append(shuffle_b[y])
            print("Your cards are: ", human_deck)

            computer_human_trumps()
            for q in range(0, len(computer_seen)):
                if computer_seen[q][-1] == TRUMP_H:
                    count_trump += 1
                    wheres_trumps = True
            if count_trump == 0:
                print("Computer doesnt have trumps so must shuffle again")
                deck.clear()  # Unshuffled Deck Seen
                deck_b.clear()  # Unshuffled Deck Unseen
                shuffle.clear()  # Shuffled Deck Seen
                shuffle_b.clear()  # Shuffled Deck Unseen

                computer.clear()  # for the background
                computer_seen.clear()  # to output
                computer_for_t.clear()  # for the shuffling tactics
                # Humans cards
                human_deck.clear()
                human_deck_unseen.clear()
                continue

        # trick 1
        print("Trick 1")
        test_h = True
        while test_h == True:
            c = random.randrange(0, len(computer_seen))
            print("Computers choice: ", computer_seen[c])
            for t in range(0, len(human_deck)):
                if computer_seen[c][1] == human_deck[t][-1]:  # Checking the suit(for same suit)
                    game = True
                    human_choice.append(human_deck[t])
            h1 = input("Your call: ")
            condition = True
            while condition == True:
                if h1 in human_deck:
                    condition = False
                    if game == True:
                        eraser = True
                        while eraser == True:
                            if h1 in human_choice:  # same suit human rule
                                eraser = False
                                if human_deck_unseen[human_deck.index(h1)][0] > computer[c][0]:
                                    print("You win +2")
                                    test_h = False
                                    count_h += 1
                                    human_p += 2
                                    human_deck_unseen.pop(human_deck.index(h1))
                                    human_deck.remove(h1)
                                    computer.pop(computer_seen.index(computer_seen[c]))
                                    computer_seen.remove(computer_seen[c])
                                    human_choice.clear()

                                else:

                                    print("Computer wins +2")
                                    test_h = False
                                    count_c += 1
                                    computer_p += 2
                                    human_deck_unseen.pop(human_deck.index(h1))
                                    human_deck.remove(h1)
                                    computer.pop(computer_seen.index(computer_seen[c]))
                                    computer_seen.remove(computer_seen[c])
                                    human_choice.clear()

                            else:
                                print("Enter a card with the same suit: ", computer_seen[c][-1])
                                h1 = input("Your call: ")
                    # if no same suits in the human_deck
                    else:

                        if h1[-1] == TRUMP_H:
                            test_h = False
                            print("You win +2")
                            count_h += 1
                            human_p += 2
                            human_deck_unseen.pop(human_deck.index(h1))
                            human_deck.remove(h1)
                            computer.pop(computer_seen.index(computer_seen[c]))
                            computer_seen.remove(computer_seen[c])


                        else:
                            test_h = False
                            print("Computer wins +2")
                            count_c += 1
                            computer_p += 2
                            human_deck_unseen.pop(human_deck.index(h1))
                            human_deck.remove(h1)
                            computer.pop(computer_seen.index(computer_seen[c]))
                            computer_seen.remove(computer_seen[c])

                else:
                    print("Please enter a card in your deck: ")
                    h1 = input("Your call: ")

        while len(computer_seen) > 0:
            trick_no += 1
            print("------------")
            print("Trick ", trick_no)
            game = False  # to check whether the human deck has the same suit played by the computer
            print("Trump is:", TRUMP_H)

            if count_c > count_h:
                count_c = 0

                print("Your cards are: ", human_deck)
                s = random.randrange(0, len(computer_seen))  # Computers card
                print("Computers card: ", computer_seen[s])
                for t in range(0, len(human_deck)):
                    if computer_seen[s][1] == human_deck[t][-1]:  # Checking the suit(for same suit)
                        game = True
                        human_choice.append(human_deck[t])

                h = input("Your call: ")

                condition = True
                while condition == True:
                    if h in human_deck:
                        condition = False
                        if game == True:
                            eraser = True
                            while eraser == True:
                                if h in human_choice:  # same suit human rule
                                    eraser = False
                                    if human_deck_unseen[human_deck.index(h)][0] > computer[s][0]:
                                        print("You win +2")
                                        count_h += 1
                                        human_p += 2
                                        human_deck_unseen.pop(human_deck.index(h))
                                        human_deck.remove(h)
                                        computer.pop(computer_seen.index(computer_seen[s]))
                                        computer_seen.remove(computer_seen[s])
                                        human_choice.clear()

                                    else:

                                        print("Computer wins +2")
                                        count_c += 1
                                        computer_p += 2
                                        human_deck_unseen.pop(human_deck.index(h))
                                        human_deck.remove(h)
                                        computer.pop(computer_seen.index(computer_seen[s]))
                                        computer_seen.remove(computer_seen[s])
                                        human_choice.clear()

                                else:

                                    print("Enter a card with the same suit: ", computer_seen[s][-1])
                                    h = input("Your call: ")
                        # if no same suits in the human_deck
                        else:

                            if h[-1] == TRUMP_H:

                                print("You win +2")
                                count_h += 1
                                human_p += 2
                                human_deck_unseen.pop(human_deck.index(h))
                                human_deck.remove(h)
                                computer.pop(computer_seen.index(computer_seen[s]))
                                computer_seen.remove(computer_seen[s])


                            else:
                                print("Computer wins +2")
                                count_c += 1
                                computer_p += 2
                                human_deck_unseen.pop(human_deck.index(h))
                                human_deck.remove(h)
                                computer.pop(computer_seen.index(computer_seen[s]))
                                computer_seen.remove(computer_seen[s])

                    else:

                        print("Please enter a card in your deck: ")
                        h = input("Your call: ")

            # if human wins first trick
            elif count_h > count_c:
                count_h = 0
                print("Your cards are: ", human_deck)
                h2 = input("Your call: ")
                y = 0
                choice = []  # computers cards with the same suit goes here
                if h2 in human_deck:
                    # computer chooses the card with the same suit
                    for y in range(0, len(computer_seen)):
                        if computer_seen[y][-1] == h2[-1]:
                            choice.append(computer_seen[y])

                    if len(choice) != 0:
                        for_choice = random.randrange(0, len(choice))
                        print("Computers card: ", choice[for_choice])
                        # checking who is higher
                        if computer[computer_seen.index(choice[for_choice])][0] > \
                                human_deck_unseen[human_deck.index(h2)][
                                    0]:

                            print("Computer wins +2")
                            count_c += 1
                            computer_p += 2

                            human_deck_unseen.pop(human_deck.index(h2))
                            human_deck.remove(h2)
                            computer.pop(
                                computer_seen.index(choice[for_choice]))  # To remove the value in the unseen deck
                            computer_seen.remove(choice[for_choice])
                            # print(computer)
                            choice.clear()
                        else:

                            print("You win +2")
                            count_h += 1

                            human_p += 2
                            human_deck_unseen.pop(human_deck.index(h2))
                            human_deck.remove(h2)
                            computer.pop(
                                computer_seen.index(choice[for_choice]))  # To remove the value in the unseen deck
                            computer_seen.remove(choice[for_choice])
                            # print(computer)
                            choice.clear()



                    # if no similar suit, computer chooses a random card
                    else:
                        r = random.randrange(0, len(computer_seen))
                        print("Computer choice:", computer_seen[r])
                        # if the random card is a trump
                        if computer[computer_seen.index(computer_seen[r])][1] == TRUMP_H:

                            print("Computer wins +2")
                            count_c += 1
                            computer_p += 2

                            human_deck_unseen.pop(human_deck.index(h2))
                            human_deck.remove(h2)
                            computer.pop(computer_seen.index(computer_seen[r]))
                            computer_seen.remove(computer_seen[r])
                        # if random card is not a trump
                        else:

                            print("You win +2")
                            count_h += 1
                            human_p += 2

                            human_deck_unseen.pop(human_deck.index(h2))
                            human_deck.remove(h2)
                            computer.pop(computer_seen.index(computer_seen[r]))
                            computer_seen.remove(computer_seen[r])

                else:

                    print("Please enter a card in your deck: ")
                    h2 = input("Your call: ")

        # Showing the final result after the round, the function is written at the top
        results()

        # clearing all the variables and the lists used in the round
        computer_p = 0
        human_p = 0

        # clearing the decks after the round is over
        deck.clear()  # Unshuffled Deck Seen
        deck_b.clear()  # Unshuffled Deck Unseen
        shuffle.clear()  # Shuffled Deck Seen
        shuffle_b.clear()  # Shuffled Deck Unseen

        computer.clear()  # for the background
        computer_seen.clear()  # to output
        computer_for_t.clear()  # for the shuffling tactics

        # Humans cards
        human_deck.clear()
        human_deck_unseen.clear()

        trick_no = 1

        count_c = 0  # to check who plays next
        count_h = 0  # to check who plays next

        print("Do you want to play another round? (Y/N)")
        another_round = str(input())

        # checking for Y and N and whether its only Y and N
        play_again = True
        while play_again == True:
            if another_round == "Y":
                print("OK lets play again")
                play_again = False
            elif another_round == "N":
                print("Thank you for playing")
                break
            else:
                print("Please enter a valid response")
                another_round = str(input())



