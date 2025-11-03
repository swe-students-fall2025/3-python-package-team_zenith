import random


short_stories = [
        "The mirror blinked when I didn’t.",
        "I just saw my reflection blink.",
        "Someone knocked from inside the coffin.",
        "I’m watching my girlfriend through the window. I wonder how much longer I need to keep the oven on.",
        "Quarantined... Without toilet paper.",
        "They celebrated the first successful cryogenic freezing. He had no way of letting them know he was still conscious.",
        "There was a picture in my phone of me sleeping. I swear I live alone.",
        "They say cats have 9 lives, but I swear I’ve buried him at least 11 times.",
        "I woke up to my own voice whispering from the hallway.",
        "My dog stared at the door. Then I heard my own voice calling from outside.",
        "The baby monitor picked up breathing before I turned it on."
    ]

medium_stories = [
        "It was raining again. My dog stared at the door, tail between his legs. Then I heard my own voice calling from outside. "
        "I don’t own a dog anymore.",
        "It actually really bothers me when people call black girls ‘chocolate’, and white girls ‘vanilla’ because neither taste any different than pork.",
        "I've been living with the love of my life for 5 years now, I think it's more than enough time to finally introduce myself.",
        "The existence of the uncanny valley suggests that in the past, our survival instincts had a reason to be afraid of something that looked human, but wasn't.",
        
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

halloween_movies = {
    "horror": {
        "Halloween (1978)",
        "A Nightmare on Elm Street",
        "Friday the 13th",
        "The Exorcist",
        "The Shining",
        "Psycho",
        "It (2017)",
        "It Follows",
        "The Conjuring",
        "Hereditary",
        "Midsommar",
        "Get Out",
        "Us",
        "The Blair Witch Project",
        "Poltergeist",
        "Child’s Play",
        "The Ring",
        "The Grudge",
        "Sinister",
        "Insidious",
        "The Babadook",
        "The Witch",
        "Crimson Peak",
        "The Cabin in the Woods",
        "The Evil Dead"
    },

    "comedy": {
        "Beetlejuice",
        "Ghostbusters (1984)",
        "Shaun of the Dead",
        "Practical Magic",
        "The Addams Family (1991)",
        "The Addams Family Values",
        "Edward Scissorhands",
        "Sleepy Hollow",
        "Scream",
        "Trick 'r Treat",
        "Army of Darkness"
    },

    "cartoon": {
        "Hocus Pocus",
        "The Nightmare Before Christmas",
        "Coraline",
        "Monster House",
        "Halloweentown",
        "ParaNorman",
        "Corpse Bride",
        "Casper",
        "The Haunting (1963)",
        "The Sixth Sense"
    }
}

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
    
    length = length.lower()
    
    if length not in stories:
        return (
            "💀 Pause, don't look behind!!! "
            "Instead, look at your input — you've typed an invalid parameter.\n"
            "(Choose from 'short', 'medium', or 'long'.)"
        )
        
    return random.choice(stories[length])

# print(get_horror())

def get_movie_idea(genre: str = "all") -> str:
    """Return a random Halloween movie based on genre.\n
    Parameters
    ---
    "horror", "cartoon", "comedy", "all"
    """
    
    genre = genre.lower()
    
    if genre == "all":
        all_movies = set().union(*halloween_movies.values())
        return "Genre: " + genre + "\n" + random.choice(list(all_movies))
    
    if genre in halloween_movies:
        return "Genre: " + genre + "\n" + random.choice(list(halloween_movies[genre]))
    
    return "Genre not found."

if __name__ == "__main__":
    get_movie_idea()