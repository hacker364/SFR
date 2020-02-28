import os
import time
import cv2

def preview_image(image, name="window", time=100, resize=True):
    if resize:
        cv2.imshow(name, cv2.resize(image, (400, 400)))
    else:
        cv2.imshow(name, image)
    cv2.waitKey(time)
    
def take_image(name):
    os.chdir("/home/pi/SFR/testData")
   # if os.path.exists(name):
    #    print("Person with same Name exists")
    #    exit
  # else:
   #     os.makedirs(name)
    
    video_capture = cv2.VideoCapture(0)
    success, image = video_capture.read()
    count = 5
        
    while success:
        success, image = video_capture.read() 
        cv2.imwrite(name+"frame%d.jpg" % count, image)     # save frame as PNG file
        count -= 1
        if count == 0:
            break
        preview_image(image)
        
if __name__ == "__main__":
    os.chdir('/home/pi/SFR')
    name = input("Enter the name of student: ")
    take_image(name)
