import random

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():  
    return [v + " " + s for s in suits for v in values] * 4

def deal_cards(deck, num_players=3, cards_per_player=5):
    random.shuffle(deck)
    return [deck[i * cards_per_player:(i + 1) * cards_per_player] for i in range(num_players)]

def calculate_score(hand):
    score = 0
    suit_count = {}
    value_count = {}
    
    for card in hand:
        value, suit = card.split(" ")
        
        if value.isdigit():
            score += int(value)
        elif value == 'Jack':
            score += 11
        elif value == 'Queen':
            score += 12
        elif value == 'King':
            score += 13
        elif value == 'Ace':
            score += 20
        
        suit_count[suit] = suit_count.get(suit, 0) + 1
        value_count[value] = value_count.get(value, 0) + 1
    return score, suit_count, value_count

def determine_losers(players):
    scores = []
    for player in players:
        score, suit_count, value_count = calculate_score(player['hand'])
        scores.append({
            'player': player,
            'score': score,
            'max_suit': max(suit_count.values()) if suit_count else 0,
            'max_value': max(value_count.values()) if value_count else 0
        })
    
    scores.sort(key=lambda x: (x['score'], -x['max_suit'], -x['max_value']))

    lowest = scores[0]
    losers = [
        p['player'] for p in scores
        if (p['score'], p['max_suit'], p['max_value']) ==
           (lowest['score'], lowest['max_suit'], lowest['max_value'])
    ]

    if len(losers) == len(players):
        return [], scores

    return losers, scores

def main():
    players = []
    num_players = 3
    
    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        players.append({'name': name, 'hand': []})
    
    
    while len(players) > 1:
        deck = create_deck()
        hands = deal_cards(deck, len(players))
        
        for i in range(len(players)):
            players[i]['hand'] = hands[i]

        for player in players:
            print(f"{player['name']}'s hand: {player['hand']}")
        
        for player in players:
            change_card = input(f"{player['name']}, do you want to change a card? (yes/no): ").strip().lower()
            if change_card == 'yes':
                card_to_change = input("Enter the card you want to change from your hand: ")
                if card_to_change in player['hand']:
                    new_card = random.choice(deck)
                    deck.remove(new_card)
                    player['hand'].remove(card_to_change)
                    player['hand'].append(new_card)
                    print(f"{player['name']} changed {card_to_change} to {new_card}.")
                else:
                    print("Card not found in hand.")
        
        for player in players:
            print(f"{player['name']}'s updated hand: {player['hand']}")
        
        losers, scores = determine_losers(players)

        if losers:
            print("\nEliminated player(s):")
            for loser in losers:
                print(f"- {loser['name']}")
            players = [p for p in players if p not in losers]
        else:
            print("It's a complete tie! No players eliminated this round.")
        
        print("Player Scores:")
        for entry in scores:
            print(f"{entry['player']['name']}: Score = {entry['score']}, "
                f"Max Suit Count = {entry['max_suit']}, Max Value Count = {entry['max_value']}")
    print(f"The final winner is {players[0]['name']}!")

if __name__ == "__main__":
    main()