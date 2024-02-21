from PIL import Image  # Importing the Image module from the PIL library
import matplotlib.pyplot as plt  # Importing the pyplot module from the matplotlib library
import internal.expectations as data  # Importing the 'expectations' module from the internal package
import internal.deformation as deform  # Importing the 'deformation' module from the internal package

# Opening the image file
image = Image.open("assets/fond-blanc.png")

# Getting the width and height of the image
width, height = image.size
print(width, height, "test test")  # Printing the width and height of the image (testing)

# Calculating the center coordinates of the image
center_x = width / 2
center_y = height / 2
marker_size = 500  # Setting the marker size

class Exercises:
    def __init__(self):
        pass

    def start(self, workout):
        # Fetching exercise title and positions
        title = data.fetchSugar(workout)
        positions = data.fetchPosition(workout)
        markers = {workout: positions}  # Creating a dictionary of workout positions

        # Adjusting markers to fit the image
        adjusted_markers = {
            workout: [(center_x + x, center_y + y) for x, y in positions]
            for workout, positions in markers.items()
        }

        # Setting the figure size
        plt.figure(figsize=(width/77, height/77))  # Adjusting figure size in inches
        print(width/77, height/77)  # Printing figure size (testing)

        # Displaying the image
        plt.imshow(image)

        # Plotting markers on the image
        for point in adjusted_markers[workout]:
            plt.scatter(point[0], point[1], color="red", marker="o", s=marker_size)

        # Plotting the center of the image
        plt.scatter(center_x, center_y, color="blue", marker="x", s=marker_size)
        plt.axis("off")  # Turning off the axis

        # Saving the plot
        plt.savefig(f"data/{workout}.png", bbox_inches="tight", pad_inches=0)
        print(deform.deformImage(workout))  # Deforming the image and printing the result
