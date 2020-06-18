import board
import neopixel
import time
from PIL import Image, ImageDraw

pixel_pin = board.D18
num_pixels = 256

ORDER = neopixel.GRB


pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

def draw_image(offset):
    img = Image.new('RGB', (32, 8), color = (0,0,0))
    d = ImageDraw.Draw(img)
    d.text((1-offset,-2), "12300", fill=(255,255,255))
    return img


def main():
    print("Starting YouTube Subscriber Clock")
    offset = 0
    while True:

        rows = 8
        cols = 32

        img = draw_image(offset)

        array = list(img.getdata())

        index = 0
        for i in range(rows):
            for j in range(cols):
                index = i*cols + j
                if i % 2 == 0:
                    pixels[i*cols + j] = array[index]
                else:
                    pixels[i*cols + 31-j] = array[index]

        pixels.show()
        offset += 1
        if offset >= 32:
            offset = -32

if __name__ == '__main__':
    main()