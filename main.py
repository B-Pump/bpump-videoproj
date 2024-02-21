from PIL import Image
import matplotlib.pyplot as plt
import internal.expectations as data
import internal.deformation as deform

image = Image.open("assets/fond-blanc.png")

largeur, hauteur = image.size
print ( largeur, hauteur, "test test")
milieu_x = largeur / 2
milieu_y = hauteur / 2
marker_size = 500

class Exercices:
    def __init__(self):
        pass

    def start(self, workout):
        title = data.fetchSugar(workout)
        positions = data.fetchPosition(workout)
        markers = {
            workout: positions
        }
        ajusted_markers = {
            workout: [(milieu_x + x, milieu_y + y) for x, y in positions]
            for workout, positions in markers.items()
        }
        plt.figure(figsize=(largeur/77, hauteur/77))  # Réglage de la taille de la figure en pouces
        print(largeur/77 ,hauteur/77)

        plt.imshow(image)

        for point in ajusted_markers[workout]:
            plt.scatter(point[0], point[1], color="red", marker="o", s=marker_size)

        plt.scatter(milieu_x, milieu_y, color="blue", marker="x", s=marker_size)
        plt.axis("off")

        plt.savefig(f"data/{workout}.png", bbox_inches="tight", pad_inches=0)
        print(deform.deformImage(workout))