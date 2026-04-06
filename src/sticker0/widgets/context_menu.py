# src/sticker0/widgets/context_menu.py
from __future__ import annotations
from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Button
from textual.message import Message


class ContextMenu(Widget):
    """스티커 우클릭 팝업 메뉴."""

    DEFAULT_CSS = """
    ContextMenu {
        position: absolute;
        width: 20;
        height: auto;
        background: $surface;
        layer: menu;
    }
    ContextMenu Button {
        width: 1fr;
        height: 1;
        border: none;
        background: transparent;
    }
    ContextMenu Button:hover {
        background: $accent 20%;
    }
    """

    class MenuAction(Message):
        def __init__(self, action: str, sticker_id: str) -> None:
            super().__init__()
            self.action = action
            self.sticker_id = sticker_id

    def __init__(
        self,
        sticker_id: str,
        x: int,
        y: int,
        indicator: str = "white",
        minimized: bool = False,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.sticker_id = sticker_id
        self._menu_x = x
        self._menu_y = y
        self._indicator = indicator
        self._minimized = minimized

    def on_mount(self) -> None:
        self.styles.offset = (self._menu_x, self._menu_y)
        self.styles.border = ("round", self._indicator)
        self.styles.color = self._indicator

    def compose(self) -> ComposeResult:
        if self._minimized:
            yield Button("복원", id="menu-restore", variant="default")
        else:
            yield Button("편집", id="menu-edit", variant="default")
            yield Button("최소화", id="menu-minimize", variant="default")
        yield Button("프리셋 변경", id="menu-preset", variant="default")
        yield Button("삭제", id="menu-delete", variant="error")
        yield Button("닫기", id="menu-close", variant="default")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        event.stop()
        if event.button.id == "menu-close":
            self.remove()
            return
        action_map = {
            "menu-edit": "edit",
            "menu-delete": "delete",
            "menu-preset": "preset",
            "menu-minimize": "minimize",
            "menu-restore": "restore",
        }
        action = action_map.get(event.button.id or "", "")
        if action:
            self.post_message(self.MenuAction(action, self.sticker_id))
            self.remove()
