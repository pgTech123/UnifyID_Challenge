import get_random
import Image


def main():
    # Create the image
    img = Image.new('RGB', (128, 128), "black")
    pix = img.load()

    # Get our random numbers
    values = get_random.get_random(128*128*3, 0, 255)

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            red = values[i*3 + j*img.size[0]]
            green = values[i*3 + j*img.size[0] + 1]
            blue = values[i*3 + j*img.size[0] + 2]
            pix[i, j] = (red, green, blue)

    img.show()
    img.save('random_image.bmp')


if __name__ == '__main__':
    main()
