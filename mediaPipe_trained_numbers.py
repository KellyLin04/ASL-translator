#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#import trained W
W = np.genfromtxt("w_opt_trained_numbers.csv", delimiter=",")

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
collection = []
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

        #output classification
        collection.append(res2)
        
        if (len(collection) >= 30):
            classification = np.round(np.mean(collection))
            if (classification == 1):
                print("1")
            elif (classification == 2):
                print("2")
            elif (classification == 3):
                print("3")
            elif (classification == 4):
                print("4")
            elif (classification == 5):
                print("5")
            elif (classification == 6):
                print("6")
            collection = []
    
  cv2.imshow('MediaPipe Hands', image)
  if cv2.waitKey(5) & 0xFF == 27:
    break
hands.close()
cap.release()


# In[ ]:




