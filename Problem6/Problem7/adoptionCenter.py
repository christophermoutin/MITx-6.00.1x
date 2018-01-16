class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        # Your Code Here
        self.name = name
        self.species_types = species_types
        self.location = tuple([float(i) for i in location])
    def get_number_of_species(self, animal):
        # Your Code Here
        if animal not in self.species_types.keys():
            return 0
        else:
            return self.species_types[animal]
    def get_location(self):
        # Your Code Here 
        return self.location
    def get_species_count(self):
        # Your Code Here 
        return self.species_types.copy()
    def get_name(self):
        # Your Code Here 
        return self.name
    def adopt_pet(self, species):
        # Your Code Here 
        if self.species_types[species] <= 1:
            del self.species_types[species]
        else:
            self.species_types[species] -= 1
