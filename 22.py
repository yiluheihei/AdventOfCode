def read_file(file):
    with open(file) as f:
        cards = f.read().splitlines()
    
    player2_idx = cards.index('Player 2:')
    player1 = cards[1:player2_idx - 1]
    player2 = cards[player2_idx + 1:]
    player2 = [int(x) for x in player2]
    player1 = [int(x) for x in player1]
    
    return player1, player2
    

player1, player2 = read_file('input/22_input.txt')

def part1():
    player1, player2 = read_file('input/22_input.txt')
    while len(player1) > 0 and len(player2) > 0:
        v1 = player1.pop(0)
        v2 = player2.pop(0)
        if v1 > v2:
            player1 += [v1, v2]
        elif v1 < v2:
            player2 += [v2, v1]
        else:
            AssertionError("error")
        
    
    winner = player1 if len(player1) > 0 else player2
    factor = range(len(winner), 0, -1)
    score = sum([int(winner[i]) * factor[i] for i in range(len(winner))])
    
    return score
    


## part 2

def run_recursive_game(p1, p2):
    p1_cards = [tuple(p1)]
    p2_cards = [tuple(p2)]
    while len(p1) > 0 and len(p2) > 0:
        v1 = p1.pop(0)
        v2 = p2.pop(0)
        
        #sub game
        if v1 <= len(p1) and v2 <= len(p2):
            sub_p1 = p1[:v1]
            sub_p2 = p2[:v2]
            # sub_p1_cards = [sub_p1]
            # sub_p2_cards = [sub_p2]
            sub_winner, _ = run_recursive_game(sub_p1, sub_p2)
        
            if sub_winner == "p1":
                winner = "p1"
                p1 += [v1, v2]
            else:
                winner = "p2"
                p2 += [v2, v1]
        
            # if p1 in p1_cards or p2 in p2_cards:
            #     winner = "p1"
            #     winner_cards = p1
        
            p1_cards += p1
            p2_cards += p2
        else:
            if v1 > v2:
                p1 += [v1, v2]
                winner = "p1"
            elif v1 < v2:
                p2 += [v2, v1]
                winner = "p2"
            else:
                AssertionError("error")
            
            if tuple(p1) in p1_cards or tuple(p2) in p2_cards:
                winner = "p1"
                winner_cards = p1
                break
            
            p1_cards += [tuple(p1)]
            p2_cards += [tuple(p2)]
            
    
    if len(p1) > 0:
        winner = "p1"
        winner_cards = p1
    else:
        winner = "p2"
        winner_cards = p2
            
    # winner, winner_cards = run_recursive_game(p1, p2) 
            
    return winner, winner_cards
        


def part2():
    p1, p2 = read_file('input/22_input.txt')
    
    _, cards, = run_recursive_game(p1, p2)
    factor = range(len(cards), 0, -1)
    score = sum([cards[i] * factor[i] for i in range(len(cards))])
    
    return score
    
# 32528
part2()
    
####### test
p1 = [9, 2, 6, 3, 1]
p2 = [5, 8, 4, 7, 10]
_, cards = run_recursive_game(p1, p2)
factor = range(len(cards), 0, -1)
# 291
score = sum([cards[i] * factor[i] for i in range(len(cards))])
    

    
            
        
    