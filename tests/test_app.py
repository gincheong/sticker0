# tests/test_app.py
import pytest
from sticker0.app import Sticker0App
from sticker0.sticker import Sticker, StickerColor
from sticker0.storage import StickerStorage


@pytest.fixture
def tmp_storage(tmp_path):
    return StickerStorage(data_dir=tmp_path)


@pytest.mark.asyncio
async def test_app_launches(tmp_storage):
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        assert app.is_running


@pytest.mark.asyncio
async def test_sticker_widget_renders_title(tmp_storage):
    s = Sticker(title="My Note", content="Hello")
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        from sticker0.widgets.sticker_widget import StickerWidget
        widgets = app.query(StickerWidget)
        assert len(widgets) == 1
        assert widgets.first().sticker.title == "My Note"
