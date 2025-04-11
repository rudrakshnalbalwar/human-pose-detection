import cv2
from pose_detector import PoseDetector
from video_processor import VideoProcessor

def main():
    # Initialize the pose detector
    pose_detector = PoseDetector()

    # Choose input source: 0 for webcam, or provide a video file path
    input_source = 0  # Change this to a video file path if needed

    # Initialize the video processor
    video_processor = VideoProcessor(pose_detector)

    # Process the video or webcam feed
    video_processor.process_video(input_source)

if __name__ == "__main__":
    main()