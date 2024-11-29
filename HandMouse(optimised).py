import cv2 as cv
import mediapipe as mp
import pyautogui as pag

# Capturing the video with reduced resolution and frame rate
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)  # Reduced width
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)  # Reduced height
cap.set(cv.CAP_PROP_FPS, 15)  # Reduced frame rate

# Detecting one hand from the mediapipe library
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)

# Drawing utils
drawing_utils = mp.solutions.drawing_utils

# Get screen size
screen_w, screen_h = pag.size()

# Create an OpenCV window with the same size as the screen
cv.namedWindow("Virtual Mouse", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("Virtual Mouse", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

middle_y = 0
index_y = 0

# Click debounce variables
click_threshold = 35  # Adjust this value for your system
last_click_time = 0

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
                # Cursor through middle finger 
                if id == 12:
                    cv.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    middle_x = screen_w / frame_w * x
                    middle_y = screen_h / frame_h * y
                    pag.moveTo(middle_x, middle_y)

                # Click through index finger
                if id == 8:
                    cv.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    index_x = screen_w / frame_w * x
                    index_y = screen_h / frame_h * y
                    if abs(middle_y - index_y) < click_threshold:
                        cv.circle(img=frame, center=(x, y), radius=10, color=(0, 0, 255))
                        current_time = pag.time.time()
                        if current_time - last_click_time > 1:  # Debounce by 1 second
                            pag.click()
                            last_click_time = current_time

    cv.imshow("Virtual Mouse", frame)
    cv.waitKey(1)
