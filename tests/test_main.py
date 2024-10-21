import unittest
from src.main import (
    gerade_zahlen,
    quadrierte_zahlen,
    gefilterte_woerter,
    flache_liste
)

class TestListComprehension(unittest.TestCase):

    def test_gerade_zahlen(self):
        erwartete_ausgabe = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        self.assertEqual(erwartete_ausgabe, gerade_zahlen())

    def test_quadrierte_zahlen(self):
        zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        erwartete_ausgabe = [25, 36, 49, 64, 81, 100]
        self.assertEqual(erwartete_ausgabe, quadrierte_zahlen(zahlen))

    def test_gefilterte_woerter(self):
        woerter = ['apfel', 'banane', 'kirsche', 'dattel', 'erdbeere', 'feige', 'traube']
        erwartete_ausgabe = ['erdbeere']
        self.assertEqual(erwartete_ausgabe, gefilterte_woerter(woerter))

    def test_flache_liste(self):
        verschachtelte_liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        erwartete_ausgabe = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(erwartete_ausgabe, flache_liste(verschachtelte_liste))

if __name__ == '__main__':
    unittest.main()
