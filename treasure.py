class Treasure:
    """Represents a collectible treasure item in a room."""

    def __init__(self, name: str, value: int, description: str) -> None:
        self.name = name
        self.value = value
        self.description = description

    def __str__(self) -> str:
        return f"{self.name} (worth {self.value} points)"
