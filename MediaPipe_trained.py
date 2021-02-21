#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#import trained W
W = np.genfromtxt("w_opt_trained.csv", delimiter=",")

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
collection = []
text2 = ""
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    result3 = []
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            output3 = []
            mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for item in hand_landmarks.landmark:
                output3.append(item.x)
                output3.append(item.y)
                output3.append(item.z)
        
        output_test2 = np.transpose(output3)
        res2 = np.round(np.matmul(np.transpose(W),output_test2))    
        
        text = ""
        classification = res2
        if (classification == 1):
            text = "Hello"
        elif (classification == 2):
            text = "i"
        elif (classification == 3):
            text = "m"
        elif (classification == 4):
            text = "a"
        elif (classification == 5):
            text = "y"
            
        # font 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        # org 
        org = (50, 50) 
        org2 = (50, 150)
        # fontScale 
        fontScale = 1
        # Blue color in BGR 
        color = (255, 0, 0) 
        # Line thickness of 2 px 
        thickness = 2
        
        k = cv2.waitKey(5)
    
        image = cv2.putText(image,text, org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)  
        
        if (k%256 == 32):
            text2 += text
        elif (k%256 == ord("e")):
            text2 += "_"
        elif (k%256 == ord("r")):
            text2 = ""
            
        image = cv2.putText(image,text2, org2, font,  
               2*fontScale, (0,0,0), thickness, cv2.LINE_AA) 
             
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
        
hands.close()
cap.release()


# In[ ]:




