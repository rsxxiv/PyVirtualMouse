# PyVirtualMouse - Virtual Mouse Controlled by Eye and Hand Movements
Python Projects to Enable Virtual Mouse Using Hand Tracking and Eye Tracking

This project includes three versions of a virtual mouse that can be controlled using either **eye movements** or **hand movements**. Each method uses computer vision techniques to track facial landmarks or hand gestures and translate them into mouse movements and clicks.

## 1. Eye Controlled Mouse
**Filename:** `EyeMouse.py`

This version of the virtual mouse uses **eye movement** to control the cursor. The system tracks the position of the user's right eye to move the mouse cursor on the screen. It also detects blinks from the left eye to simulate mouse clicks. This allows for hands-free control, making it especially useful for accessibility or for those looking to control their system without physical touch.

### Features:
- **Right Eye Tracking**: Moves the cursor based on the position of the right eye.
- **Left Eye Blink Detection**: Simulates mouse clicks with a blink of the left eye.
- **Real-time Operation**: Processes video frames in real-time for smooth cursor movement and click detection.

---

## 2. Hand Controlled Mouse
This category includes two versions of a hand-tracking-based virtual mouse, allowing users to control the cursor and perform clicks with hand gestures.

### 2a. Regular Hand Controlled Mouse
**Filename:** `HandMouse.py`

The regular version of the hand-controlled mouse tracks hand movements using the webcam and MediaPipe's hand-tracking model. The cursor moves in correspondence with the user's hand gestures, and basic hand gestures can trigger mouse clicks. This provides a natural, gesture-based way to control the mouse hands-free.

#### Features:
- **Hand Tracking**: Tracks the position and movement of the user's hand to move the mouse cursor.
- **Click Simulation**: Uses hand gestures, such as pinching or closing the fist, to simulate mouse clicks.
- **Real-time Control**: Offers smooth and responsive mouse control through hand gestures.

---

### 2b. Optimized Hand Controlled Mouse
**Filename:** `HandMouse(optimised).py`

This is the **optimized version** of the hand-controlled mouse, designed to improve performance and accuracy. The optimized version reduces lag and enhances the detection of hand gestures for smoother and more precise control. It provides a more efficient experience, especially in environments where the system needs to respond faster or with more accuracy.

#### Features:
- **Improved Hand Tracking**: Enhanced algorithm for faster and more accurate hand gesture detection.
- **Reduced Lag**: Optimized processing to minimize delays between hand movement and cursor action.
- **Smoother Interaction**: Offers better responsiveness, ideal for more complex hand gestures and longer use.

---

## Technology Stack
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For detecting and tracking facial landmarks (EyeMouse) and hand gestures (Handmouse).
- **PyAutoGUI**: For controlling the system's mouse cursor.

## How It Works:
- **Eye Controlled Mouse**: Uses facial landmarks to track the right eye for mouse movement and detects the left eye's blink to simulate clicks.
- **Hand Controlled Mouse**: Tracks hand movements using MediaPipe's hand-tracking model, allowing users to control the cursor and trigger clicks with simple hand gestures.

## Getting Started:
1. Ensure you have a webcam connected.
2. Install required Python libraries (`opencv-python`, `mediapipe`, `pyautogui`).
3. Run the desired script to start controlling your mouse with either your eyes or hands!

---
