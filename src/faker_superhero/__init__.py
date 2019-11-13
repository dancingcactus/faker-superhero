"""Provider for Faker which adds fake microservice names."""

from faker.providers import BaseProvider

ADJECTIVES = [
    "Big", "Invisible", "Turbo", "Rescue", "Ice", "Green", "Fly", "Iron", "Mis-Direction", "Gas",
    "Stunt", "Captian", "Spy", "lion"
]

MALE_NOUNS = [
    "man", "guy", "boy"
]

MALE_PREFIXES = [
    "Mr.", "Sir", "President", "The"
]

FEMALE_NOUNS = [
    "girl", "woman", "widow", "lady",
]

FEMALE_PREFIXES = [
    "Mrs.", "Ms.", "The"
]

NEUTRAL_NOUNS = [
    "person", "hero", "diviner", "rockstar", "gnome", "saint", "centapede"
]

class Provider(BaseProvider):
    """Provider for Faker which adds fake Super Hero Names"""
    def _no_gender(self):
        nouns = MALE_NOUNS + FEMALE_NOUNS + NEUTRAL_NOUNS
        return f'{self.random_element(ADJECTIVES)} {self.random_element(nouns)}'


    def _male(self):
        nouns = MALE_NOUNS + NEUTRAL_NOUNS
        prefix = self.random_element([self.random_element(MALE_PREFIXES),""])
        if prefix:    
            name =  f'{prefix }{self.random_element(ADJECTIVES)} {self.random_element(nouns)}'
        else:
            name = f'{prefix} {self.random_element(ADJECTIVES)} {self.random_element(nouns)}'
        return name
    
    def _female(self):
        nouns = FEMALE_NOUNS + NEUTRAL_NOUNS
        prefix = self.random_element([self.random_element(FEMALE_PREFIXES),""])
        if prefix:    
            name =  f'{prefix }{self.random_element(ADJECTIVES)} {self.random_element(nouns)}'
        else:
            name = f'{prefix} {self.random_element(ADJECTIVES)} {self.random_element(nouns)}'
        return name
    
    def _neutral(self):
        nouns = NEUTRAL_NOUNS
        return f'{self.random_element(ADJECTIVES)} {self.random_element(nouns)}'

    def superhero(self, gender=False):
        """ Fake Super Hero Names """
        if gender :
            if str(gender).lower() == "male":
                return self._male()
            elif str(gender).lower() == "female":
                return self._female()
            elif str(gender).lower() == "neutral":
                return self._neutral()
        else:
            return self._no_gender()