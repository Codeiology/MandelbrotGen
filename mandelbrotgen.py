import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time
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
logo = '''

                                        .o.
                                      o8888o
                                     d888888b
                                     `Y8888P'
                                 o .oood88booo. .o
                           Ybo  .88888888888888888.
                           "8888888888888888888888888b,
                          .o88888888888888888888888888"
                        Y88888888888888888888888888888b.
                       .o8888888888888888888888888888888.
                       8888888888888888888888888888888888
        o, ,db, ,o    d8888888888888888888888888888888888[
       .8888888888.   88888888888888888888888888888888888[
      o888888888888b ]88888888888888888888888888888888888
     d88888888888888o88888888888888888888888888888888888P
 .o8o88888888888888888888888888888888888888888888888888"               MANDELBROT SET RENDERER
<8888888888888888888888888888888888888888888888888888K
  "Y"88888888888888888888888888888888888888888888888888o
     Y88888888888888"88888888888888888888888888888888888b
      "888888888888" ]88888888888888888888888888888888888              by Codeiology
       '8888888888`   88888888888888888888888888888888888[
        "` "YP" `"    "8888888888888888888888888888888888[
                        888888888888888888888888888888888
                        "8888888888888888888888888888888'
                        d88888888888888888888888888888P'
                          `"88888888888888888888888888o
                           ,8888888888888888888888888P'
                           dP"  "88888888888888888
                                 " `"""Y88P"""' "'
                                     .d8888b.
                                     Y888888P    
                                      "8888"
'''
print(logo)
# Parameters
widthstr = input("Render width: ")
width = int(widthstr)
heightstr = input("Render height: ")
height = int(heightstr)
zoomstr = input("Render zoom: ")
zoom = float(zoomstr)
xoffsetstr = input("Y axis offset: ")
x_offset = float(xoffsetstr)
yoffsetstr = input("X axis offset: ")
y_offset = float(yoffsetstr)
maxiterstr = input("Max iterations: ")
max_iter = int(maxiterstr)
colormap = input("MatPlotLib colormap: ")

print("")
print("Rendering... ")
print("")

# Generate the Mandelbrot set
image = generate_mandelbrot(width, height, zoom, x_offset, y_offset, max_iter)
plt.figure(figsize=(10, 10))
plt.imshow(image.T, cmap=f'{colormap}', extent=[-2.5 / zoom - x_offset, 1.5 / zoom - x_offset, -1.5 / zoom - y_offset, 1.5 / zoom - y_offset])
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
time.sleep(1)
print("Render completed!")
print("")
while True:
    viewordown = input("Would you like to view this render temporarily or download the render? (view/down): ")
    print("")
    if viewordown == "view":
	    print("Viewing (close window to go back to program)...")
	    plt.show()
    elif viewordown == "down":
	    output_file = input("Name for new image? ")
	    dpistr = input("DPI (Dots Per Inch. Determines image quality. Recommended: 500 - 800): ")
	    dpi = int(dpistr)
	    plt.savefig(output_file, dpi=dpi)
	    print("")
	    print(f"Render saved as {output_file}")
	    sys.exit()
    else:
	    print("Invalid. Type either 'view', or 'down'")
