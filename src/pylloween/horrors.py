import random


short_stories = [
        "The mirror blinked when I didn’t.",
        "Someone knocked from inside the coffin.",
        "I woke up to my own voice whispering from the hallway.",
        "My dog stared at the door. Then I heard my own voice calling from outside.",
        "The baby monitor picked up breathing before I turned it on."
    ]

medium_stories = [
        "It was raining again. My dog stared at the door, tail between his legs. Then I heard my own voice calling from outside. "
        "I don’t own a dog anymore.",
        "The phone buzzed at 3AM. A text from Mom: 'Come downstairs.' She’s been dead for ten years.",
        "The lights flickered, and I saw my reflection smile even though I didn’t move."
    ]

long_stories = [
        "When the town’s sirens wailed, everyone ran underground. But tonight, the sound came from below. "
        "The ground shook as something started knocking from under the soil. "
        "By morning, every basement had a new door built into the floor.",
        "I used to talk to my reflection as a kid. It used to talk back. "
        "When I broke the mirror, the voice didn’t stop. It just moved to the window."
    ]

stories = {"short": short_stories, "medium": medium_stories, "long": long_stories}

def get_horror(length: str = "medium")-> str:
    """
    Return a random horror story based on the given length.

    Parameters
    ----------
    length : str
        One of {"short", "medium", "long"}.

    Returns
    -------
    str
        A randomly chosen horror story.
    """
    
    if length not in stories:
        return (
            "💀 Pause, don't look behind!!! "
            "Instead, look at your input — you've typed an invalid parameter.\n"
            "(Choose from 'short', 'medium', or 'long'.)"
        )
        
    return random.choice(stories[length])

print(get_horror())