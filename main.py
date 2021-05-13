import cv2
import mediapipe as mp
Blue = (0, 0, 255)
mphands = mp.solutions.hands
mpHand = mphands.Hands()
mpDraw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
while True:
    success, img = camera.read()
    image = cv2.resize(img, (1000, 1000))
    output = mpHand.process(image)
    if output.multi_hand_landmarks:
        for landmarks in output.multi_hand_landmarks:
            for id, land in enumerate(landmarks.landmark):
                height, width, z = image.shape
                x, y = int(width * land.x), int(height * land.y)
                if id == 0:
                    if x < 400 and y < 600 and y > 400:
                        print("left")
                    if x > 600 and y < 600 and y > 400:
                        print("Right")
                    if y < 400 and x < 600 and x > 400:
                        print("Up")
                    if y > 600 and x < 600 and x > 400:
                        print("Down")
            mpDraw.draw_landmarks(image, landmarks, mphands.HAND_CONNECTIONS)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
