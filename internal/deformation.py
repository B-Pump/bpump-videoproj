import cv2
import numpy as np
import keyboard
import os

class Counter:
    def __init__(self):
        self.moinplus = 0

def deformImage(workout):
    filePath = f"./data/{workout}.png"
    folderPath = "./output"

    image = cv2.imread(filePath)
    
    if image is not None:
        height, width = image.shape[:2]

        points_originaux = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        counter = Counter()

        def update_points_dest():
            nonlocal counter
            return np.float32([[0 + counter.moinplus, 0], [width - counter.moinplus, 0], [0, height], [width, height]])

        def action_clavier(event):
            nonlocal counter
            if event.name == "a":
                counter.moinplus -= 10
            elif event.name == "z":
                counter.moinplus += 10

        keyboard.on_press(action_clavier)

        while True:
            points_dest = update_points_dest()
            matrice_transformation = cv2.getPerspectiveTransform(points_originaux, points_dest)
            image_deformee = cv2.warpPerspective(image, matrice_transformation, (width, height))
            scaled_image = cv2.resize(image_deformee, (800, 400))

            cv2.imshow("Affichage des points", scaled_image)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()

        if not os.path.exists(folderPath):
            os.makedirs(folderPath)

        cv2.imwrite(f"{folderPath}/{workout}.png", image_deformee)
        os.remove(filePath)

        return f"Image déformée avec succès dans : {folderPath}/{workout}.png"

    return "Erreur : Impossible de charger l'image initiale"