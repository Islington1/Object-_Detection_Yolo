import cv2
import os
import time
import uuid

labels = ['hello1']

          #'thanks', 'yes', 'No', 'iloveyou']
images_path = "E:/PythonProjects/Thesis_project/custom_img"


number_imgs = 15

for label in labels:
    #!mkdir {'E:\PythonProjects\Thesis_project\custom_img\\'+label}
    os.mkdir(images_path+label)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(images_path, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

    cap.release()
