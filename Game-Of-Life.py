# Alan Yi


from war_classes import *


# Part I
def create_deck():
    clubs = []
    spades= []
    diamonds = []
    hearts = []
    for n in range(13):
        clubs.append(Card(n, 0))
        spades.append(Card(n, 1))
        diamonds.append(Card(n, 2))
        hearts.append(Card(n, 3))

    return clubs + spades + diamonds + hearts


# Part II
def deal_cards(deck):
    player1 = Player(1, 0, [])
    player2 = Player(2, 0,[])
    for n in range(0, len(deck),2):
        player1._cards.append(deck[n])
        player2._cards.append(deck[n+1])


    return player1, player2


# Part III
def play_normal_round(player1, player2):
    score = 0
    while len(player1._cards) > 0 and len(player2._cards) > 0:
        score += 2
        player1_card = player1.draw_card()
        player2_card = player2.draw_card()

        if player1_card._rank > player2_card._rank:
            player1._score += score
            return player1._player_num, player1._score

        elif player2_card._rank > player1_card._rank:
            player2._score += score
            return player2._player_num, player2._score

    if player1._score == 0 and player2._score == 0:
        return 0,0


# Part IV
def check_game_winner(player1, player2):
    if player1._score > player2._score:
        return 1
    elif player1._score < player2._score:
        return 2
    else:
        return 0



# Part V
def play_with_suits(player1, player2):
    score = 0
    while len(player1._cards) > 0 and len(player2._cards) > 0:
        score += 2
        player1_card = player1.draw_card()
        player2_card = player2.draw_card()

        if player1_card._suit ==3 and (player2_card._suit == 1 or player2_card._suit == 2):
            player1._score += score
            return player1._player_num, player1._score

        elif player2_card._suit == 3 and (player1_card._suit == 1 or player1_card._suit ==2):
            player2._score += score
            return player2._player_num, player2._score

        elif player1_card._suit == 1 and (player2_card._suit == 2 or player2_card._suit == 0):
            player1._score += score
            return player1._player_num, player1._score

        elif player2_card._suit == 1 and (player1_card._suit ==2 or player1_card._suit == 0):
            player2._score += score
            return player2._player_num, player2._score

        elif player1_card._suit == 2 and player2_card._suit == 0:
            player1._score += score
            return player1._player_num, player1._score

        elif player2_card._suit == 2 and player1_card._suit ==0:
            player2._score += score
            return player2._player_num, player2._score #return player 2

        elif player1_card._suit == 0 and player2_card._suit == 3:
            player1._score += score
            return player1._player_num, player1._score

        elif player2_card._suit ==0 and player1_card._suit == 3:
            player2._score += score
            return player2._player_num, player2._score #return player 2






# Part VI
def play_with_scouts(player1, player2):
    score = 0
    while len(player1._cards) > 0 and len(player2._cards) > 0:
        score += 2

        player1_card = player1.draw_card()
        player2_card = player2.draw_card()

        p1total = player1_card._rank + 2
        p2total = player2_card._rank + 2

        if player1_card._rank <= 3 and len(player1._cards) > 0:
            score += 1
            player1_card1 = player1.draw_card()

            p1total += player1_card1._rank + 2  #<--- draw another card for player 1

        if player2_card._rank <= 3 and len(player2._cards) > 0:
            score += 1
            player2_card2 = player2.draw_card()
            p2total += player2_card2._rank + 2   #<--- Draw another card for player 2

        print(player1_card._rank)
        print(player2_card._rank)

        if p1total > p2total:
            player1._score += score
            return player1._player_num, score

        elif p2total > p1total:
            player2._score += score
            return player2._player_num, score


 
    return 0,0

