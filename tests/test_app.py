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


@pytest.mark.asyncio
async def test_sticker_drag_moves_position(tmp_storage):
    s = Sticker(title="Drag me")
    s.position.x = 5
    s.position.y = 5
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        from sticker0.widgets.sticker_widget import StickerWidget
        widget = app.query_one(StickerWidget)
        # 타이틀바에서 드래그: widget 위치 기준 offset (2, 0) 에서 mouse down
        # widget.region = (5, 6) 이므로 screen_down = (7, 6)
        await pilot.mouse_down(widget, offset=(2, 0))
        await pilot.pause()
        # screen 절대좌표 (17, 11) 에서 mouse up -> delta (+10, +5)
        # new position = (5+10, 5+5) = (15, 10)
        await pilot.mouse_up(offset=(17, 11))
        await pilot.pause()
        assert widget.sticker.position.x == 15
        assert widget.sticker.position.y == 10


@pytest.mark.asyncio
async def test_sticker_resize_from_corner(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    s = Sticker(title="Resize me")
    s.size.width = 30
    s.size.height = 10
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        widget = app.query_one(StickerWidget)
        # 우하단 모서리(리사이즈 핸들)에서 드래그: 10x3 증가
        corner_offset = (s.size.width - 1, s.size.height - 1)
        await pilot.mouse_down(widget, offset=corner_offset)
        # mouse_up을 corner보다 +10, +3 위치에서
        corner_screen = (
            widget.region.x + corner_offset[0],
            widget.region.y + corner_offset[1],
        )
        await pilot.mouse_up(offset=(corner_screen[0] + 10, corner_screen[1] + 3))
        await pilot.pause()
        assert widget.sticker.size.width == 40
        assert widget.sticker.size.height == 13


@pytest.mark.asyncio
async def test_double_click_enters_edit_mode(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    from textual.widgets import TextArea
    s = Sticker(title="Edit me", content="original")
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        widget = app.query_one(StickerWidget)
        # 더블클릭 시뮬레이션: 빠른 연속 클릭
        await pilot.click(widget, offset=(5, 2))
        await pilot.click(widget, offset=(5, 2))
        await pilot.pause(0.1)
        assert len(app.query(TextArea)) >= 1


@pytest.mark.asyncio
async def test_escape_exits_edit_mode(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    from textual.widgets import TextArea
    s = Sticker(title="Edit me", content="original")
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        widget = app.query_one(StickerWidget)
        await pilot.click(widget, offset=(5, 2))
        await pilot.click(widget, offset=(5, 2))
        await pilot.pause(0.1)
        await pilot.press("escape")
        await pilot.pause(0.1)
        assert len(app.query(TextArea)) == 0


@pytest.mark.asyncio
async def test_right_click_shows_context_menu(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    from sticker0.widgets.context_menu import ContextMenu
    s = Sticker(title="Menu test")
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        widget = app.query_one(StickerWidget)
        await pilot.click(widget, button=3, offset=(5, 2))
        await pilot.pause(0.1)
        assert len(app.query(ContextMenu)) == 1


@pytest.mark.asyncio
async def test_context_menu_delete_removes_sticker(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    from sticker0.widgets.context_menu import ContextMenu
    s = Sticker(title="Delete via menu")
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        widget = app.query_one(StickerWidget)
        await pilot.click(widget, button=3, offset=(5, 2))
        await pilot.pause(0.1)
        menu = app.query_one(ContextMenu)
        await pilot.click(menu.query_one("#menu-delete"))
        await pilot.pause(0.1)
        assert len(app.query(StickerWidget)) == 0
        assert tmp_storage.load_all() == []


@pytest.mark.asyncio
async def test_press_n_creates_sticker(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        await pilot.press("n")
        await pilot.pause(0.1)
        assert len(app.query(StickerWidget)) == 1
        assert len(tmp_storage.load_all()) == 1


@pytest.mark.asyncio
async def test_color_change_via_context_menu(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    from sticker0.widgets.color_picker import ColorPicker
    from sticker0.sticker import StickerColor
    s = Sticker(title="Color test", color=StickerColor.YELLOW)
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        widget = app.query_one(StickerWidget)
        # 우클릭으로 컨텍스트 메뉴 열기
        await pilot.click(widget, button=3, offset=(5, 2))
        await pilot.pause(0.1)
        from sticker0.widgets.context_menu import ContextMenu
        menu = app.query_one(ContextMenu)
        # 색상 변경 버튼 클릭
        await pilot.click(menu.query_one("#menu-color"))
        await pilot.pause(0.1)
        # ColorPicker가 표시되어야 함
        assert len(app.query(ColorPicker)) == 1
        # 파란색 선택
        picker = app.query_one(ColorPicker)
        await pilot.click(picker.query_one("#color-blue"))
        await pilot.pause(0.1)
        # 스티커 색상이 변경되어야 함
        loaded = tmp_storage.load(s.id)
        assert loaded.color == StickerColor.BLUE


@pytest.mark.asyncio
async def test_context_menu_buttons_have_text_color(tmp_storage):
    """ContextMenu CSS에 color: $text 가 있어야 버튼 텍스트가 보임."""
    from sticker0.widgets.context_menu import ContextMenu
    s = Sticker(title="Menu test")
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        from sticker0.widgets.sticker_widget import StickerWidget
        widget = app.query_one(StickerWidget)
        await pilot.click(widget, button=3, offset=(5, 2))
        await pilot.pause(0.1)
        menu = app.query_one(ContextMenu)
        css = menu.DEFAULT_CSS
        assert "color: $text" in css


@pytest.mark.asyncio
async def test_focused_sticker_delete_with_d_key(tmp_storage):
    from sticker0.widgets.sticker_widget import StickerWidget
    s = Sticker(title="Press d")
    tmp_storage.save(s)
    app = Sticker0App(storage=tmp_storage)
    async with app.run_test(size=(120, 40)) as pilot:
        widget = app.query_one(StickerWidget)
        widget.focus()
        await pilot.pause(0.1)
        await pilot.press("d")
        await pilot.pause(0.1)
        assert len(app.query(StickerWidget)) == 0
        assert tmp_storage.load_all() == []
