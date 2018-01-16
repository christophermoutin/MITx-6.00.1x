class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelling. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self,name,desired_species,location):
        Adopter.__init__(self,name,desired_species)
        self.location = tuple([float(i) for i in location])
        
    def get_linear_distance(self,adoption_center): 
        d = ((adoption_center.get_location()[0]-self.location[0])**2+(adoption_center.get_location()[1]-self.location[1])**2)**(0.5)
        return float(d)
        
    def get_score(self,adoption_center):
        distance = self.get_linear_distance(adoption_center)
        if distance < 1:
            will = 1
        elif distance >= 1 and distance <3:
            will = random.uniform(0.7,0.9)
        elif distance >=3 and distance <5:
            will = random.uniform(0.5,0.7)
        else:
            will = random.uniform(0.1,0.5)
        score = will*adoption_center.get_number_of_species(self.desired_species)
        return float(score)
