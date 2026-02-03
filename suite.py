def longueur_vol(n):
    '''
    retourne lalongueur du vol pour la suite de Syracuse
    '''
    compteur = 0 
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else : 
            n = 3 * n + 1
        compteur += 1
    return compteur

    # test
    assert longueur_vol(3) == 7
    assert longueur_vol(7) == 
    assert longueur_vol(1) ==

##################################

def syracuse(n):
    '''
    retourne le liste des termes de la suite de syracuse
    '''
    reponse = []
    while n != 1:
        