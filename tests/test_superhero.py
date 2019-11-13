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

    def test_male(self):
        """Test Male Super Hero Names """
        male = self.fake.superhero("male")
        self.assertIsInstance(male, str, "Returns wrong type of variable")
        self.assertIn(" ", male, "No space in name")
        noun = male.split(" ")[1]
        self.assertNotIn(noun, faker_superhero.FEMALE_NOUNS)

    def test_female(self):
        """Test Male Super Hero Names """
        female = self.fake.superhero("female")
        self.assertIsInstance(female, str, "Returns wrong type of variable")
        self.assertIn(" ", female, "No space in name")
        noun = female.split(" ")[1]
        self.assertNotIn(noun, faker_superhero.MALE_NOUNS)

    def test_neutral(self):
        """Test Male Super Hero Names """
        neutral = self.fake.superhero("neutral")
        self.assertIsInstance(neutral, str, "Returns wrong type of variable")
        self.assertIn(" ", neutral, "No space in name")
        noun = neutral.split(" ")[1]
        self.assertNotIn(noun, faker_superhero.MALE_NOUNS)
        self.assertNotIn(noun, faker_superhero.MALE_NOUNS)

if __name__ == '__main__':
    unittest.main()