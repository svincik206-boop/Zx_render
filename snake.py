#Basic snake animation
import zx_render, time
x = 0
while True:
    zx_render.eraseText()
    zx_render.renderText("Snake", 15, 1)
    if x < 37:
        x += 1
        zx_render.renderText("X", x, 2)
        time.sleep(0.05)
    else:
        x = 0
        zx_render.renderText("X", x, 2)
        time.sleep(0.05)