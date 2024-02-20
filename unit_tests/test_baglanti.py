# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error
import unittest
from internet.baglanti import Baglanti


class TestIndir(unittest.TestCase):
    def setUp(self):
        self.baglanti = Baglanti()

    def test_response_code_200(self):
        sonuc = self.baglanti.indir()

        self.assertIsNotNone(sonuc, str)
