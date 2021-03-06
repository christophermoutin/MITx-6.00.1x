Introduction

In this problem set, you will help some people find their forever friends! You have been tasked with creating a representation of both pet adoption centers and the pet adopters. By creating python classes to model both elements, you will be able to assign a score to each adopter relative to a certain adoption center. A higher score means a specific adopter is more likely to adopt a pet from a specific adoption center.
OBJECTIVES

The goal of this problem will be to learn classes, methods, and class inheritance. There are a lot of references on Python classes available (look for classes in the readings listed in the Reference Links section of the webpage); here is the official Python tutorial on classes, sections 9.1-9.7 (excepting 9.5.1) will be useful for this Problem Set.

You will learn many facets of object-oriented programming, specifically:

    Implementing new classes and their attributes.
    Understanding class methods.
    Understanding inheritance.
    Telling the difference between a class and an instance of that class - recall that a class is a blueprint of an object, whilst an instance is a single, unique unit of a class.

Part 1 - The Adoption Center
The Adoption Center
10.0/10.0 points (graded)

The adoption center class will hold information specific to each adoption center, as well as methods for fetching information from or modifying the adoption center.

We want to store this information in an object that we can then pass around in the rest of our program. Your task, in this problem, is to write a class, AdoptionCenter, starting with a constructor that takes (name, location, species_count) as arguments and stores them appropriately. You will also write some methods, detailed later on in this section.

Adoption Center Initialization

The following information should be stored in an AdoptionCenter instance, and passed in as its initialization variables: __init__(self, name, species_types, location)

    name- A string that represents the name of the adoption center
    location- A tuple (x, y) That represents the x and y as floating point coordinates of the adoption center location.
    species_types- A string:integer dictionary that represents the number of specific pets that each adoption center holds. An example would be: {"Dog": 10, "Cat": 5, "Lizard": 3}, and another example would be {"Cat": 10, "Horse": 8}. Species names will always begin with a capital letter followed by lowercase letters, so you do not have to check for the case of the species name ('Cat' will never be stored as 'cat' or 'cAT' etc). Note that the specific animals tracked depend on the adoption center. If an adoption center does not have any of a specific species up for adoption, it will not be represented in the dictionary.

Adoption Center Methods

The following methods should be implemented for the AdoptionCenter class. The solution to this problem should be relatively short and very straightforward (please review what get methods should do if you find yourself writing multiple lines of code for each).

    get_name()- Returns the name of the adoption center
    get_location()- Returns the location of the adoption center
    get_species_count()- Returns a copy of the full list and count of the available species at the adoption center.
    get_number_of_species(species_name)- Returns the number of a given species that the adoption center has.
    adopt_pet(species_name)- Decrements the value of a specific species at the adoption center and does not return anything.

Part 2A - The Adopter
Meet the Adopter
10.0/10.0 points (graded)

There are a few types of potential adopters. The base class of the adopters is simply called "Adopter", which you will write below. The Adopter class will contain information that will be shared among all types of adopters.

Adopter Initialization

The following information should be stored in an Adopter instance, and passed in as its initialization variables:

__init__(self, name, desired_species):

    name- A string that represents the name of the adopter
    desired_species- A string that represents the desired species to adopt

Adopter Methods

The following methods should be implemented for the Adopter class

    get_name() - Returns the name of the adopter
    get_desired_species() - Returns the desired species of the adopter
    get_score(adoption_center) - Returns the score (details below)

About Scoring

Each Adopter class, and each Adopter subclass will have its own scoring methods. The minimum value that a score can be is 0, and there is no upper bound. The score method will take in an adoption_center as its argument, and will do some calculations to determine how good of a fit the specific adopter is to the specific adoption center.

For the base Adopter class, this score will be
where is the number of the adopter's desired species that the adoption center has. 

 The Flexible and Fearful Adopters
20.0/20.0 points (graded)

Now that you have written the base class for the adopter types, we want to represent different personalities and traits. The next two types of adopters will be the FlexibleAdopter and the FearfulAdopter, and both will be subclasses of the base Adopter class.

The Flexible Adopter

