import unittest
from .core import select


class TestDictop(unittest.TestCase):

    def test01(self):
        data = {
            "a": {
                "b": "a.b",
            }
        }
        value = select(data, "a.b")
        assert value == "a.b"
        with self.assertRaises(KeyError):
            select(data, "b")

    def test02(self):
        data = {
            "a": {
                "b": "a.b",
            }
        }
        value = select(data, "a.b.c")
        assert value is None

    def test03(self):
        data = {
            "a": {
                "b": "a.b",
            }
        }
        with self.assertRaises(KeyError):
            select(data, "a.b.c", slient=False)

    def test04(self):
        data = [{
            "a": {
                "b": "0.a.b",
            }
        }]
        assert select(data, "0.a.b") == "0.a.b"
        with self.assertRaises(KeyError):
            select(data, "1")

    def test05(self):
        class DATA(object):
            x = [{
                "a": {
                    "b": "x.0.a.b",
                }
            }]
        data = DATA()
        assert select(data, "x.0.a.b") == "x.0.a.b"

