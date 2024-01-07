#!/usr/bin/python3

tableau_de_Morpion = [['-','-','-'],['-','-','-'],['-','-','-']]

def fin_de_partie():
    fin = False
    if tableau_de_Morpion[0][0] != '-' and tableau_de_Morpion[0][0] == tableau_de_Morpion[0][1] and tableau_de_Morpion[0][0] == tableau_de_Morpion[0][2] :
        fin = True
    elif tableau_de_Morpion[0][0] != '-' and tableau_de_Morpion[0][0] == tableau_de_Morpion[1][1] and tableau_de_Morpion[0][0] == tableau_de_Morpion[2][2] :
        fin = True
    elif tableau_de_Morpion[1][0] != '-' and tableau_de_Morpion[1][0] == tableau_de_Morpion[1][1] and tableau_de_Morpion[1][0] == tableau_de_Morpion[1][2] :
        fin = True
    elif tableau_de_Morpion[2][0] != '-' and tableau_de_Morpion[2][0] == tableau_de_Morpion[2][1] and tableau_de_Morpion[2][0] == tableau_de_Morpion[2][2] :
        fin = True
    elif tableau_de_Morpion[2][0] != '-' and tableau_de_Morpion[2][0] == tableau_de_Morpion[1][1] and tableau_de_Morpion[2][0] == tableau_de_Morpion[0][2] :
        fin = True
    elif tableau_de_Morpion[0][0] != '-' and tableau_de_Morpion[0][0] == tableau_de_Morpion[1][0] and tableau_de_Morpion[0][0] == tableau_de_Morpion[2][0] :
        fin = True
    elif tableau_de_Morpion[0][1] != '-' and tableau_de_Morpion[0][1] == tableau_de_Morpion[1][1] and tableau_de_Morpion[0][1] == tableau_de_Morpion[2][1] :
        fin = True
    elif tableau_de_Morpion[0][2] != '-' and tableau_de_Morpion[0][2] == tableau_de_Morpion[1][2] and tableau_de_Morpion[0][2] == tableau_de_Morpion[2][2] :
        fin = True
    return fin

def tab_plein():
    plein = True
    for i in range (3) :
        for j in range (3) :
            if tableau_de_Morpion[i][j] == '-' :
                plein = False
    return plein

def tab(joueur):
    print(str(tableau_de_Morpion[2])+'\n'+str(tableau_de_Morpion[1])+'\n'+str(tableau_de_Morpion[0]))
    emplacement = int(input("Utilisez le clavier numérique pour choisir où placer votre coup : ")) -1
    while not (emplacement in [0,1,2,3,4,5,6,7,8] and tableau_de_Morpion[emplacement//3][emplacement%3] == '-') :
        print("La valeur rentrée doit être dans[1,2,3,4,5,6,7,8,9] et à un emplacement libre")
        emplacement = int(input('Choississez une valeur correct : ')) -1
    if joueur == 'croix':
        tableau_de_Morpion[(emplacement)//3][emplacement%3] = 'X'
        tour(True)
    else:
        tableau_de_Morpion[(emplacement)//3][emplacement%3] = 'O'
        tour(False)

def tour(tour_rond):
    fin = fin_de_partie()
    rempli = tab_plein()
    if not fin and not rempli:
        if tour_rond:
            print("C'est au tour du joueur de ronds")
            tab('rond')
        else:
            print("C'est au tour du joueur de croix")
            tab('croix')
    else :
        if fin :
            message_fin = "Le joueur des "
            if tour_rond :
                message_fin = message_fin + 'croix'
            else :
                message_fin = message_fin + 'ronds'
            message_fin = message_fin + " qui a gangé !"
        else :
            message_fin = "Vous vous êtes bien battu(e)s, mais c'est une égalité !"
        print(str(tableau_de_Morpion[2])+'\n'+str(tableau_de_Morpion[1])+'\n'+str(tableau_de_Morpion[0]))
        print(message_fin)

def Morpion_Jeu():
    tour(True)

Morpion_Jeu()