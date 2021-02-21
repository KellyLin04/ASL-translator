from flask import Flask, request, url_for, redirect, render_template, Response
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
app = Flask(__name__)

cap = cv2.VideoCapture(0)
def recognition():
    #import trained W
    W = np.genfromtxt("w_opt_trained.csv", delimiter=",")
    W2 = np.genfromtxt("w_opt_trained_numbers.csv", delimiter=",")
    W_used = W
    trackW = 1

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
            res2 = np.round(np.matmul(np.transpose(W_used),output_test2))    
            
            text = ""
            classification = res2
            
            if (trackW == 1):
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
            else:
                if (classification == 1):
                    text = "1"
                elif (classification == 2):
                    text = "2"
                elif (classification == 3):
                    text = "3"
                elif (classification == 4):
                    text = "4"
                elif (classification == 5):
                    text = "5"
                elif (classification == 6):
                    text = "6"
                
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
            
            #update displayed text
            if (k%256 == 32):
                text2 += text
            #keys to add underscore, spacing, and switch trained model
            elif (k%256 == ord("e")):
                text2 += "_"
            elif (k%256 == ord("r")):
                text2 = ""
            elif (k%256 == ord("w")):
                if (trackW == 1):
                    W_used = W2
                    trackW = 2
                else:
                    W_used = W
                    trackW = 1
                
            image = cv2.putText(image,text2, org2, font,  
                1.5*fontScale, (0,0,0), thickness, cv2.LINE_AA) 
                
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
            
    hands.close()
    cap.release()

    cv2.destroyAllWindows()


@app.route("/")
def home():
  return render_template("button.html")

@app.route("/main", methods=['GET', 'POST'])
def main():
  return render_template("main.html")

@app.route('/trained')
def trained():
    return Response(recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')
  
if (__name__ == "__main__"):
  app.run()

