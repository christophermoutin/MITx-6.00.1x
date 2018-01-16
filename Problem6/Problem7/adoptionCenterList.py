def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here
    liste = []
    result = []
    for i in list_of_adoption_centers:
        score = adopter.get_score(i)
        liste.append([score,i])
    #liste.sort(reverse = True)
    test=sorted(liste,key = lambda x:(-x[0],x[1].get_name()))
    #print liste
    for i in test:
        result.append(i[1])
    return result
            
    

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 
    liste = []
    result = []
    for i in list_of_adopters:
        score = i.get_score(adoption_center)
        liste.append([score,i])
    #print 'not sorted', liste, '\n'
    #liste.sort(reverse = True)
    #print 'sorted once', liste,'\n'
    test = sorted(liste,key = lambda x:(-x[0],x[1].get_name())) #ne fait rien
    #print 'end sorted',test,'\n'
    for i in test:
        n -= 1
        while n >= 0:
            result.append(i[1])
            break
    return result
