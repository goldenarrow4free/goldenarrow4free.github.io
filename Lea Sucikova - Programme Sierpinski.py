import turtle
turtle.tracer(0,0)            # accélération du tracé
turtle.screensize(2000,2000)  # taille fenêtre graphique
turtle.pu()
turtle.goto(-500,0)
turtle.pd()

def dessiner(courbe, longueur, angle):    
    """ réalise une représentation graphique d'une courbe donnée par des chaines de caractères """
    for caractere in courbe:
        if caractere == '+':
            turtle.left(angle)
        elif caractere == '-' or caractere == '−':
            turtle.right(angle)
        elif caractere in ['F', 'G']:          
            turtle.forward(longueur)


#dessiner('F', 50, 60)

def regleSierpinski(chaine):
    nouvelleChaine = ''    # on crée une nouvelle chaine de caractères VIDE
    for lettre in chaine:  # on épelle la chaine de caractères donnée en paramètres
        if lettre == 'F':  # si dans l'ancienne chaine, il y a un 'F'
            nouvelleChaine = nouvelleChaine + 'F − G + F + G − F'  # alors, on écrit F+F--F+F dans la nouvelle chaine 
        elif lettre == 'G':
            nouvelleChaine = nouvelleChaine + 'GG'
        else :
            nouvelleChaine = nouvelleChaine + lettre  # sinon, on reporte la lettre telle quelle
    return nouvelleChaine


def courbeSierpinski(motifInitial, niter):
    """ 
        appelle niter fois regleSierpinski pour créer la courbe de Sierpinski
    """
    courbe = motifInitial # on part du motif initial donné par l'utilisateur en paramètres
    for i in range(niter):
        nouveauMotif = regleSierpinski(courbe)  # on trouve le nouveau Motif à partir du motif de départ
        courbe = nouveauMotif # on dit que le nouveau Motif est maintenant le motif de départ
    return courbe



#courbe = courbeSierpinski('F',3)
#dessiner(courbe,50, 60)

# def flocon(motifInitial, niter):
#     courbe = courbeSierpinski(motifInitial, niter)
#     flocon = ''
#     for _ in range(3):
#         flocon += courbe
#         flocon += '--' 
#     return flocon

longueur = 10
angle = -120
niter = 4
dessiner(courbeSierpinski('F-G-G', niter), longueur, angle)


turtle.update()      # accélération du tracé
turtle.exitonclick() # permet la fermeture de la fenêtre graphique