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

class ArmRepCounter:
    def __init__(self):
        self.counter = 0
        self.position = "down"  # start with arm down
        self.threshold = 0.15  # adjust based on testing
        
    def count_rep(self, landmarks):
        if not landmarks:
            return self.counter
            
        # Get wrist and shoulder positions (using right arm)
        shoulder = landmarks.landmark[12]  # right shoulder
        elbow = landmarks.landmark[14]    # right elbow
        wrist = landmarks.landmark[16]    # right wrist
        
        # Calculate vertical distance between wrist and shoulder
        wrist_shoulder_dist = shoulder.y - wrist.y
        
        # State machine for counting
        if self.position == "down" and wrist_shoulder_dist > self.threshold:
            self.position = "up"
        elif self.position == "up" and wrist_shoulder_dist < 0:
            # When wrist goes below shoulder level, count as complete rep
            self.position = "down"
            self.counter += 1
            
        return self.counter