Air Doodle – Real-Time Air Drawing Using OpenCV

Overview

Air Doodle is a computer vision-based application that enables users to draw on a virtual canvas using hand gestures in real time. Developed with Python and OpenCV, the application tracks hand movements through a webcam and translates finger movements into drawing actions without requiring a physical input device.

Features

- Real-time hand tracking using a webcam.
- Gesture-based drawing on a virtual canvas.
- Touchless interaction using finger movements.
- Live visualization of hand movements.
- Interactive drawing experience using computer vision.

Technologies Used

- Python
- OpenCV
- Computer Vision
- NumPy

How It Works

1. Captures live video through the webcam.
2. Processes video frames to track hand movements.
3. Identifies finger positions and converts them into drawing coordinates.
4. Updates the virtual canvas based on detected hand movements.

Applications

- Touchless human-computer interaction.
- Gesture-based interfaces.
- Computer vision learning and experimentation.
- Interactive digital drawing systems.

Project Objective

To demonstrate the practical application of computer vision and real-time hand tracking by developing an interactive, touch-free drawing system.

Results and Output:
The Airdoodle system was executed and tested to evaluate its performance in real-time gesture-based drawing. The results show that the system successfully tracks hand movements, recognizes gestures, and converts them into smooth drawing strokes on the digital canvas.
The webcam input was processed continuously at a stable frame rate, and MediaPipe accurately detected the 21 hand landmarks in various lighting conditions. The system responded immediately when the index finger was raised, allowing the user to draw freely in the air. When the hand was closed, the drawing stopped as expected. Additional gestures such as clearing the canvas were also recognized reliably.
The drawing canvas produced smooth lines with minimal jitter due to the coordinate smoothing applied in the gesture pipeline. Users were able to draw shapes, letters, and free-hand sketches with reasonable accuracy. The control panel also functioned correctly, supporting color changes, brush size adjustments, undo actions, and saving the final drawing as a PNG file.



<img width="1019" height="542" alt="image" src="https://github.com/user-attachments/assets/b3714878-5eac-4790-955c-56326e4f6f0c" />

<img width="1019" height="542" alt="image" src="https://github.com/user-attachments/assets/8e349cbb-c5df-48b8-97f4-13e6f209bb4f" />

<img width="1019" height="542" alt="image" src="https://github.com/user-attachments/assets/4c35ba60-73d8-41e8-bbca-50c2bb7a09c0" />

<img width="1019" height="542" alt="image" src="https://github.com/user-attachments/assets/26aac3bd-66cb-487e-9e35-9c1763bdc540" />

<img width="1019" height="542" alt="image" src="https://github.com/user-attachments/assets/f3b54f67-59d2-468b-a077-2bef05e6e19e" />






Author

Priyadarshini K C
