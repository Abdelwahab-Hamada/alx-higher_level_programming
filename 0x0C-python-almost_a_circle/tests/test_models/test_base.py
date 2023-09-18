#!/usr/bin/python3
"""test_base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
