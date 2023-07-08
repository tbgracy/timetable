from dataclasses import dataclass

@dataclass
class Subject:
    label: str
    duration: int = 0