The FlexibleAdopter varies from the regular Adopter because a FlexibleAdopter is able to specify more than one species that they are interested in, but will still have one preferred species. The FlexibleAdopter is a subclass of the Adopter class, and should inherit from it and only it. The FlexibleAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, considered_species)

All of the inputs are the same as the Adopter class, except that considered_species is a list of strings of alternative species that the person is interested in adopting.

The FlexibleAdopter's scoring method also differs from the Adopter's scoring method. You should override the method so that a score calculated on a FlexibleAdopter will return a value that is the result of

where:

is the value that the Adopter class's score method returns

    is the number of animals the adoption center has of all the other considered species

Note that since considered_species is a list, you will have to iterate over the values to get the total number of considered pets that a specific adoption center has. The scoring method should take only one argument, the AdoptionCenter instance to calculate the score from.

Below, please write your implementation of the FlexibleAdopter class, including its __init__ method and its get_score(adoption_center) method.

The Fearful Adopter

The FearfulAdopter varies from the regular Adopter because a FearfulAdopter is afraid of one certain species of animal. While they may visit an AdoptionCenter that houses one or more of the feared species, their enthusiasm to visit the AdoptionCenter is reduced. The FearfulAdopter is a subclass of the Adopter class, and should inherit from it and only it. The FearfulAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, feared_species)

All of the inputs are the same as the Adopter class, except that feared_species is a string that is the name of the feared species.

The FearfulAdopter's scoring method also differs from the Adopter's scoring method. You should override the method so that a score calculated on a FearfulAdopter will return a value that is the result of

where:

is the value that the Adopter class's score method returns

    is the number of animals the adoption center has of the feared species

The scoring method should take only one argument, the AdoptionCenter instance to calculate the score from. 

Part 2C - AllergicAdopter and MedicatedAllergicAdopter
AllergicAdopter and MedicatedAllergicAdopter
20.0/20.0 points (graded)

The next two types of adopters will be the AllergicAdopter and the MedicatedAllergicAdopter.

The Allergic Adopter

The AllergicAdopter varies from the regular Adopter because an AllergicAdopter is extremely allergic to one or more particular species and cannot be around them even a little bit! If the adoption center contains one or more of those animals, they will not be able to go there. The AllergicAdopter is a subclass of the Adopter class, and should inherit from it and only it. The AllergicAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, allergic_species)

All of the inputs are the same as the Adopter class, except that allergic_species is a list of strings of one or more species that the adopter is allergic to.

The AllergicAdopter's scoring method also differs from the Adopter's scoring method. You should override the method so that a score calculated on an AllergicAdopter will return a value that is 0 if the adoption center has one or more of a species that the adopter is allergic to, otherwise it should calculate score based on the Adopter's calculate score method. Note that since allergic_species is a list, you will have to iterate over the values to check if the AdoptionCenter contains one or more of any. The scoring method should take only one argument, the AdoptionCenter instance to calculate the score from.

Below, please write your implementation of the AllergicAdopter class, including its __init__ method and its get_score(adoption_center) method.

The Medicated Allergic Adopter

The MedicatedAllergicAdopter varies from the AllergicAdopter as they have medicine to lessen their allergies. The MedicatedAllergicAdopter is a subclass of the AllergicAdopter class, and should inherit from the MedicatedAllergicAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, allergic_species, medicine_effectiveness)

All of the inputs are the same as the AllergicAdopter class, except that medicine_effectiveness is a dictionary of {string: float} of the medicines effectiveness to certain species. The effectiveness can range from 0.0 (no effectiveness against allergies) to 1.0 (full effectiveness against allergies).

For example, medicine_effectiveness may look like {"Dog": 0.5, "Cat": 0.0, "Horse": 1.0}, which means there is a medium effectiveness against dog allergies, no effectiveness against cat allergies, and full effectiveness against horse allergies.

The MedicatedAllergicAdopter's scoring method also differs from the AllergicAdopter's scoring method. Since the MedicatedAllergicAdopter is able to prevent against some allergies, they are now able to enter some AdoptionCenters they could not before. To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.

For example, consider the following:

