class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self,name,desired_species,considered_species):
        Adopter.__init__(self,name,desired_species)
        self.considered_species=considered_species
        
    def get_score(self, adoption_center):
        score = adoption_center.get_number_of_species(self.desired_species)
        for i in self.considered_species:
            score += adoption_center.get_number_of_species(i)*0.3    
        return float(score)


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self,name,desired_species,feared_species):
        Adopter.__init__(self,name,desired_species)
        self.feared_species=feared_species
        
    def get_score(self, adoption_center):
        score = adoption_center.get_number_of_species(self.desired_species)-adoption_center.get_number_of_species(self.feared_species)*0.3
        if score <= 0.0:
            return 0.0
        else:
            return float(score)
