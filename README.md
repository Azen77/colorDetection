# Color Detection
```
1. Captures from your webcam
2. Converts each frame from BGR to HSV
3. Creates a mask to isolate the color yellow
4. Draws a green bounding box around any detected yellow region
```
# File Structure
```
├── src/
│   ├── main.py # Captures webcam and runs detection
│   └── util.py # Helper function to calculate HSV color limits
├── .gitignore
├── README.md
└── requirements.txt
```
# Requirements
```
Python3
OpenCV
NumPy
Pillow
```
To install, type into the terminal:
```
pip install -r requirements.txt
```
# How to Run
Run main.py in the terminal:
```
python src\main.py
```
After running, a window will open showing your webcam.
A green bounding box will appear around any detected yellow regions.
Press 'q' while focused on the webcam window to end the program

# Changing the Color
If you wish to change the detected color, edit the BGR value of the variable yellow
```
from util import getlimits

yellow = [0,255,255] # Change these values [blue,green,red]
cap = cv2.VideoCapture(0)
```
