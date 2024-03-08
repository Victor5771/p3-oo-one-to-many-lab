class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)

# Testing the implementation

def test_owner_init():
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

def test_invalid_pet_type():
    try:
        pet = Pet("Tweety", "birdy")
    except Exception as e:
        assert str(e) == "Invalid pet type"

def test_owner_pets():
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Fluffy", "cat", owner)
    assert owner.pets() == [pet1, pet2]

def test_add_pet():
    owner = Owner("John")
    pet = Pet("Fido", "dog")
    owner.add_pet(pet)
    assert pet.owner == owner

def test_get_sorted_pets():
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Fluffy", "cat", owner)
    pet3 = Pet("Buddy", "dog", owner)
    assert owner.get_sorted_pets() == [pet2, pet3, pet1]