Joe is allergic to dogs and horses, but wants a cat. He takes a medicine that has 0.5 effectiveness against dog allergies, and 1.0 effectiveness against horse allergies. He is considering going to an adoption center that has dogs, cats, and horses. Since the adoption center contains both of his allergies, to calculate his score, we will want to take the lowest effectiveness, that is, the 0.5 effectiveness against dogs, and multiply it by the normal Adopter score. The end score for his would be 0.5 * the base class Adopter score.

 The Sluggish Adopter
10.0/10.0 points (graded)

The final type of adopter will be the SluggishAdopter, and it will extend the baseAdopter class. A SluggishAdopter really dislikes travelling. The further away the adoption center is linearly, the less likely they will want to visit it. Since we are not sure the specific mood the SluggishAdopter will be in on a given day, we will assign their score with a random modifier depending on distance as a guess.

The SluggishAdopter varies from the regular Adopter because a SluggishAdopter really dislikes travelling. The further away the adoption center is linearly, the less likely they will want to visit it. Since we are not sure the specific mood the SluggishAdopter will be in on a given day, we will assign their score with a random modifier depending on distance as a guess. The SluggishAdopter is a subclass of the Adopter class, and should inherit from it and only it. The SluggishAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, location)

All of the inputs are the same as the Adopter class, except that location is a tuple of floats of the (x, y) coordinates, similar to the AdoptionCenter's location variable. The range for the coordinates are -5.0 to 5.0.

For this adopter, you will have to write an additional class method called get_linear_distance(to_location), which will calculate the linear distance between two points,

. You will want to calculate the distance by using the following formula:

This will be used calculate the linear distance between the SluggishAdopter, and the AdoptionCenter.

The SluggishAdopter's scoring method also differs from the Adopter's scoring method. You should override the method so that a score calculated on a SluggishAdopter will return a value that is:

, if the distance is less than 1
, if the distance is less than 3 but greater than or equal to 1
, if the distance is less than 5 but greater than or equal to 3

    , if the distance is greater than or equal to five.

Hints on how to generate random numbers!

The scoring method should take only one argument, the AdoptionCenter instance to calculate the score from.

Hint: remember AdoptionCenter's get_location method!

Part 3 - Connecting Adopters and Adoption Centers
20.0/20.0 points (graded)

Now that you have implemented both the AdoptionCenter and the different types of Adopters, it is time to try to adopt out some pets!

We will deal with two scenarios, one from the perspective of the Adopter type, and one from the perspective of an AdoptionCenter.

Help an Adopter visit AdoptionCenters in the Best Order

An Adopter or Adopter Subclass has a list of AdoptionCenters in the area, as well as information on what animals each AdoptionCenter has that day. Write a method that will return an organized list of the AdoptionCenters in such a way that the scores unique to the Adopter or Adopter Subclass for the AdoptionCenter will be ordered from highest score to lowest score.

Write the method get_ordered_adoption_center_list(adopter, list_of_adoption_centers) with the following parameters:

    adopter - A single Adopter or Adopter Subclass instance
    list_of_adoption_centers - A list of AdoptionCenter instances.

The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score. In case of ties, order the adoption center names alphabetically.

Help an AdoptionCenter Select Adopters

Using the methods that you have been given, you want to help organize a list of Adopter types for an AdoptionCenter to send advertisements which will invite them to visit the AdoptionCenter. The AdoptionCenters may have limited funds and can only send out mail to a select few Adopters in their database, so want to select the best candidates to advertise to in order to increase the odds of adoption.

Your task is to write a method get_adopters_for_advertisement(adoption_center, list_of_adopters, n). The method should return a list of length up to n that represents the highest scoring Adopters/Adopter Subclasses for the specific AdoptionCenter (You want to find the top n best Adopter matches). Write the method get_adopters_for_advertisement(adoption_center, list_of_adopters, n) with the following parameters:

    adoption_center - A single AdoptionCenter instance
    list_of_adopters - A list of Adopter (or a subclass of Adopter) instances.
    n - The number of adopters, up to a maximum of n, who will be sent advertisements. Note that n >= 0 and may be longer than the list_of_adopters, in which case less than n advertisements will be sent out.

The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score). In case of ties, order the Adopter names alphabetically.
