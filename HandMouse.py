import cv2 as cv
import mediapipe as mp
import pyautogui as pag

# Capturing the video
cap = cv.VideoCapture(0)

# Detecting hand from the mediapipe library
hand_detector = mp.solutions.hands.Hands()

# Drawing utils
drawing_utils = mp.solutions.drawing_utils

# Get screen size
screen_w, screen_h = pag.size()

# Create an OpenCV window with the same size as the screen
cv.namedWindow("Virtual Mouse", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("Virtual Mouse", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

index_y = 0
thumb_y = 0

while True:
    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape

    # Converting the captured frames to RGB for better processing
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                if id == 8:
                    cv.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_w / frame_w * x
                    index_y = screen_h / frame_h * y
                    pag.moveTo(index_x, index_y)

                # Click
                if id == 12:
                    cv.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    thumb_x = screen_w / frame_w * x
                    thumb_y = screen_h / frame_h * y
                    if abs(index_y - thumb_y) < 30:
                        pag.click()
                        pag.sleep(1)

    cv.imshow("Virtual Mouse", frame)
    cv.waitKey(1)
