from waveshare_epd import epd2in13b_V4
from PIL import Image

epd = epd2in13b_V4.EPD()
epd.init()
epd.Clear()

# Create pure black image
black = Image.new('1', (epd.height, epd.width), 255)
red = Image.new('1', (epd.height, epd.width), 255)

# Draw a black rectangle
for x in range(50, 150):
    for y in range(20, 80):
        black.putpixel((x, y), 0)

# Draw a red rectangle
for x in range(10, 60):
    for y in range(20, 80):
        red.putpixel((x, y), 0)

# Try normal order
epd.display(
    epd.getbuffer(black),
    epd.getbuffer(red)
)

epd.sleep()
