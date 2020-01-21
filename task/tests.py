from django.test import TestCase

# Create your tests here.
import unittest
from .services import Utils

class UniqueIdTest(unittest.TestCase):
    def testGenSameNamespaceUniqueIP(self):
        for _ in range(100):
            m = [Utils('abc',_)._unique_id() for _ in range(100)]
            self.assertEqual(len(m), len(set(m)), "Error, duplicates found !")

    def testGenDiffNamespaceSameIP(self):
        for _ in range(100):
            m = [Utils(_, '192.168.1.1')._unique_id() for _ in range(100)]
            self.assertEqual(len(m), len(set(m)), "Error, duplicates found !")

    def testSameNameSpaceSameIP(self):
        for _ in range(100):
            m = [Utils('abc', '192.168.1.1')._unique_id() for _ in range(100)]
            self.assertEqual(len(m), len(set(m)), "Error, duplicates found !")