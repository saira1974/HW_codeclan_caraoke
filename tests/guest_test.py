import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Ice Ice Baby", "Vanilla Ice")
        self.song_2 = Song("Greatest Day", "Take That")
        self.song_3 = Song("Especially for You", "Kylie and Jason")

        self.songs = [self.song_1, self.song_2, self.song_3]

        song = Song("Ice, Ice, Baby", "Vanilla Ice")
        self.guest = Guest("Nevan", song)
    
    def test_guest_has_name(self):
        self.assertEqual("Nevan", self.guest.name)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Ice, Ice, Baby", self.guest.favourite_song.title)
    
   
    
