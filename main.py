import streamlit as st
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from yolo_img_detection import *
from yolo_video_detection import *
from web_cam_detection import *
from yolo_custom_detection import *


def main():

    model_selection = st.sidebar.selectbox(
        'Choose one of the data trained type',('Welcome', 'Yolo Pretrained Model', 'Yolo Custom Trained Model')
    )

    if model_selection == "Yolo Pretrained Model":

        selected_box = st.sidebar.selectbox(
            'Choose one of the following media format',
            ('About YOLO Dataset', 'Image Object Detection', 'Video', 'Web Cam')
        )

        if selected_box == 'About YOLO Dataset':
            about_yolo()

        if selected_box == 'Image Object Detection':
            object_detection()

        if selected_box == 'Video':
            video_detection()

        if selected_box == 'Web Cam':
            web_video_detection()

    elif model_selection == "Yolo Custom Trained Model":
        selected_box1 = st.sidebar.selectbox(
            'Choose one of the following option',
            ('About Custom Dataset', 'Activate Real time Detection')
        )

        if selected_box1 == 'About Custom Dataset':
            about_custom_dataset()

        if selected_box1 == 'Activate Real time Detection':
            custom_detection()

    elif model_selection == "Welcome":
        welcome()


def about_yolo():
    st.title('Introcution to pre trained models of YOLO')
    st.write('YOLO model has been trained on the MS COCO datasets for the thousands of iteration and hours of training.')
    st.write('Thus it provides us the different pretrained models for the multi class object detection.')
    st.subheader('YOLO is trained on the 80 classes')
    st.write('In this preoject, we have used yolo-tiny weights and configuration files provided by YOLO to detect objects.')


def about_custom_dataset():
    st.title('About Trained Custom Dataset')

def custom_detection():

    custom_object_detection()


def welcome():
    st.title('Object Detection Using Deep Learning Algorithm')

    st.header('YOLO: You Only Look Once')

    st.write('In this app, we have used YOLOv3, a real-time object detection algorithm that uses a fully'
             ' convolutional network, along with a Darknet backbone, which performs feature extraction')

    st.header('A simple app that shows object detection on image, video and live video. ')

    st.subheader(' You can choose the options from the left.')
    st.write('See the sample of object detection in an Image')
    # status = st.radio ("See the sample of images and videos", ('Image detection', 'Video Detection'))
    #if status == 'Image detection':
    sampleImage = Image.open("images//sample_image.jpg")
    st.image(sampleImage)





def video_detection():

    st.header('Detecting Objects in a Video')
    st.write('We will be processing the videos using the pre-trained weights on COCO dataset on 80 classes.')
    st.subheader("Object Detection is done using YOLO V3 Model")
    st.write('The approach is quite similar to detecting images with YOLO.'
             ' We get every frame of a video like an image and detect objects at that frame using yolo.'
             ' Then draw the boxes, labels and iterate through all the frame in a given video.'
             ' Adjust the confidence and nms threshold to see how the algorithms detections change. '
            )

    choice = st.radio("", ("See an illustration", "Upload Video of your choice"))
    # streamlit.radio() inserts a radio button widget

    # If user selects 2nd option:
    if choice == "Upload Video of your choice":
        st.subheader("Input Video")  # streamlit.subheader()
        video_file = st.file_uploader("Upload", type=['mp4'])
         #streamlit.fileUploader() shows a file uploader widget. By default, size limit for uploaded files is  200MB. You can
        #configure it using the server.maxUploadSize config option. Here, “Upload” will be the label of uploader widget and the
        #allowed file types have been mentioned in types[] array

        if video_file is not None:  # if a file has been uploaded

            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(video_file.read())
            #my_video = cv2.VideoCapture(tfile.name)

            # st.write('my_video', my_video)
            # perform object detection on selected image
            video_function(tfile.name)

        # If user selects 1st option
    elif choice == "See an illustration":
        # display the example image
        #my_video = cv2.VideoCapture("test.mp4")
        #my_video = open("test.mp4", "rb")

        # perform object detection on the example image
        video_function("images/test1.mp4")


def object_detection():

    st.header('Object Detection In an Image')

    st.write('Finding all the objects in an image and drawing the so-called bounding boxes around them, is the main motive. ')

    #st.subheader("Object Detection is done using YOLO Models")
    choice = st.radio("", ("See an illustration", "Choose an image of your choice"))
    # streamlit.radio() inserts a radio button widget

    # If user selects 2nd option:
    if choice == "Choose an image of your choice":
        image_file = st.file_uploader("Upload", type=['jpg', 'png', 'jpeg'])
        if image_file is not None:  # if a file has been uploaded
            my_img = Image.open(image_file)  # open the image
            # perform object detection on selected image
            image_function(my_img)
        # If user selects 1st option
    elif choice == "See an illustration":
        # display the example image
        my_img = Image.open("images//test.jpeg")
        # perform object detection on the example image
        image_function(my_img)


def web_video_detection():

    st.header('Object Detection from the Web Cam')
    st.write('Creates an instance of VideoCapture with argument as device index or the name of a video file. Pass 0 as the device index for the camera'
             '. Once the instance of VideoCapture is created, you can capture the video frame-by-frame and detect object.')

    web_cam();


if __name__ == "__main__":
    main()
