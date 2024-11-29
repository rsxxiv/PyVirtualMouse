# Importing Libraries
import cv2 as cv
import mediapipe as mp
import pyautogui as pag


# Capturing Video from first available device
cam = cv.VideoCapture(0)

# Using facemesh from mediapipe
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)

# Scaling the frame size to fit the screen
screen_w, screen_h = pag.size()

# Displaying the frames captured 
while True:
    _, frame = cam.read()
    frame = cv.flip(frame, 1)
    # converting the scammed frames to rgb for better processiong
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # creating an output from the rgb_frame frame by using the face_mesh
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Marking the right eye for movement
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            # print(x, y)
            cv.circle(frame, (x, y), 3, (0, 255, 0))

            if id == 1:
                # Matching the screen to the frame by getting the factor ratio
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_w * y
                # Alternate simpler option
                # screen_x = int(landmark.x * screen_w)
                # screen_y = int(landmark.y * screen_h)
                pag.moveTo(screen_x, screen_y)

        # Marking the left eye for clicking
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.008:
            pag.click()
            pag.sleep(1)
    cv.imshow('Eye controlled Mouse', frame)
    cv.waitKey(1)