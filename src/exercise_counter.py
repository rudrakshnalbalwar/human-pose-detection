import numpy as np

class SquatCounter:
    def __init__(self):
        self.counter = 0
        self.position = "up"  # start in standing position
        self.hip_threshold = 0.2  # adjust based on testing
        
    def count_squat(self, landmarks):
        if not landmarks:
            return self.counter
            
        # Get hip and knee y-positions (normalized)
        hip = landmarks.landmark[24].y  # right hip
        knee = landmarks.landmark[26].y  # right knee
        
        hip_knee_dist = hip - knee
        
        # State machine for counting
        if self.position == "up" and hip_knee_dist < self.hip_threshold:
            self.position = "down"
        elif self.position == "down" and hip_knee_dist > self.hip_threshold:
            self.position = "up"
            self.counter += 1
            
        return self.counter