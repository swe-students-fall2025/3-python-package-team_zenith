from ghosts import draw_ghost
from pumpkin import draw_pumpkin
from bat import draw_bat
import random

def draw_random():
    choice = random.randint(1,3)

    if choice == 1:
        return draw_ghost()
    elif choice == 2:
        return draw_pumpkin()
    elif choice ==3:
        return draw_bat()
    
    return None