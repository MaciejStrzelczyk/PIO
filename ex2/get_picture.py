from skimage import io
from skimage import img_as_ubyte
import os


def get_pictures_and_convert(area, size_x, size_y):
    pictures = os.listdir(area)
    for i in range(0, len(pictures)):
        img = io.imread(area +"/" + pictures[i], as_gray=True)
        cropped_img = img[:size_x, :size_y]
        cropped_img = img_as_ubyte(cropped_img)
        io.imsave(area+"_changed/"+area+"_gray"+str(i+1)+".jpg", cropped_img)

    io.imshow(img)
    io.show()
    #return convert

if __name__ == '__main__':

    get_pictures_and_convert('desk', 128, 128)
    #print(os.listdir('desk'))
   #print(pictures[1])
    #io.imsave("wall/wall11.jpg", x)