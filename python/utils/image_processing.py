from PIL import Image, ImageEnhance

WIDTH = 212
HEIGHT = 104

def process_image(path):
    image = Image.open(path)
    image = image.resize((WIDTH, HEIGHT))
    image = image.convert("RGB")

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    black_image = Image.new('1', (WIDTH, HEIGHT), 255)
    red_image = Image.new('1', (WIDTH, HEIGHT), 255)

    black_pixels = black_image.load()
    red_pixels = red_image.load()
    pixels = image.load()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            r, g, b = pixels[x, y]

            if r > 120 and g < 100 and b < 100:
                red_pixels[x, y] = 0
            else:
                gray = int(0.3*r + 0.59*g + 0.11*b)
                if gray < 128:
                    black_pixels[x, y] = 0

    return black_image, red_image
