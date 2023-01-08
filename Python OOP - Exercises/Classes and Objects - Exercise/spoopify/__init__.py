class Band():

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album}."
        return f"Band {album} already has {self.name} in their library."

    def remove_album(self, album_name: str):
        for show in self.albums:
            if show.name in self.albums and show.published:
                return f"Album has been published. It cannot be removed."
        if album_name in self.albums:
            self.albums.remove(album_name)
            return f"Album {album_name} has been removed."
        elif album_name not in self.albums:
            return f"Album {self.name} is not found."

    def details(self):
        result = f"Band {self.name}"
        for group in self.albums:
            result += f"\n{group}"
        return result