import sys
from PIL import Image, ImageEnhance
from waveshare_epd import epd2in13b_V4

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bw_test.py <image_path>")
        return

    image_path = sys.argv[1]

    epd = epd2in13b_V4.EPD()
    epd.init()
    epd.Clear()

    # ✅ Use correct display dimensions
    width = epd.height   # 212
    height = epd.width   # 104

    # Load image
    image = Image.open(image_path)

    # Resize + rotate correctly
    image = image.resize((width,height ))
    image = image.rotate(180)

    # Convert to grayscale
    image = image.convert("L")

    # Improve contrast (important for e-ink)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    # Convert to pure black & white
    bw_image = image.point(lambda x: 0 if x < 128 else 255, '1')

    # Create empty red buffer (all white)
    red_image = Image.new('1', (width, height), 255)

    # Display (BLACK + EMPTY RED)
    epd.display(
        epd.getbuffer(bw_image),
        epd.getbuffer(red_image)
    )

    epd.sleep()

    print("Black & White display done ✅")


if __name__ == "__main__":
    main()
