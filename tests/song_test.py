import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Ice, Ice, Baby", "Vanilla Ice")
    
    def test_song_title(self):
        self.assertEqual("Ice, Ice, Baby", self.song.title)
    
    def test_song_artist(self):
        song = Song("Ice, Ice, Baby", "Vanilla Ice")
        self.assertEqual("Vanilla Ice", self.song.artist)
    
   