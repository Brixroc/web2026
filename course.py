def nombre_coureurs(lst):
	```
	retourne le nombre de coureurs dans lst

	```
	assert type(lst) == liste
	assert all([type(obj) == str for obj in lst] == True
	return len(lst)

###################################################################################
def premier(lst):
	```
	retourne le premier coureur de lst
	```
	assert type(lst) == liste
	assert all([type(obj) == str for obj in lst] == True
	reurne lst[0]


##################################################
def dernier(lst):
    ``` 
    retourne le premier coureur de lst
     ``` 
    assert type(lst) == liste
    assert all([type(obj) == str for obj in lst] == True
    reurne lst[len(lst)-1]
#####################################################################
def coureur_en_position(lst, position):
    ``` 
    retourne le premier coureur de lst        ``` 
    assert type(lst) == liste
	assert all([type(obj) == str for obj in lst] == True
	assert type(position) == int and position >= 0 and position <= len(lst) - 1
	return lst[position - 1]
