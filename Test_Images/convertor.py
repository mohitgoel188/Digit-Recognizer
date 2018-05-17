import cv2
import glob2

for path in glob2.glob('*.jpg'):
    img=cv2.imread(path)
    img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if img_g.shape!=(28,28):
        img_g=cv2.resize(img_g,(28,28))
        cv2.imwrite(path,img_g)
    #img_arr=numpy.array(img_g)
    # print(type(img_g))
    # print(img_g.shape)
        
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()