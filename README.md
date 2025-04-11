# Human Pose Detection

This project implements a real-time human pose detection system using Python. It is designed to work with both video files and real-time camera feeds, providing a robust solution for detecting human poses in various environments.

## Project Structure

```
human-pose-detection
├── src
│   ├── main.py               # Entry point of the application
│   ├── pose_detector.py       # Contains PoseDetector class for pose detection
│   ├── video_processor.py      # Handles video input and output
│   └── utils
│       ├── __init__.py        # Initializes the utils module
│       └── visualization.py    # Functions for visualizing detected poses
├── models
│   └── README.md              # Documentation for models used in pose detection
├── data
│   └── sample_videos
│       └── README.md          # Documentation for sample videos
├── requirements.txt           # Lists project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Specifies files to ignore in version control
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/human-pose-detection.git
   cd human-pose-detection
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

You can provide a video file path or use the real-time camera feed as input.

## Functionality

- **Pose Detection**: The system detects human poses in images and video frames using the `PoseDetector` class.
- **Video Processing**: The `VideoProcessor` class handles the reading and processing of video frames.
- **Visualization**: Detected poses are visualized on the input frames using functions from the `visualization` module.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.