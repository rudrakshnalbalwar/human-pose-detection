import cv2
import mediapipe as mp
import numpy as np

class PoseDetector:
    def __init__(self, static_image_mode=False, min_detection_confidence=0.5):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            static_image_mode=static_image_mode, 
            min_detection_confidence=min_detection_confidence
        )
    
    def detect_pose(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)
        return results
    
    def draw_pose(self, image, results):
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                image, 
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )
        return image