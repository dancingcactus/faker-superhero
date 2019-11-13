# -*- coding: utf-8 -*-

import pytest
import unittest
from faker import Faker, Generator
import faker_superhero

__author__ = "Justin Grover"
__copyright__ = "Justin Grover"
__license__ = "mit"


class IntegrationTestCase(unittest.TestCase):
    """Integration Tests"""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_superhero.Provider)

    def test_integration(self):
        """Test integration with Faker."""
        superhero = self.fake.superhero()
        self.assertIsInstance(superhero, str, "Returns wrong type of variable")
        self.assertGreater(len(superhero), 1)

if __name__ == '__main__':
    unittest.main()