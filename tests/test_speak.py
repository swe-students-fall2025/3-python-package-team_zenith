import pytest
from halloween.speak import ghost_speak_random
from PIL import Image

def test_ghost_speak_random_basic():
    img, story = ghost_speak_random(seed=42)
    assert isinstance(img, Image.Image)
    assert isinstance(story, str)
    assert len(story) > 0

def test_ghost_speak_random_seed_deterministic():
    _, story1 = ghost_speak_random(seed=1)
    _, story2 = ghost_speak_random(seed=1)
    assert story1 == story2

def test_ghost_speak_random_invalid_csv(tmp_path):
    fake_path = tmp_path / "not_exist.csv"
    with pytest.raises(FileNotFoundError):
        ghost_speak_random(csv_path=str(fake_path))