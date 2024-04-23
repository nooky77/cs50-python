from PIL import Image
import sys

images = []

for item in sys.argv[1:]:
    image = Image.open(item)
    images.append(image)

images[0].save(
    "walking.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
