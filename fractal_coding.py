import numpy as np
import cv2

#Returns the transformation of a point according to the wi transformation
def wi(input,matrix,sum):
    return np.dot(input,matrix) + sum

def getR(im):
    #Get the Range partitions of the image where R is a list of 8x8 non overlapping partitions of an image
    #We assume the image is 256x256 for simplicity
    R = []
    for i in range(0,256,8):
        for j in range(0,256,8):
            R.append(im[i:i+8,j:j+8])
    
    return R

def getD(im):
    #Get the domain partitions of the image where D is a list of 16x16 (overlapping) partitions of an image
    #We assume the image is 256x256 for simplicity
    D = []
    for i in range(0,256):
        for j in range(0,256):
            D.append(im[i:i+16,j:j+16])

def distance(ri,di):
    #Get the distance between two partitions
    #Were ri is an 8x8 partition of the image and di is a 16x16 partition of the image
    return np.sqrt(np.sum((ri-di)**2))


def FractalCompress(impath):
    #Convert the image to numpy array, as grayscale
    im = cv2.imread(impath,0)
    print(im.shape())
    #Get the Range partitions of the image
    Ri = getR(im)
    #Get the Domain partitions of the image
    Di = getD(im)
    # Get wi transformation for each partition
    print(Ri)


if __name__ == "__main__":
    FractalCompress("cat.jpg")