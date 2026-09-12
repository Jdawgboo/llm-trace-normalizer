"""Normalize LLM trace events into a stable comparison format."""
from __future__ import annotations

from typing import Any


def normalize(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep comparable fields and order events by timestamp then sequence."""
    normalized = []
    for sequence, event in enumerate(events):
        normalized.append({
            "timestamp": str(event.get("timestamp", "")),
            "kind": str(event.get("kind", "unknown")),
            "name": str(event.get("name", "")),
            "status": str(event.get("status", "unknown")),
            "sequence": sequence,
        })
    return sorted(normalized, key=lambda item: (item["timestamp"], item["sequence"]))
