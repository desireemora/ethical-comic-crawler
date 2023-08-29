# test_comic_title.py

import unittest

from models.comic_title import ComicTitle

class TestComicTitle (unittest.TestCase):
    def setUp(self):
        """Set up sample comcis for use in all unit tests."""
        self.comic = ComicTitle("Wicked and the Divine (2014)", "#1", "#45", "2014 - 2019", "Image")
        self.comic_one_shot = ComicTitle("Wicked and The Divine Christmas Annual (2017 Image)","#1", None, "2017","Image")
        self.comic_tpb = ComicTitle("Wicked and the Divine TPB (2014-2019 Image)","#1","#9","2014 - 2015","Image")
    
    def test_is_tpb(self):
        """Testing that trade paper backs comics returns true"""
        self.assertEqual(self.comic_tpb.is_tpb(), True)

        """Testing that non trade paper backs comics returns false"""
        self.assertEqual(self.comic.is_tpb(), False)
        self.assertEqual(self.comic_one_shot.is_tpb(), False)