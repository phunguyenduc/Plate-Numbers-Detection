import cv2
import numpy as np 

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    brightness = 10 
    # Adjusts the contrast by scaling the pixel values by 2.3 
    contrast = 2.3 
    image2 = cv2.addWeighted(img_gray, contrast, np.zeros(img_gray.shape, img_gray.dtype), 0, brightness)
    cv2.imshow('modified_image.jpg', image2)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            img_roi_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Gray image', img_roi_gray)
            cv2.imshow("ROI", img_roi)


    cv2.imshow("Input_Gray_Img", img_gray)
    cv2.imshow("Input Image", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Input Image",img)
        cv2.waitKey(500)
        count += 1

