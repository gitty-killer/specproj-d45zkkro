"""Data models."""

from dataclasses import dataclass

@dataclass
class Record:
    key: str
    value: str

@dataclass
class Result:
    items: list

