import abc

class MediaLoader(abc.ABC):
    @abc.abstractmethod
    def play(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...

class Wav(MediaLoader): 
    pass

class Ogg(MediaLoader): 
    ext = ".ogg"
    def __init__(self) -> None:
        self.ext = ".ogg"

    def play(self) -> None: 
        print(f"playing a Ogg extension")