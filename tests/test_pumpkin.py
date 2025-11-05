import pytest
from pylloween.pumpkin import draw_pumpkin, PUMPKIN_STYLES

def _capture_printed(style, capsys):
    draw_pumpkin(style)
    out = capsys.readouterr().out
    
    if out.endswith("\n"):
        out = out[:-1]
    return out

def test_style_1_exact(capsys):
    out = _capture_printed(1, capsys)
    assert out == PUMPKIN_STYLES[1]

def test_style_2_exact(capsys):
    out = _capture_printed("2", capsys)
    assert out == PUMPKIN_STYLES[2]

def test_style_3_exact(capsys):
    out = _capture_printed(3, capsys)
    assert out == PUMPKIN_STYLES[3]

def test_style_4_exact(capsys):
    out = _capture_printed(4, capsys)
    assert out == PUMPKIN_STYLES[4]

def test_random_prints_something(capsys):
    draw_pumpkin()  # 随机
    out = capsys.readouterr().out
    assert len(out.strip()) > 0

def test_multiple_random_calls_vary_or_valid(capsys):
    draw_pumpkin()
    a = capsys.readouterr().out
    draw_pumpkin()
    b = capsys.readouterr().out
    assert a != b or len(a) > 0

def test_string_key_equivalent_to_int(capsys):
    a = _capture_printed("3", capsys)
    b = _capture_printed(3, capsys)
    assert a == b

def test_invalid_style_value_raises():
    with pytest.raises(ValueError):
        draw_pumpkin(999)

def test_invalid_style_type_raises():
    with pytest.raises(TypeError):
        draw_pumpkin(style=3.14)