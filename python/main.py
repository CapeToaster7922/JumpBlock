import pygame

# Dimensions de la carte
largeur = 600
hauteur = 400

# Position initiale du personnage
x_personnage = 300
y_personnage = 200

# Vitesse de déplacement du personnage
vitesse_x = 1.75
vitesse_y = 0

# Gravité
gravite = 0.5
niveau_gravite = 1

# Hauteur du saut
hauteur_saut = 12
peut_sauter = True

# Temps d'atterrissage
temps_atterrissage = 0

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jump")

# Boucle principale du programme
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement horizontal du personnage
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        x_personnage -= vitesse_x
    if touches[pygame.K_RIGHT]:
        x_personnage += vitesse_x

    # Gestion du saut
    if touches[pygame.K_SPACE] and peut_sauter:
        vitesse_y = -hauteur_saut
        peut_sauter = False

    # Mise à jour de la position verticale du personnage avec la gravité
    y_personnage += vitesse_y
    vitesse_y += gravite * niveau_gravite

    # Limite la position verticale du personnage pour éviter qu'il ne tombe en dehors de l'écran
    if y_personnage > hauteur - 50:
        y_personnage = hauteur - 50
        vitesse_y = 0
        peut_sauter = True
        temps_atterrissage = 0
    else:
        temps_atterrissage += 1

    # Effacement de la fenêtre
    fenetre.fill((255, 255, 255))  # Couleur de fond blanche

    # Dessiner le personnage
    pygame.draw.rect(fenetre, (255, 0, 0), (x_personnage, y_personnage, 50, 50))  # Rectangle rouge pour le personnage

    # Afficher le temps d'atterrissage
    font = pygame.font.Font(None, 30)
    texte = font.render("Temps d'atterrissage : " + str(temps_atterrissage), True, (0, 0, 0))
    fenetre.blit(texte, (10, 10))

    # Actualisation de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
