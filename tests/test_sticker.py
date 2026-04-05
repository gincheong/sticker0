# tests/test_sticker.py
from sticker0.sticker import Sticker, StickerColor, BorderType, StickerPosition, StickerSize


def test_sticker_defaults():
    s = Sticker()
    assert s.title == ""
    assert s.content == ""
    assert s.color == StickerColor.NONE
    assert s.border == BorderType.ROUNDED
    assert s.position.x == 0
    assert s.position.y == 0
    assert s.size.width == 30
    assert s.size.height == 10
    assert s.id != ""


def test_sticker_roundtrip():
    s = Sticker(title="Test", content="Hello", color=StickerColor.BLUE)
    d = s.to_dict()
    s2 = Sticker.from_dict(d)
    assert s2.id == s.id
    assert s2.title == "Test"
    assert s2.content == "Hello"
    assert s2.color == StickerColor.BLUE


def test_sticker_color_none_roundtrip():
    from sticker0.sticker import StickerColor
    s = Sticker(color=StickerColor.NONE)
    d = s.to_dict()
    assert d["color"] == "none"
    s2 = Sticker.from_dict(d)
    assert s2.color == StickerColor.NONE


def test_new_sticker_default_color_is_none():
    from sticker0.sticker import StickerColor
    s = Sticker()
    assert s.color == StickerColor.NONE


def test_sticker_touch_updates_timestamp():
    import time
    s = Sticker()
    before = s.updated_at
    time.sleep(0.01)
    s.touch()
    assert s.updated_at > before
