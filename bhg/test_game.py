import random


def ini_game(n):
    jewel_position = (random.randint(0, n - 1), random.randint(0, n - 1))
    
    while True:
        player_position = (random.randint(0, n - 1), random.randint(0, n - 1))
        if player_position != jewel_position:
            break
    
    return jewel_position, player_position




아ㅏㅏㅏㅏㅏㅏ