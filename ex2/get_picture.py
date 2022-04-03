from skimage import io, feature
from skimage import img_as_ubyte
import os
from PIL import Image


def get_pictures_and_convert(area, size_x, size_y):
    pictures = os.listdir(area)
    for i in range(0, len(pictures)):
        img = io.imread(area + "/" + pictures[i], as_gray=True)
        cropped_img = img[:size_x, :size_y]
        cropped_img /= 4
        cropped_img = img_as_ubyte(cropped_img)

        # cropped_img = cropped_img / 4
        # cropped_img = cropped_img.astype(int) * 4
        # io.imsave(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg", cropped_img)

        # pImage = Image.fromarray(cropped_img)
        # pImageConverted = pImage.convert("P", palette=Image.ADAPTIVE, colors=64).convert("RGB")
        # pImageConverted.save(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg")
        #
        # img = io.imread(area + "_changed/" + area + "_gray" + str(i + 1) + ".jpg", as_gray=True)
        # img = img_as_ubyte(img)
        g = feature.greycomatrix(cropped_img, [1], [0], levels=256, symmetric=False, normed=True)

        contrast = feature.greycoprops(g, 'contrast')[0][0]
        energy = feature.greycoprops(g, 'energy')[0][0]
        homogeneity = feature.greycoprops(g, 'homogeneity')[0][0]
        correlation = feature.greycoprops(g, 'correlation')[0][0]
        dissimilarity = feature.greycoprops(g, 'dissimilarity')[0][0]
        ASM = feature.greycoprops(g, 'ASM')[0][0]

# io.imshow(img)
# io.show()
# return convert


if __name__ == '__main__':
    get_pictures_and_convert('desk', 128, 128)
    # print(os.listdir('desk'))
# print(pictures[1])
# io.imsave("wall/wall11.jpg", x)
