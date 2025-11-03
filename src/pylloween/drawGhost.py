"""
ghosts.py — Functions related to ghost drawings and interactions.

This module provides:
1. draw_ghost()  → Draws an ASCII ghost.
2. ghost_say()   → Displays a speech bubble and then the ghost.
3. ghost_story() → Makes the ghost tell a horror story using horrors.get_horror().
"""
import random
import horrors  # Imports the horror story generator

GHOST_STYLES = {
    1: """
      ⣴⣿⣿⣿⣦
    ⣰⣿⡟⢻⣿⡟⢻⣧
   ⣰⣿⣿⣇⣸⣿⣇⣸⣿
  ⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
 ⠈⠿⠿⠋⠙⢿⣿⡿⠁
""",
    2: """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀
⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀
⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀
⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀
⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    3: """
⠀⠀⠄⠀⠀⠂⠀⠀⠀⡀⠀⠀
⠁⠀⠀⣠⣶⣿⣷⣶⣄⠀⠀⠁
⠈⠀⢰⡿⠛⢿⡿⠻⣿⡆⠀⡀
⠀⠠⣾⡇⠀⢸⡇⠀⢸⣧⠀⠀
⠀⠀⣿⣷⣤⣿⣷⣤⣿⣿⠀⠀
⠠⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⡀
⠄⡀⠙⠟⢿⣿⡿⠿⠿⠋⠀⠀
"""
}

def draw_ghost():
    """
    Prints a cute ASCII ghost to the console.

    This function only handles the visual part — no message or logic.
    Example:
        draw_ghost()
    """
    s = random.choice([1,2,3])
    print(GHOST_STYLES[s])


def ghost_say(message: str = "I'm haunting your terminal! Zelle me 50 or I'll overflow your stack."):
    """
    Prints a ghost speech bubble with the given message, followed by the ghost itself.

    Parameters
    ----------
    message : str, optional
        The text that the ghost will say (default: a spooky warning).

    Example
    -------
    >>> ghost_say("Boo!")
      _______
     < Boo! >
      -------
          ⣴⣿⣿⣿⣦
        ⣰⣿⡟⢻⣿⡟⢻⣧
        ...
    """
    # Remove extra spaces from user input
    msg = message.strip()

    # Calculate the bubble width (message length + padding)
    width = len(msg) + 4

    # Print the top border of the speech bubble
    print("  " + "_" * width)

    # Print the main message line
    print(f" < {msg} >")

    # Print the bottom border
    print("  " + "-" * width)

    # Finally, draw the ghost under the message
    draw_ghost()


def ghost_story(length: str = "medium"):
    """
    Makes the ghost tell a horror story from the horrors module.

    Parameters
    ----------
    length : str, optional
        The desired story length: "short", "medium", or "long" (default: "medium").

    Behavior
    --------
    Calls horrors.get_horror(length) to fetch a random story,
    and then displays it inside the ghost's speech bubble.
    """
    story = horrors.get_horror(length)
    ghost_say(story)


# Demo behavior when this file is run directly
if __name__ == "__main__":
    ghost_say()
