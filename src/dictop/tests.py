import os
import unittest
from .core import select
from .core import update


class TestDictop(unittest.TestCase):

    def test01(self):
        data = {
            "a": {
                "b": "a.b",
            }
        }
        value = select(data, "a.b")
        assert value == "a.b"
        if os.sys.version.startswith("2.6"):
            self.assertRaises(KeyError, lambda:select(data, "b", slient=False))
        else:
            with self.assertRaises(KeyError):
                select(data, "b", slient=False)
            

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
        if os.sys.version.startswith("2.6"):
            self.assertRaises(KeyError, lambda:select(data, "a.b.c", slient=False))
        else:
            with self.assertRaises(KeyError):
                select(data, "a.b.c", slient=False)
            

    def test04(self):
        data = [{
            "a": {
                "b": "0.a.b",
            }
        }]
        assert select(data, "0.a.b") == "0.a.b"
        if os.sys.version.startswith("2.6"):
            self.assertRaises(KeyError, lambda:select(data, "1", slient=False))
        else:
            with self.assertRaises(KeyError):
                select(data, "1", slient=False)

    def test05(self):
        class DATA(object):
            x = [{
                "a": {
                    "b": "x.0.a.b",
                }
            }]
        data = DATA()
        assert select(data, "x.0.a.b") == "x.0.a.b"

    def test06(self):
        data = {
            "a": 1,
        }
        update(data, "a", 2)
        assert select(data, "a") == 2

    def test07(self):
        data = {}
        update(data, "a", 2)
        assert select(data, "a") == 2

    def test08(self):
        data = {
            "a": {
                "a": 1,
            }
        }
        update(data, "a.b", 2)
        assert select(data, "a.b") == 2

    def test09(self):
        data = [{
            "a": 1
        }]
        update(data, "0.a", 2)
        assert select(data, "0.a") == 2
        update(data, "1.a", 2)
        assert select(data, "1.a") == 2

    def test10(self):
        data = [1,2,3]
        update(data, "3", 4)
        assert data[3] == 4

    def test11(self):
        data = {}
        update(data, "a.b.c.d", 2)
        assert select(data, "a.b.c.d") == 2

    def test12(self):
        class DATA(object):
            pass
        data = DATA()
        update(data, "a.b.c.d", 2)
        assert select(data, "a.b.c.d", 2)

    def test13(self):
        class DATA(object):
            pass
        data = DATA()
        update(data, "a", 2)
        assert data.a == 2
