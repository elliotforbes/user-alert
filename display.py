import board
import neopixel
import time

pixel_pin = board.D18
num_pixels = 256

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=False, pixel_order=ORDER
)

rows = 8
cols = 32

array = [ [(255,255,255)]*cols for i in range(rows)]



for i in range(len(array)):
    for j in range(len(array[0])):
        index = i*cols + j
        if i % 2 == 0:
            pixels[i*cols + j] = array[i][j]
        else:
            pixels[i*cols + 31-j] = array[i][j]

        pixels.show()
        time.sleep(0.2)


pixels.hide()