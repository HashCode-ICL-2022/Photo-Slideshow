
from structures import Slide, Image

if __name__ == "__main__":

    with open("data/a_example.txt", 'r') as images_pointer:
        image_strings = images_pointer.readlines()[1:]

    vertical_images = set()
    slides = set()

    for id, image_string in enumerate(image_strings):
        image = Image(image_string.strip(), id)

        if image.orientation == "V":
            vertical_images.add(image)
        else:
            slide = Slide([image])
            slides.add(slide)

    print(vertical_images)
    print(slides)