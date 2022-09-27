import abc

class Die(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    def __repr__(self) -> str:
        return f"{self.face}"

    @abc.abstractmethod
    def roll(self) -> None:
        ...