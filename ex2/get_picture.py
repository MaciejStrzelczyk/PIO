from skimage import io, feature
from skimage import img_as_ubyte
import os
import numpy as np
from PIL import Image


def get_pictures_and_convert(area, size_x, size_y):
    pictures = os.listdir(area)
    vectors = []
    for i in range(0, len(pictures)):
        img = io.imread(area + "/" + pictures[i], as_gray=True)
        cropped_img = img[:size_x, :size_y]
        cropped_img = img_as_ubyte(cropped_img)

        # cropped_img = cropped_img / 4
        # cropped_img = cropped_img.astype(int) * 4
        # io.imsave(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg", cropped_img)

        pImage = Image.fromarray(cropped_img)
        pImageConverted = pImage.convert("P", palette=Image.ADAPTIVE, colors=64).convert("RGB")
        pImageConverted.save(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg")

        img = io.imread(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg", as_gray=True)
        img = img_as_ubyte(img)
        g = feature.greycomatrix(img, [1], [45], levels=256, symmetric=True, normed=True)

        contrast = feature.greycoprops(g, 'contrast')[0][0]
        energy = feature.greycoprops(g, 'energy')[0][0]
        homogeneity = feature.greycoprops(g, 'homogeneity')[0][0]
        correlation = feature.greycoprops(g, 'correlation')[0][0]
        dissimilarity = feature.greycoprops(g, 'dissimilarity')[0][0]
        ASM = feature.greycoprops(g, 'ASM')[0][0]
        vector = [area + str(i + 1), contrast, energy, homogeneity, correlation, dissimilarity, ASM]
        vectors.append(vector)
    with open("vector.csv", 'a') as f:
        np.savetxt(f, np.array(vectors), fmt="%s", delimiter=",")


# io.imshow(img)
# io.show()
# return convert


if __name__ == '__main__':
    vectors = [["Texture", "Contrast", "Energy", "Homogeneity", "Correlation", "Dissimilarity", "ASM"]]
    with open("vector.csv", 'w') as f:
        np.savetxt(f, np.array(vectors), fmt="%s", delimiter=",")
    get_pictures_and_convert('desk', 128, 128)
    get_pictures_and_convert('floor', 128, 128)
    get_pictures_and_convert('wall', 128, 128)
    # print(os.listdir('desk'))
# print(pictures[1])
# io.imsave("wall/wall11.jpg", x)
