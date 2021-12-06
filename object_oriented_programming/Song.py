class Song:
    """Class to represent a song.

    Attributes:
        title (str): the title of the song.
        artist (artist) : An artist representing the song creator.
        duration (int) : Duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        # """Song init method.
        #
        # :param title: Initialises the title attribute
        # :param artist: An artist object representing the song's creator.
        # :param duration (optional [int]): Initial value for the 'duration' attribute.
        #         will default to zero if not specified"""
        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song)
# help(Song.__init__)
# print(Song.__init__.__doc__)
# Song.__init__.__doc__ = """Song init method.
#
# :param title: Initialises the title attribute
# :param artist: An artist object representing the song's creator.
# :param duration (optional [int]): Initial value for the 'duration' attribute.
#         will default to zero if not specified"""
# help(Song)


class Album:
    """Class to represent an album, using it's track list

    Attributes:
        name (str) : The name of the album.
        year (int) : The year album was released.
        artist (Artist) : The artist responsible for the album. If not specified the artist
                    will default to be named "Various Artists".
        tracks (List[Song]) : A list of the songs of the album.

    Methods:
        add_song: Used the add a new to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to the track list.

        :param song: A song to add.
        :param position: (Optional[int]):If specified , the song will be added to that position
                in the track list - inserting it between the other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        :return:
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.
    Attributes:
        name(str): The name of the artist.
        albums (List[Album]) : A list of album by this artist.
                    The list includes only those albums in this collection, it is not an exhaustive
                    list of artist's published albums.
        Methods :
            add_album: Use to add a new album to the artist's album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """

        :param album:(Album) Album object to add to the list.
                if the album is already present, It will not be added again.(Although this
                 is not yet implemented
        :return:
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open("albums.txt","r") as albums:
        for line in albums:
            # data row should consist of (artist,album,year,song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field, sep="; ")


if __name__ == "__main__":
    load_data()