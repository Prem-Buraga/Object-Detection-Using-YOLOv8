# Object Detection Using YOLOv8

## Overview
The Object Detection Using YOLOv8 project enables users to upload images and detect objects using the YOLOv8 model. The system identifies various objects in the image, providing their names and counts, and outputs an annotated image highlighting the detected objects. This project leverages state-of-the-art deep learning techniques to ensure accurate and efficient object detection.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Output](#output)
- [License](#license)

## Features
- **Object Detection**: Detects and classifies multiple objects in an image using the YOLOv8 model.
- **User Interface**: Simple web interface for image upload and displaying results.
- **Output Image**: Provides an annotated image with detected objects highlighted.
- **Object Count**: Displays the names and counts of detected objects.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/object-detection-yolov8.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd object-detection-yolov8
    ```

3. **Set up your Python environment**:
    - Ensure you have Python 3.x installed.
    - Install the required libraries:
      ```bash
      pip install flask opencv-python torch torchvision numpy
      ```

4. **Download the YOLOv8 model weights**:
    - Place the pre-trained YOLOv8 model weights (`yolov8.pth`) in the project directory. You can download it from [YOLOv8 Model Weights](https://github.com/ultralytics/yolov8).

## Usage
1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the application**:
    - Open a web browser and go to `http://127.0.0.1:5000`.

3. **Upload an Image**:
    - Click on the "Upload Image" button and select an image for object detection.

4. **View Results**:
    - The detected objects' names and counts will be displayed.
    - Download the annotated output image with detected objects highlighted.
    - ![Screenshot 2024-09-22 222120](https://github.com/user-attachments/assets/42c53a07-b95c-42fa-994c-6e185e99517f)


## Dataset
This project uses any image uploaded by the user for object detection. No specific dataset is required.

## Project Structure
- `app.py`: The main Flask application script handling routes and functionalities.
- `yolov8.pth`: Pre-trained YOLOv8 model weights for object detection.
- `templates/`: Contains `index.html` for the frontend display.
- `static/uploads/`: Directory for storing uploaded images.
- `static/output/`: Directory for storing output images.

## Output
- **Detected Objects**: Displays the names and counts of detected objects.
- **Annotated Image**: An image with detected objects highlighted and labeled.


