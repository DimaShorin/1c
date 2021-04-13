from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

img = Image.open('img.png').convert('RGB')
pic = np.array(img)
shape = pic.shape
img.close()

exit_fl = False
vertexes = []

for i in range(shape[0]):
    for j in range(shape[1]):
        if pic[i, j][0] == 0:
            # plt.plot(j, i, 'ro')
            vertexes.append((j, i))
            print(f'vertex in ({i},{j})')
            exit_fl = True
            break
    
    if exit_fl == True:
        break        

# print(shape)
angs = np.linspace(0, 2 * np.pi, 100)
ss = []
length = int((shape[0] ** 2 + shape[1] ** 2) ** 0.5)

for ang in angs:
    currs = 0
    # c = 0
    print(ang)

    # plt.imshow(pic)
    # print(shape)

    for t in range(length):
        # print('------', vertexes[0][0], vertexes[0][1])
        x = int(vertexes[0][0] + t * np.cos(ang))
        y = int(vertexes[0][1] + t * np.sin(ang))

        if x >= shape[1] or x <= 0 or y >= shape[0] or y <= 0:
            break

        # print(x, y)

        # c += 1
        currs += (0 if pic[y, x][0] == 255 else 1)

        # plt.plot(x, y, 'r.')

    
    # plt.show()
    ss.append(currs)

plt.plot(angs, ss)
plt.show()
