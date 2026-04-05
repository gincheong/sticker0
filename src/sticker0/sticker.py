# src/sticker0/sticker.py
from __future__ import annotations
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class StickerColor(str, Enum):
    YELLOW = "yellow"
    BLUE = "blue"
    GREEN = "green"
    PINK = "pink"
    WHITE = "white"
    DARK = "dark"
    NONE = "none"


class BorderType(str, Enum):
    ROUNDED = "rounded"
    SHARP = "sharp"
    DOUBLE = "double"
    THICK = "thick"
    ASCII = "ascii"


@dataclass
class StickerPosition:
    x: int = 0
    y: int = 0


@dataclass
class StickerSize:
    width: int = 30
    height: int = 10


@dataclass
class Sticker:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    content: str = ""
    color: StickerColor = StickerColor.NONE
    border: BorderType = BorderType.ROUNDED
    position: StickerPosition = field(default_factory=StickerPosition)
    size: StickerSize = field(default_factory=StickerSize)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "color": self.color.value,
            "border": self.border.value,
            "position": {"x": self.position.x, "y": self.position.y},
            "size": {"width": self.size.width, "height": self.size.height},
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Sticker:
        now = datetime.now(timezone.utc).isoformat()
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            title=data.get("title", ""),
            content=data.get("content", ""),
            color=StickerColor(data.get("color", "none")),
            border=BorderType(data.get("border", "rounded")),
            position=StickerPosition(**data.get("position", {})),
            size=StickerSize(**data.get("size", {})),
            created_at=datetime.fromisoformat(data.get("created_at", now)),
            updated_at=datetime.fromisoformat(data.get("updated_at", now)),
        )

    def touch(self) -> None:
        self.updated_at = datetime.now(timezone.utc)
