from PIL import Image
import matplotlib.pyplot as plt
import internal.expectations as data

image = Image.open("assets/blanc.jpg")

largeur, hauteur = image.size
milieu_x = largeur / 2
milieu_y = hauteur / 2
marker_size = 100
nom_fichier = "image_points.png"
class Exercices:
    def __init__(self):
        """
        Class initialization
        """
        pass

    def start(self, workout):
        """
        Show chart for specified fiscal year

        :param workout: The name of the exercise
        """
        title = data.fetchSugar(workout)
        positions = data.fetchPosition(workout)
        markers = {
            workout: positions
        }
        ajusted_markers = {
            workout: [(milieu_x + x, milieu_y + y) for x, y in positions]
            for workout, positions in markers.items()
        }

        plt.imshow(image)

        for point in ajusted_markers[workout]:
            plt.scatter(point[0], point[1], color="red", marker="o", s=marker_size)

        plt.scatter(milieu_x, milieu_y, color="blue", marker="x", s=marker_size)
        plt.axis('off')
    
        plt.savefig(nom_fichier, bbox_inches='tight', pad_inches=0)  # Enregistre l'image sans les marges
        image_points = Image.open("image_points.png")
        resized_image = image_points.resize((1600, 800))
        resized_image.save("./assets/resized_points.png")
