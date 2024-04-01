## COMPUTER VISION USING OPENCV
---
# FACE , EYE AND SMILE DETECTION FROM PHOTOS
### Purpose
This Python script detects faces, eyes, and smiles in images using OpenCV.

### Usage
- Ensure Python 3.x and OpenCV are installed.
- Download Haar cascade XML files for face, eye, and smile detection.
- Update file paths in the code.
- Run the script and provide the image path.

### Functionality
- Detects faces using a face cascade classifier.
- Draws rectangles around detected faces.
- Detects eyes and smiles within each face ROI.
- Draws rectangles around detected eyes and smiles.
- Displays processed image with detections.
- Press any key to view each detection.
- Press any key to close displayed images.

### Example Output
<img src="https://github.com/Abeshith/Computer-Vision/blob/main/output%20images/Detect-FromPhotos.png" width="400">


### Notes
- Adjust parameters for better detection.
- Requires accurate placement of Haar cascade XML files.
- Basic demonstration, may need refinement for specific needs.

---
# FACE AND EYE DETECTION USING CAMERA

This Python script demonstrates real-time object detection using OpenCV, a powerful computer vision library. It utilizes a pre-trained Haar cascade classifier to detect objects within a live video stream from a webcam.

## How it Works

- **Loading Haar Cascade Classifier**: The script loads a pre-trained Haar cascade classifier for detecting objects of interest, such as faces. The classifier file is stored in the `haarcascade` directory.

- **Detection Function (`detect`)**: The `detect` function takes grayscale images (`gray`) and their corresponding color images (`frame`) as input. It utilizes the `detectMultiScale` method to detect objects within the grayscale image. Detected objects are highlighted with rectangles drawn on the color image (`frame`).

- **Video Capture and Main Loop**: The script initializes the webcam and enters a loop to continuously read frames from it. For each frame, it converts it to grayscale, performs object detection using the `detect` function, and displays the results in real-time.

- **Exiting the Program**: The program exits when the user presses the 'q' key. It releases the video capture object and closes all OpenCV windows.

## Usage

1. **Requirements**: Ensure that you have OpenCV installed (`pip install opencv-python`).

2. **Running the Script**: Execute the Python script. It will open a window showing the live webcam feed with detected objects highlighted.

3. **Exiting the Program**: Press the 'q' key to exit the program.

## Notes

- Adjust the detection parameters (`scaleFactor`, `minNeighbors`, etc.) for better performance based on the object being detected.
- Haar cascade classifiers can be trained for various objects beyond faces. Custom classifiers can be created for specific objects if needed.
- This script provides a basic example of real-time object detection. Further optimizations and enhancements can be made based on specific requirements.

## References

- [OpenCV Documentation](https://opencv.org/)
- [Cascade Classifier Training](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
- [Haar Feature-based Cascade Classifiers](https://docs.opencv.org/3.4/d7/d8b/tutorial_py_face_detection.html)

---

# Full Body Detection Using OpenCV

This Python script demonstrates real-time full body detection using OpenCV. It utilizes a pre-trained Haar cascade classifier to detect full bodies within a video file.

## Implementation

The script uses OpenCV to detect full bodies in a video file. It loads a pre-trained Haar cascade classifier for full body detection and then processes each frame of the video to identify and draw rectangles around the detected bodies. 

## Usage

1. **Requirements**: Ensure that you have OpenCV installed (`pip install opencv-python`).

2. **Running the Script**: Make sure you have the video file `walking.avi` in the same directory as the script. Execute the Python script.

3. **Exiting the Program**: Press the 'Enter' key to exit the program.

## Notes

- Adjust the parameters (`scaleFactor`, `minNeighbors`, etc.) of the `detectMultiScale` method for better performance based on the size and resolution of the video.

- This script provides a basic example of real-time full body detection. Further optimizations and enhancements can be made based on specific requirements.

<img src="https://github.com/Abeshith/Computer-Vision/blob/main/output%20images/WalkingHumans.png" width="400">


## References

- [OpenCV Documentation](https://opencv.org/)

---







