import cv2
from exercise_counter import ArmRepCounter

class VideoProcessor:
    def __init__(self, pose_detector):
        self.pose_detector = pose_detector
        self.squat_counter = ArmRepCounter()
    
    def process_video(self, source):
        cap = cv2.VideoCapture(source)
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Failed to read video")
                break
            
            # Detect pose
            results = self.pose_detector.detect_pose(image)
            
            # Count exercises if landmarks detected
            if results.pose_landmarks:
                count = self.squat_counter.count_squat(results.pose_landmarks)
                # Display count
                cv2.putText(image, f"ARm Curls: {count}", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Draw pose landmarks
            image = self.pose_detector.draw_pose(image, results)
            
            # Display the image
            cv2.imshow('Exercise Counter', image)
            if cv2.waitKey(5) & 0xFF == 27:  # ESC key to exit
                break
        
        cap.release()
        cv2.destroyAllWindows()