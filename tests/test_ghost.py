import re
from pylloween import draw_ghost

def test_draw_ghost_prints_expected(capsys):
    draw_ghost()
    out = capsys.readouterr().out

    expected = "\n".join([
        "      ⣴⣿⣿⣿⣦",
        "    ⣰⣿⡟⢻⣿⡟⢻⣧",
        "   ⣰⣿⣿⣇⣸⣿⣇⣸⣿",
        "  ⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿",
        "⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇",
        "⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀",
        " ⠈⠿⠿⠋⠙⢿⣿⡿⠁",
        ""
    ])
    assert out == expected