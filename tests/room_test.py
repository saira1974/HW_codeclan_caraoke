import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest



class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Ice Ice Baby", "Vanilla Ice")
        self.song_2 = Song("Greatest Day", "Take That")
        self.song_3 = Song("Especially for You", "Kylie and Jason")
        

        self.songs = [self.song_1, self.song_2, self.song_3]
    
        self.nevan = Guest("Nevan", self.song_1)
        self.inaya = Guest("Inaya", self.song_2)
        self.olly = Guest("Olly", self.song_3)

        self.guests = [self.nevan, self.inaya, self.olly]
        self.room = Room("The Cheesy Pop Room")

    
    def test_room_name(self):
        self.assertEqual("The Cheesy Pop Room", self.room.name)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.nevan)
        self.assertEqual(1, self.room.number_of_guests())
    
    def test_check_guest_out(self):
        self.room.check_in_guest(self.nevan)
        self.room.check_out_guest(self.nevan)
        self.assertEqual(0, self.room.number_of_guests())
    
    def test_room_name(self):
        self.assertEqual("The Cheesy Pop Room", self.room.name)
    