import cv2
from time import sleep
key = cv2. waitKey(1)
sleep(2)
count = 0
while True:
    webcam = cv2.VideoCapture(0)

    try:
        check, frame = webcam.read()
        print(check)
        cv2.imshow("Capturing Images. Press 'S' to click picture.", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            file = './colored/colored#' + str(count) + '.jpg'
            cv2.imwrite(filename=file, img=frame)
            webcam.release()
            print("Image Processing...")
            img_ = cv2.imread(file, cv2.IMREAD_ANYCOLOR)
            print("Converting colored image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            img_ = cv2.resize(gray,(84,56))
            print("Image Grayscaled And Resized")
            img_resized = cv2.imwrite(filename= ('./grayscale/grayscale#' + str(count) + '.jpg'), img=img_)
            print(str(count) + "# Image saved!")
            count+=1
            
            #break
        
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
    
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
