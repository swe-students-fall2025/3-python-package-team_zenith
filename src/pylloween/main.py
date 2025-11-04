import argparse
from .drawGhost import ghost_story, ghost_idea

def main():
    parser = argparse.ArgumentParser(description="👻 Pylloween — spooky fun in your terminal!")
    parser.add_argument("--story", choices=["short", "medium", "long"], help="Hear a random ghost story.")
    parser.add_argument("--movie", choices=["horror", "comedy", "cartoon", "all"], help="Get a Halloween movie idea!")
    args = parser.parse_args()

    if args.story:
        ghost_story(args.story)
    elif args.movie:
        ghost_idea(args.movie)
    else:
        ghost_story("medium")  # default behavior
