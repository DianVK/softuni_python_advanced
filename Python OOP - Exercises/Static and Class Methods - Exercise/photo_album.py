class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []

    @classmethod
    def from_photos_count(cls,photos_count: int):
        return cls(photos_count)

    def add_photo(self,label: str):
        if not self.photos:
            for x in range(self.pages):
                self.photos.append([])

        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        output = "-----------\n"
        for x in self.photos:
            current_page = ""
            for y in x:
                current_page += "[] "
            output += current_page
            output += "\n-----------\n"

        return output.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


# from math import ceil
#
#
# class PhotoAlbum:
#
#     def __init__(self, pages):
#         self.pages = pages
#         self.photos = [[] for _ in range(pages)]
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         return cls(ceil(photos_count / 4))
#
#     def add_photo(self, label: str):
#         for row in range(len(self.photos)):
#             if len(self.photos[row]) < 4:
#                 self.photos[row].append(label)
#                 return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
#         return "No more free slots"
#
#     def display(self):
#         output = ["-----------",]
#         for row in range(len(self.photos)):
#             how_long = len(self.photos[row])
#             if how_long > 0:
#                 pics = "[] " * how_long
#             else:
#                 pics = ""
#             output.append(pics.rstrip())
#             output.append("-----------")
#         return "\n".join(output)