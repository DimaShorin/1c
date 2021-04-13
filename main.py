from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

img = Image.open('img.png').convert('RGB')
pic = np.array(img)
shape = pic.shape
img.close()

plt.imshow(pic)

exit_fl = False
vertexes = []

# находим первую вершину со стороны одного из краев картинки, тк очевидно, что
# у нас впервые встретится именно вершина (либо сторона параллельная этой грани
# картинки) и тогда мы остановимся 

for i in range(shape[0]):
    for j in range(shape[1]):
        if pic[i, j][0] == 0:
            plt.plot(j, i, 'ro')
            vertexes.append((j, i))
            print(f'vertex in ({i},{j})')
            exit_fl = True
            break
    
    if exit_fl == True:
        break  

plt.show()
