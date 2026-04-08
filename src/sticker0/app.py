# src/sticker0/app.py
from __future__ import annotations
from textual.app import App, ComposeResult
from sticker0.config import AppConfig
from sticker0.storage import StickerStorage
from sticker0.widgets.board import StickerBoard


class Sticker0App(App):
    CSS = """
    Screen {
        layers: base stickers menu;
    }
    """

    BINDINGS = [
        ("n", "new_sticker", "New sticker"),
        ("ctrl+z", "undo_delete", "Undo delete"),
    ]

    def __init__(
        self,
        storage: StickerStorage | None = None,
        config: AppConfig | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.config = config if config is not None else AppConfig.load()
        self.storage = storage or StickerStorage()

    def action_new_sticker(self) -> None:
        board = self.query_one(StickerBoard)
        board.add_new_sticker()

    def action_undo_delete(self) -> None:
        board = self.query_one(StickerBoard)
        board.undo_delete()

    def compose(self) -> ComposeResult:
        yield StickerBoard(storage=self.storage, config=self.config)
