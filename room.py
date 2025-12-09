class Room:
    """Represents a room in a house"""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.exits = []

    def add_exits(self, rooms: list) -> None:
        """Add exits (connections) to other rooms."""
        self.exits.extend(rooms)
