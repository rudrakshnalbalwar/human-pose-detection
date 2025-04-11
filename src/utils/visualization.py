def draw_pose(image, keypoints, skeleton, color=(0, 255, 0), thickness=2):
    for i, keypoint in enumerate(keypoints):
        if keypoint[2] > 0:  # Check if the keypoint is detected
            cv2.circle(image, (int(keypoint[0]), int(keypoint[1])), 5, color, -1)

    for pair in skeleton:
        part_a = keypoints[pair[0]]
        part_b = keypoints[pair[1]]
        if part_a[2] > 0 and part_b[2] > 0:  # Check if both keypoints are detected
            cv2.line(image, (int(part_a[0]), int(part_a[1])), (int(part_b[0]), int(part_b[1])), color, thickness)

    return image