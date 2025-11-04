"""
function draws and returns a pumpkin
"""

import random
from ghosts import draw_ghost

def draw_pumpkin():
    """Draws and returns a pumpkin."""
    return """___
           ___)__|_
      .-*'          '*-,
     /      /|   |\     \
    ;      /_|   |_\     ;
    ;   |\           /|  ;
    ;   | ''--...--'' |  ;
     \  ''---.....--''  /
      ''*-.,_______,.-*'
"""
                
        
def draw_bat():
    
    return"""  _   ,_,   _
              / `'=) (='` \
             /.-.-.\ /.-.-.\ 
             `      "      `
             """

def draw_random():
    choice = random.randint(1,3)

    if choice == 1:
        return draw_ghost()
    elif choice == 2:
        return draw_pumpkin()
    elif choice ==3:
        return draw_bat()
    
    return None