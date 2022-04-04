import os
import numpy as np
from PIL import Image
from skimage import img_as_ubyte
from skimage import io, feature


def get_pictures_and_convert(area, size_x, size_y):
    pictures = os.listdir(area)
    vectors = []
    for i in range(0, len(pictures)):
        img = io.imread(area + "/" + pictures[i], as_gray=True)
        cropped_img = img[:size_x, :size_y]
        cropped_img = img_as_ubyte(cropped_img)

        p_image = Image.fromarray(cropped_img)
        p_image_converted = p_image.convert("P", palette=Image.ADAPTIVE, colors=64).convert("RGB")
        p_image_converted.save(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg")

        img = io.imread(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg", as_gray=True)
        img = img_as_ubyte(img)
        g = feature.greycomatrix(img, [1], [45], levels=256, symmetric=True, normed=True)

        contrast = round(feature.greycoprops(g, 'contrast')[0][0], 5)
        energy = round(feature.greycoprops(g, 'energy')[0][0], 5)
        homogeneity = round(feature.greycoprops(g, 'homogeneity')[0][0], 5)
        correlation = round(feature.greycoprops(g, 'correlation')[0][0], 5)
        dissimilarity = round(feature.greycoprops(g, 'dissimilarity')[0][0], 5)
        ASM = round(feature.greycoprops(g, 'ASM')[0][0], 5)
        vector = [area, contrast, energy, homogeneity, correlation, dissimilarity, ASM]
        vectors.append(vector)
    with open("vector.csv", 'a') as f:
        np.savetxt(f, np.array(vectors), fmt="%s", delimiter=",")


if __name__ == '__main__':
    vectors = [["Texture", "Contrast", "Energy", "Homogeneity", "Correlation", "Dissimilarity", "ASM"]]
    with open("vector.csv", 'w') as f:
        np.savetxt(f, np.array(vectors), fmt="%s", delimiter=",")
    get_pictures_and_convert('desk', 128, 128)
    get_pictures_and_convert('floor', 128, 128)
    get_pictures_and_convert('wall', 128, 128)
