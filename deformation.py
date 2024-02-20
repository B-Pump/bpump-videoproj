import cv2
import numpy as np
import keyboard

# Charger l'image
image = cv2.imread('resized_points.png')

# Définir les points originaux du trapèze
points_originaux = np.float32([[0, 0], [1600, 0], [0, 800], [1600, 800]])

# Définir une classe pour gérer le compteur moinplus
class Counter:
    def __init__(self):
        self.moinplus = 0

counter = Counter()

# Définir les points de destination initiaux du trapèze
points_dest = np.float32([[0, 0], [1600, 0], [0, 800], [1600, 800]])

# Fonction pour mettre à jour les points de destination en fonction de moinplus
def update_points_dest():
    global points_dest
    points_dest = np.float32([[0 + counter.moinplus, 0], [1600 - counter.moinplus, 0], [0, 800], [1600, 800]])

# Fonction de rappel pour gérer les événements clavier
def action_clavier(event):
    global counter
    if event.name == 'a':
        counter.moinplus -= 10
        update_points_dest()
    elif event.name == 'z':
        counter.moinplus += 10
        update_points_dest()

# Initialiser l'écouteur d'événements clavier
keyboard.on_press(action_clavier)

# Boucle principale pour afficher les images
while True:
    # Calculer la matrice de transformation
    matrice_transformation = cv2.getPerspectiveTransform(points_originaux, points_dest)

    # Appliquer la transformation
    image_trapeze = cv2.warpPerspective(image, matrice_transformation, (1600, 800))

    # Redimensionner l'image pour l'affichage
    scaled_image = cv2.resize(image_trapeze, (800, 400))  # Réduire la taille par exemple

    # Afficher l'image originale et l'image transformée
    #cv2.imshow('Image originale', image)
    cv2.imshow('Affichage des points', scaled_image)  # Afficher l'image redimensionnée

    # Attendre une touche pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources et fermer les fenêtres
cv2.destroyAllWindows()
