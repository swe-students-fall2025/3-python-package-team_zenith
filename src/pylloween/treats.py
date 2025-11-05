import random
from collections import Counter
from typing import Dict, List, Tuple, Optional

_DEFAULT_BAG: Dict[str, float] = {
    "chocolate_bar": 10.0,
    "gummy_worms": 6.0,
    "lollipop": 4.0,
    "candy_corn": 5.0,
    "pretzel": 2.0,
    "toothbrush": 1.0, 
}

def trick_or_treat(
    n: int = 10,
    bag: Optional[Dict[str, float]] = None,
    seed: Optional[int] = None,
) -> Tuple[List[str], Dict[str, int]]:
    """
    Extract n Halloween candies.
    -Bag: {Item: Weight}, if not passed, use _deFAULTRA-BAG
    -Seed: The result can be reproduced after setting (convenient for CI)
    Return (picks, counts):
    -Picks: Sampling sequence of length n
    -Counts: The number of times each item has been drawn
    """
    if n <= 0:
        raise ValueError("n must be >= 1")
    bag = dict(bag) if bag is not None else dict(_DEFAULT_BAG)
    if not bag:
        raise ValueError("bag cannot be empty")
    if any(w <= 0 for w in bag.values()):
        raise ValueError("all weights must be > 0")

    rng = random.Random(seed) if seed is not None else random
    items = list(bag.keys())
    weights = [float(bag[k]) for k in items]
    picks = rng.choices(items, weights=weights, k=n)
    counts = dict(Counter(picks))
    return picks, counts

def normalize_bag(bag: Dict[str, float]) -> Dict[str, float]:
    """Transform weight into Probability"""
    total = sum(bag.values())
    if total <= 0:
        raise ValueError("sum of weights must be > 0")
    return {k: v / total for k, v in bag.items()}