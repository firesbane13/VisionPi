class AprilTagDetector:
    def __init__(self, camera_matrix, dist_coeffs):
        self.camera_matrix = camera_matrix
        self.dist_coeffs = dist_coeffs
        self.detector = cv2.aruco.ArucoDetector(cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250))

    def detect_tags(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = self.detector.detectMarkers(gray)
        return corners, ids

    def calculate_pose(self, corners, tag_size):
        if corners:
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, tag_size, self.camera_matrix, self.dist_coeffs)
            angles_distances = []
            for rvec, tvec in zip(rvecs, tvecs):
                pitch = np.arctan2(tvec[0][2], tvec[0][0]) * (180 / np.pi)
                yaw = np.arctan2(tvec[0][1], tvec[0][0]) * (180 / np.pi)
                distance = np.linalg.norm(tvec)
                angles_distances.append((pitch, yaw, distance))
            return angles_distances
        return []