from abc import ABC, abstractmethod


class Media(ABC):
    @abstractmethod
    def play(self) -> str:
        pass


class Song(Media):
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def play(self) -> str:
        return f'Playing song: {self.title} - {self.artist}'


class Podcast(Media):
    def __init__(self, title: str, host: str):
        self.title = title
        self.host = host

    def play(self) -> str:
        return f'Playing podcast: {self.title} (host: {self.host})'


def play_all(items: list[Media]) -> list[str]:
    return [i.play() for i in items]


print(play_all([Song('Sky', 'A.'), Podcast('Tech', 'B')]))
