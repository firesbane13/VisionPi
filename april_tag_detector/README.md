# April Tag Detector

## Overview
The April Tag Detector project is designed to detect AprilTags and various objects (balls, cones, cubes, rings) using OpenCV. It calculates the vertical and horizontal angles, as well as the distance from the camera to the detected objects. Additionally, it identifies the basic colors of the detected objects.

## Project Structure
```
april_tag_detector
├── src
│   ├── main.py                # Entry point of the application
│   ├── detection
│   │   ├── apriltag_detector.py  # Detects AprilTags and calculates their pose
│   │   ├── object_detector.py     # Detects various objects and retrieves their information
│   │   └── color_identifier.py     # Identifies the colors of detected objects
│   └── utils
│       └── camera_calibration.py   # Functions for camera calibration
├── requirements.txt           # Lists project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Specifies files to ignore in version control
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd april_tag_detector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure your camera is connected and accessible.

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Functionality
- **AprilTag Detection**: The application detects AprilTags in the camera feed and calculates their pose (angles and distance).
- **Object Detection**: It identifies various objects (balls, cones, cubes, rings) and retrieves their angles, distances, and colors.
- **Color Identification**: The application analyzes detected objects to determine their basic colors.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.