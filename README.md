# Fake Superhero Name Generator

Provider for [Faker](https://faker.readthedocs.io/en/master/) adds fake superhero names. Find your next super hero name with library.

## Installation

```python
pipenv install faker-microservice
```

## Usage

### Python

```python
from faker import Faker

import faker_superhero

fake = Faker()
fake.add_provider(faker_superhero.Provider)
print(fake.superhero())  # prints "Turbo Girl " or similar
print(fake.superhero("male"))  # prints super hero names for males
print(fake.superhero("female"))  # prints super hero names for females
print(fake.superhero("female"))  # prints super hero names that aren't gender specific
print()
```

### Command Line

```bash
pipenv run faker superhero -i faker_superhero
```
