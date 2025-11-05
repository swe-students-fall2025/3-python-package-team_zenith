import math
from pylloween.treats import trick_or_treat, normalize_bag

def test_trick_or_treat_reproducible_with_seed():
    a = trick_or_treat(n=12, seed=2025)
    b = trick_or_treat(n=12, seed=2025)
    assert a == b

def test_trick_or_treat_counts_sum_to_n():
    picks, counts = trick_or_treat(n=25, seed=7)
    assert len(picks) == 25
    assert sum(counts.values()) == 25

def test_trick_or_treat_custom_bag_only_contains_custom_items():
    bag = {"choco": 3, "corn": 1}
    picks, counts = trick_or_treat(n=20, bag=bag, seed=0)
    assert set(counts).issubset(set(bag))

def test_normalize_bag_basic():
    probs = normalize_bag({"a": 1, "b": 3})
    assert math.isclose(probs["a"] + probs["b"], 1.0, rel_tol=1e-9)
    assert math.isclose(probs["b"] / probs["a"], 3.0, rel_tol=1e-9)