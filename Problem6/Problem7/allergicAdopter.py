class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self,name,desired_species,allergic_species):
        Adopter.__init__(self,name,desired_species)
        self.allergic_species=allergic_species
        
    def get_score(self,adoption_center):
        for i in self.allergic_species:
            if i in adoption_center.species_types.keys():
                return 0.0
        score = float (adoption_center.get_number_of_species(self.desired_species))
        return score
                        


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medecine_effectiveness):
        AllergicAdopter.__init__(self,name,desired_species,allergic_species)
        self.medecine_effectiveness=medecine_effectiveness
    
    def get_score(self,adoption_center):
        rate = 1.0
        for i in adoption_center.species_types.keys():
            if i in self.allergic_species:
                if i not in self.medecine_effectiveness.keys():
                    rate = 0
                    break
                if self.medecine_effectiveness[i]<rate:
                    rate = self.medecine_effectiveness[i]
        score = rate*adoption_center.get_number_of_species(self.desired_species)
        return float(score)
