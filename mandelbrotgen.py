import numpy as np
import matplotlib.pyplot as plt
import os
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def generate_mandelbrot(width, height, zoom, x_offset, y_offset, max_iter):
    x = np.linspace(-2.5 / zoom - x_offset, 1.5 / zoom - x_offset, width)
    y = np.linspace(-1.5 / zoom - y_offset, 1.5 / zoom - y_offset, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    img = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            c = Z[j, i]
            img[j, i] = mandelbrot(c, max_iter)

    return img
os.system("clear")
print("MANDELBROT SET RENDERER")
print("")
# Parameters
widthstr = input("Render width: ")
width = int(widthstr)
heightstr = input("Render height: ")
height = int(heightstr)
zoomstr = input("Render zoom: ")
zoom = float(zoomstr)
xoffsetstr = input("X axis offset: ")
x_offset = float(xoffsetstr)
yoffsetstr = input("Y axis offset: ")
y_offset = float(yoffsetstr)
maxiterstr = input("Max iterations: ")
max_iter = int(maxiterstr)

print("")
print("Generating render... ")
print("")

# Generate the Mandelbrot set
image = generate_mandelbrot(width, height, zoom, x_offset, y_offset, max_iter)

# Plotting the Mandelbrot set
plt.figure(figsize=(10, 10))
plt.imshow(image.T, cmap='hot', extent=[-2.5 / zoom - x_offset, 1.5 / zoom - x_offset, -1.5 / zoom - y_offset, 1.5 / zoom - y_offset])
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
