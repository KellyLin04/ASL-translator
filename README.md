
## Inspiration
The inspiration for this project comes from our first hackathon. In our first hackathon, we created an image classification app. We wanted to see how we can expand on that. One of our teammates explained how they have a deaf cousin. That cousin feels as though remote learning has stripped his language away from him, similar to how if we couldn't use English. That's our language, and it's a part of who we are. He didn't feel a part of his community anymore when all he could do is type. Therefore, we decided to try to implement a program to help people like our teammate's cousin! We wanted him to have the ability to continue using American Sign Langauge (ASL) in his everyday life. 

## What it does
Our program essentially translates ASL, like subtitles in a movie. 

![demo1](images/ASL1.png width="250")

## How we built it
We built this program using a Google API for hand tracking called Mediapipe. Using this API, we used the fact that we can process the hand into smaller pieces of information. More specifically, we could get the coordinates of specific points in our hand that at as identifiers. We used those identifiers as vectors, and we implemented a linear regression model to train our model to identify ASL hand gestures. All of the programming was done through Python. Then, we used HTML and CSS to create a web page and used Flask to implement our Python script into our web app.

## Challenges we ran into
At first, we ran into a problem with training our data. Our linear regression model could only take a limited set of data, which meant we could not expand past a few letters. However, further inspection showed us that it was not the amount of data, but the type of data we were using. Furthermore, we had a lot of difficulties using Flask, as this was our first time using the program. We had to read through countless tutorials to understand them. 

## What's next for The Hand-y Translator
Next, we are looking at expanding our project to more ASL gestures. Additionally, we want this to not just be a remote learning tool but also a tool that can make communication with people who use ASL easier. It is definitely a wonderful idea that can help many people. 

