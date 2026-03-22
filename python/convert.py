import sys
from PIL import Image, ImageEnhance
from waveshare_epd import epd2in13b_V4

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 convert.py <image_path>")
        return

    image_path = sys.argv[1]

    epd = epd2in13b_V4.EPD()
    epd.init()
    epd.Clear()

    width = epd.width
    height = epd.height

    # Load image
    image = Image.open(image_path)

    # ✅ KEEP YOUR WORKING ORIENTATION
    image = image.rotate(270, expand=True)
    image = image.resize((width, height))

    image = image.convert("RGB")

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.5)

    # Create buffers
    black_image = Image.new('1', (width, height), 255)
    red_image = Image.new('1', (width, height), 255)

    black_pixels = black_image.load()
    red_pixels = red_image.load()
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # 🔴 STRICT RED DETECTION (prevents full red issue)
            if r > 180 and g < 80 and b < 80:
                red_pixels[x, y] = 0

            else:
                # ⚫ BLACK DETECTION
                gray = int(0.3*r + 0.59*g + 0.11*b)

                if gray < 100:
                    black_pixels[x, y] = 0

    # Display
    epd.display(
        epd.getbuffer(black_image),
        epd.getbuffer(red_image)
    )

    epd.sleep()

    print("Black + Red display done ✅")


if __name__ == "__main__":
    main()
