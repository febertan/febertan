from unittest import TestCase

from test import harommal_oszthatok


class TestHarommalOszthato(TestCase):

    def test_harommal_oszthatok_1(self):
        self.assertEqual(harommal_oszthatok([1, 2, 3]), 1)

    def test_harommal_oszthatok_2(self):
        self.assertEqual(harommal_oszthatok([1, 3, 3, 0, -7]), 2)

    def test_harommal_oszthatok_3(self):
        self.assertEqual(harommal_oszthatok([-3, 27, -111]), 3)

    def test_harommal_oszthatok_0(self):
        self.assertEqual(harommal_oszthatok([1, 112, 1000, 5000, 245]), 0)

    def test_harommal_oszthatok_ures_0(self):
        self.assertEqual(harommal_oszthatok([]), 0)
