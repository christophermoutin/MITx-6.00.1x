class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        # Your Code Here
        self.name = name
        self.desired_species = desired_species        
    def get_name(self):
        # Your Code Here
        return self.name 
    def get_desired_species(self):
        # Your Code Here
        return self.desired_species 
    def get_score(self, adoption_center):
        # Your Code Here
        score = adoption_center.get_number_of_species(self.desired_species)
        return float(score) 
