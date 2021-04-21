# Importing the mains librarys
import cv2
import numpy as np
import os
import PIL.Image

pathName = ''
scale = 10
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
new_width = 0
#checking for the filter and video path
while True:
    pathName = input('what is the video path?')
    scale = int(input('what is the txt scale do you want?'))
    if os.path.exists(pathName):
        break
    else:
        print('Please, insert a valid path or a valid scale number' )

#resize the frame
def resizeImage(frame):
    width = int(frame.shape[1] * (scale/100))
    height = int(frame.shape[0] * (scale/100))
    dresize = (width, height)
    return cv2.resize(frame, dresize)

#conver each pixel to grayscale
def grayify(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

#Convert pixel into ascii
def pixels_to_ascii(path):
    image = PIL.Image.open(path)
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

#Extraction of the frames
def frameExtraction():
    vid = cv2.VideoCapture(pathName)
    lenght_vid = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    currentFrame = 0
    #checking for a path to put all the frames
    try:
        if not os.path.exists('data'):
            #creating a data dir if it does not exist
            os.makedirs('data')
            print('Data dir was created')
    except OSError:
        #print on the console if a error with OS lib occurs
        print('Error: os lib is not working')
    try:
        if not os.path.exists('data/frame'):
            #creating a data dir if it does not exist
            os.makedirs('data/frame')
            print('framedir was created')
    except OSError:
        #print on the console if a error with OS lib occurs
        print('Error: os lib is not working')
    try:
        if not os.path.exists('data/txt'):
            #creating a data dir if it does not exist
            os.makedirs('data/txt')
            print('txt dir was created')
    except OSError:
        #print on the console if a error with OS lib occurs
        print('Error: os lib is not working')

    while lenght_vid > currentFrame:
        # Capture frame-by-frame
        ret, frame = vid.read()

        # Saves image of the current frame in jpg file
        name = './data/frame/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        finalFrame = grayify(resizeImage(frame))
        cv2.imwrite(name, finalFrame)
        new_width = finalFrame.shape[1]
        new_image_data = pixels_to_ascii(name)

        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
        
        save_path = './data/txt/' + str(currentFrame) + ".txt"
        with open(save_path, "w") as f:
            f.write(ascii_image)
        currentFrame += 1
    # When everything done, release the capture
    vid.release()
    cv2.destroyAllWindows()
frameExtraction()