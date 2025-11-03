"""
ghosts.py — Functions related to ghost drawings and interactions.

This module provides:
1. draw_ghost()  → Draws an ASCII ghost.
2. ghost_say()   → Displays a speech bubble and then the ghost.
3. ghost_story() → Makes the ghost tell a horror story using horrors.get_horror().
"""
import random
from typing import Optional, Union
try:
    # Prefer package-relative import when available
    from . import horrors  # type: ignore
except ImportError:  # pragma: no cover - fallback for direct execution
    import horrors  # type: ignore  # Fallback for running module as a script

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

def draw_ghost(style: Optional[Union[int, str]] = None):
    """
    Prints a cute ASCII ghost to the console.

    Parameters
    ----------
    style : int | str | None, optional
        Pick a specific ghost style by its numeric key.
        When omitted or None, a random style is chosen.

    This function only handles the visual part — no message or logic.
    Example:
        draw_ghost(2)
    """
    if style is None:
        chosen_style = random.choice(list(GHOST_STYLES.keys()))
    else:
        if isinstance(style, str):
            try:
                chosen_style = int(style)
            except ValueError as exc:
                raise ValueError("style must be an integer key matching the available ghost styles") from exc
        elif isinstance(style, int):
            chosen_style = style
        else:
            raise TypeError("style must be an int, str, or None")

        if chosen_style not in GHOST_STYLES:
            raise ValueError(f"style must be one of {sorted(GHOST_STYLES.keys())}")

    print(GHOST_STYLES[chosen_style])


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
