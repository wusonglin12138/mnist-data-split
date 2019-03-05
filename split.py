# coding=utf-8
from PIL import Image
import numpy as np


def loadImage():
    im = Image.open("mnistdigits.png")
    # im.show()

    im = im.convert("L")
    print(im.size)
    """
    (0,0,28,28)[0,0],(28,0,56,28)[0,1],(56,0,84,28)[0,2]
    (0,28,28,56)[1,0],(28,28,56,56)[1,1],(56,28,84,56)[1,2]   
    (0,56,28,84)[2,0] 
    """
    for i in range(0, 100):
        for j in range(0, 100):
            cropped = im.crop((j*28, i*28, j*28+28, i*28+28))
            cropped.save("C:/Users/wsl/Desktop/imgs/"+str(((28*i)+j))+".png")
            print((28*i)+j)
    # data = np.matrix(im.getdata())
    # print(data.shape)
    # img = data.reshape(28, 280000)

    matrix = []
    # for i in range(0, 28):
    #     for j in range(0, 28):
    #         print(img[i][j])
    # for x in range(0, 10000):
    #     for i in range(0, 28):
    #         matrix_temp = []
    #         for j in img[i]:
    #             matrix_temp.extend(x*28+j)
    #         print(matrix_temp)
    #         matrix.append(matrix_temp)
loadImage()
